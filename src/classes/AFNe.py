class AFNe:
  def __init__(self, Sigma, Q, delta, q0, F):
    self.Sigma = Sigma
    self.Q = Q
    self.delta = delta
    self.q0 = q0
    self.F = F

  @staticmethod
  def erToAFNe(er):
    return AFNe()