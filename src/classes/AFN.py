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

  @staticmethod
  def to_AFD(er):
    return AFD()