from .AFD import AFD

class AFN:
  def __init__(self, Sigma, Q, delta, q0, F):
    self.Sigma = Sigma
    self.Q = Q
    self.delta = delta
    self.q0 = q0
    self.F = F

  def print(self):
    print('\n######### AFN #########')
    print('Sigma:', self.Sigma)
    print('Q:', self.Q)
    print('delta:', self.delta)
    print('q0:', self.q0)
    print('F:', self.F)
    print('#########################')

  @staticmethod
  def afnToAFD(er):
    return AFD()