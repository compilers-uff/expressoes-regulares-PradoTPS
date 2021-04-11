class AFD:
  def __init__(self, Sigma, Q, delta, q0, F):
    self.Sigma = Sigma
    self.Q = Q
    self.delta = delta
    self.q0 = q0
    self.F = F

  def accepted(self, word):
    word_list = list(word)
    current_state = self.q0

    for letter in word_list:
      if (self.Sigma.count(letter) <= 0): return False
      if (current_state not in self.delta): return False

      changed_state = False

      for path_letter, path_state in self.delta[current_state]:
        if (path_letter == letter):
          current_state = path_state
          changed_state = True

      if (not changed_state): return False

    return self.F.count(current_state) > 0

  @staticmethod
  def afdToAFDmin(afd):
    return afd