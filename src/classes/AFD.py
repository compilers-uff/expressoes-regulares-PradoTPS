from .Automaton import Automaton

def _flag_group_state(group_state, relationship_table):
  if(not relationship_table[group_state]['flag']):
    relationship_table[group_state]['flag'] = True
    for associated_group_state in relationship_table[group_state]['associated_list']:
      _flag_group_state(associated_group_state, relationship_table)

def _get_group_state(first_state, second_state, relationship_table):
  if ('/'.join([first_state, second_state]) in relationship_table):
    return relationship_table['/'.join([first_state, second_state])]
  else:
    return relationship_table['/'.join([second_state, first_state])]

def _get_equivalent_states(states_list, marked_list, relationship_table):
  if (len(states_list) < 1):
    return []

  new_equivalent_states = []

  for state in states_list:
    for group_state in relationship_table.keys():
      if (not relationship_table[group_state]['flag']):
        first_state, second_state = group_state.split('/')
        if ((state == first_state) or (state == second_state)):
          if (first_state not in marked_list):
            new_equivalent_states = list(set([*new_equivalent_states, first_state]))
          if (second_state not in marked_list):
            new_equivalent_states = list(set([*new_equivalent_states, second_state]))
  
  marked_list = list(set([*marked_list, *new_equivalent_states]))

  return list(set([*states_list, *_get_equivalent_states(new_equivalent_states, marked_list, relationship_table)]))

class AFD(Automaton):
  def __init__(self, Sigma, Q, delta, q0, F):
    super().__init__(Sigma, Q, delta, q0, F)

  def accepted(self, word):
    word_list = list(word)
    current_state = self.q0

    for symbol in word_list:
      if (self.Sigma.count(symbol) <= 0): return False
      if (current_state not in self.delta): return False

      changed_state = False

      for path_symbol, path_state in self.delta[current_state]:
        if (path_symbol == symbol):
          current_state = path_state
          changed_state = True

      if (not changed_state): return False

    return self.F.count(current_state) > 0
  
  def _get_state_transition_for_symbol(self, state, symbol):
    if (state in self.delta):
      for path_symbol, path_state in self.delta[state]:
        if (path_symbol == symbol):
          return path_state
    
    return ''

  def to_min_AFD(self):
    min_afd_sigma = self.Sigma.copy()
    min_afd_q = self.Q.copy()
    min_afd_delta = {}
    min_afd_q0 = ''
    min_afd_f = []

    relationship_table = {}

    # Creating relationship table 
    for state_index in range(len(self.Q)):
      for other_state_index in range(state_index + 1, len(self.Q), 1):
        key = '/'.join([self.Q[state_index],self.Q[other_state_index]])

        if (key not in relationship_table):
          relationship_table[key] = { 'flag': False, 'associated_list': [] }

    # Flaging final/not final pairs
    for state_group in relationship_table.keys():
      first_state, second_state = state_group.split('/')

      if ((first_state in self.F) != (second_state in self.F)):
        _flag_group_state(state_group, relationship_table)

    # Flaging nonequivalent pairs
    for state_group in relationship_table.keys():
      if (not relationship_table[state_group]['flag']):
        for symbol in min_afd_sigma:
          first_state, second_state = state_group.split('/')

          first_state_transition = self._get_state_transition_for_symbol(first_state, symbol)
          second_state_transition = self._get_state_transition_for_symbol(second_state, symbol)

          if ((first_state_transition == '' and second_state_transition != '') or (first_state_transition != '' and second_state_transition == '')):
            _flag_group_state(state_group, relationship_table)
          elif (first_state_transition != second_state_transition):
            state_transition_relationship = _get_group_state(first_state_transition, second_state_transition, relationship_table)

            if (not state_transition_relationship['flag']):
              state_transition_relationship['associated_list'].append(state_group)
            else:
              _flag_group_state(state_group, relationship_table)

    # Unifying equivalent states
    ## Building min_afd_q
    for state_group in relationship_table.keys():
      if (not relationship_table[state_group]['flag']):
        first_state, second_state = state_group.split('/')
        if (first_state in min_afd_q):
          equivalent_states = _get_equivalent_states([first_state, second_state], [first_state, second_state], relationship_table)
          equivalent_states_as_one = '&'.join(equivalent_states)

          for equivalent_state in equivalent_states:
            if (equivalent_state in min_afd_q):
              min_afd_q.remove(equivalent_state)

          min_afd_q.append(equivalent_states_as_one)

    ## Building min_afd_delta keys
    for group_state in min_afd_q:
      states_list = group_state.split('&')
      for state in states_list:
        if (state in self.delta):
          if (group_state not in min_afd_delta):
            min_afd_delta[group_state] = self.delta[state].copy()
          else: 
            min_afd_delta[group_state] = [*min_afd_delta[group_state], *self.delta[state]]
            min_afd_delta[group_state] = [elem for index, elem in enumerate(min_afd_delta[group_state]) if elem not in min_afd_delta[group_state][:index]]

    ## Changing references in delta
    for group_state in min_afd_q:
      states_list = group_state.split('&')
      if (len(states_list) > 1):
        for state in states_list:
          for key in min_afd_delta.keys():
            pairs_to_remove = []
            pairs_to_add = []

            for path_symbol, path_state in min_afd_delta[key]:
              if (path_state == state):
                pairs_to_add.append([path_symbol, group_state])
                pairs_to_remove.append([path_symbol, state])
            
            for pair_to_remove in pairs_to_remove:
              min_afd_delta[key].remove(pair_to_remove)
            for pair_to_add in pairs_to_add:
              min_afd_delta[key].append(pair_to_add)

            min_afd_delta[key] = [elem for index, elem in enumerate(min_afd_delta[key]) if elem not in min_afd_delta[key][:index]]

    ## Building q0 and F
    for group_state in min_afd_q:
      states_list = group_state.split('&')

      for state in states_list:
        if (state == self.q0):
          min_afd_q0 = group_state
        if (state in self.F):
          min_afd_f = list(set([*min_afd_f, group_state]))

    return AFD(min_afd_sigma, min_afd_q, min_afd_delta, min_afd_q0, min_afd_f)