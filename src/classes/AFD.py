class AFD:
  def __init__(self, Sigma, Q, delta, q0, F):
    self.Sigma = Sigma
    self.Q = Q
    self.delta = delta
    self.q0 = q0
    self.F = F

  def accepted(self, word):
    return True

  @staticmethod
  def afnToAFD(er):
    return AFD()

  @staticmethod
  def afdToAFDmin(afd):
    return afd