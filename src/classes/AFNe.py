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

  def afneToAFN(self):
    afn_q0 = self.q0
    afn_q = self.Q
    afn_sigma = [elem for elem in self.Sigma if elem != 'E']

    return AFN(afn_sigma, self.Q, self.delta, afn_q0, self.F)