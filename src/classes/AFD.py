from .Automaton import Automaton

class AFD(Automaton):
  def __init__(self, Sigma, Q, delta, q0, F):
    super().__init__(Sigma, Q, delta, q0, F)

  def print(self):
    print('\n######### AFD #########')
    print('Sigma:', self.Sigma)
    print('Q:', self.Q)
    print('delta:', self.delta)
    print('q0:', self.q0)
    print('F:', self.F)
    print('#########################')

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

  def to_min_AFD(self):
    return AFD(self.Sigma, self.Q, self.delta, self.q0, self.F)