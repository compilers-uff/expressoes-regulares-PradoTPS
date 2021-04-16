from .Automaton import Automaton
from .AFN import AFN

class AFNe(Automaton):
  def __init__(self, Sigma, Q, delta, q0, F):
    super().__init__(Sigma, Q, delta, q0, F)

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

  def _get_reachable_states_by_epsilon(self, states, symbol):
    if (len(states) <= 0): return []

    reachable_by_epsilon = []
    reachable_by_symbol = []

    for state in states:
      if (state in self.delta):
        for transition_symbol, transition_state in self.delta[state]:
          if (transition_symbol == 'E'):
            reachable_by_epsilon.append(transition_state)
          if (transition_symbol == symbol):
            reachable_by_symbol.append(transition_state)

    return [*reachable_by_symbol, *self._get_reachable_states_by_epsilon(reachable_by_epsilon, symbol)]

  def to_AFN(self):
    afn_q0 = self.q0
    afn_q = self.Q
    afn_sigma = [elem for elem in self.Sigma if elem != 'E']
    afn_delta = {}

    afn_f = self._get_reachable_final_states(self.F)

    # Changing epsilon transitions to all symbols transitions
    for state in self.Q:
      for symbol in afn_sigma:
        reachable_states = self._get_reachable_states_by_epsilon([state], symbol)

        if (len(reachable_states) > 0):
          state_transitions = []
          if (state not in afn_delta): afn_delta[state] = []
          
          for reachable_state in reachable_states:
            afn_delta[state].append([symbol, reachable_state])

    return AFN(afn_sigma, afn_q, afn_delta, afn_q0, afn_f)