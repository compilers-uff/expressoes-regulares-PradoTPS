from .Automaton import Automaton
from .AFD import AFD

class AFN(Automaton):
  def __init__(self, Sigma, Q, delta, q0, F):
    super().__init__(Sigma, Q, delta, q0, F)

  def print(self):
    print('\n######### AFN #########')
    print('Sigma:', self.Sigma)
    print('Q:', self.Q)
    print('delta:', self.delta)
    print('q0:', self.q0)
    print('F:', self.F)
    print('#########################')

  def to_AFD(self):
    afd_sigma = self.Sigma
    afd_q0 = self.q0
    afd_q = [self.q0]
    afd_delta = {}
    afd_f = []

    unreachedStates = [self.q0]

    while (len(unreachedStates) > 0):
      compound_state = unreachedStates.pop()

      if (compound_state not in afd_delta.keys()):
        part_states = compound_state.split('#')
        compound_state_transitions = {}

        for current_state in part_states:
          if (current_state in self.delta.keys()):
            for path_symbol, path_state in self.delta[current_state]:
              if (path_symbol not in compound_state_transitions.keys()): compound_state_transitions[path_symbol] = [path_state]
              else: compound_state_transitions[path_symbol] = list(set(compound_state_transitions[path_symbol] + [path_state]))

        compound_state_transitions_list = []
        for symbol in compound_state_transitions.keys():
          new_state = '#'.join(compound_state_transitions[symbol])

          unreachedStates.append(new_state)
          afd_q.append(new_state)
          compound_state_transitions_list.append([symbol, new_state])

        if (len(compound_state_transitions_list) > 0): 
          afd_delta = {
            **afd_delta,
            compound_state: compound_state_transitions_list
          }
    
    for afd_state in afd_q:
      for final_afn_state in self.F:
        if (final_afn_state in afd_state): afd_f = list(set(afd_f + [afd_state]))

    return AFD(afd_sigma, afd_q, afd_delta, afd_q0, afd_f)