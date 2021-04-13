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

  def _getReachableFinalStates(self, states):
    if(len(states) <= 0):
      return []

    transitions_states = []

    for current_state in states:
      for state, transitions in self.delta.items():
        for transition_symbol, transition_state in transitions:
          if (transition_symbol == 'E' and transition_state == current_state):
            transitions_states.append(state)
    
    return [*states, *self._getReachableFinalStates(transitions_states)]

  def afneToAFN(self):
    afn_q0 = self.q0
    afn_q = self.Q
    afn_sigma = [elem for elem in self.Sigma if elem != 'E']
    afn_delta = self.delta.copy()

    # Changing epsilon transitions to all symbols transitions
    for state, transitions in afn_delta.items():
      for transition_symbol, transition_state in transitions:
        if (transition_symbol == 'E'):
          transitions_without_epsilon = []

          for symbol in afn_sigma:
            transitions_without_epsilon.append([symbol, transition_state])
          
          afn_delta[state] = [elem for elem in afn_delta[state] if elem != ['E', transition_state]]
          afn_delta[state].extend(transitions_without_epsilon)
          afn_delta[state] = [elem for index, elem in enumerate(afn_delta[state]) if elem not in afn_delta[state][:index]]

    afn_f = self._getReachableFinalStates(self.F)

    return AFN(afn_sigma, afn_q, afn_delta, afn_q0, afn_f)