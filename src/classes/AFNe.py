from .AFN import AFN

class AFNe:
  def __init__(self, Sigma, Q, delta, q0, F):
    self.Sigma = Sigma
    self.Q = Q
    self.delta = delta
    self.q0 = q0
    self.F = F

  def print(self):
    print('\n######### AFNe #########')
    print('Sigma:', self.Sigma)
    print('Q:', self.Q)
    print('delta:', self.delta)
    print('q0:', self.q0)
    print('F:', self.F)
    print('########################')

  def _get_reachable_final_states(self, states):
    if (len(states) <= 0): return []

    transitions_states = []

    for current_state in states:
      for state, transitions in self.delta.items():
        for transition_symbol, transition_state in transitions:
          if (transition_symbol == 'E' and transition_state == current_state):
            transitions_states.append(state)
    
    return [*states, *self._get_reachable_final_states(transitions_states)]

  def _get_reachable_states_by_epsilon(self, states):
    if (len(states) <= 0): return []

    reachable_by_epsilon = []

    for state in states:
      if (state in self.delta):
        for transition_symbol, transition_state in self.delta[state]:
          if (transition_symbol == 'E'):
            reachable_by_epsilon.append(transition_state)

    return [*reachable_by_epsilon, *self._get_reachable_states_by_epsilon(reachable_by_epsilon)]

  def afneToAFN(self):
    afn_q0 = self.q0
    afn_q = self.Q
    afn_sigma = [elem for elem in self.Sigma if elem != 'E']
    afn_delta = self.delta.copy()

    # Changing epsilon transitions to all symbols transitions
    for state in self.Q:
      reachable_states = self._get_reachable_states_by_epsilon([state])

      if (len(reachable_states) > 0):
        afn_delta[state] = [elem for elem in afn_delta[state] if elem[0] != 'E']

        for reachable_state in reachable_states:
          for symbol in afn_sigma:
            afn_delta[state].append([symbol, reachable_state])

        afn_delta[state] = [elem for index, elem in enumerate(afn_delta[state]) if elem not in afn_delta[state][:index]]

    afn_f = self._get_reachable_final_states(self.F)

    return AFN(afn_sigma, afn_q, afn_delta, afn_q0, afn_f)