from .AFNe import AFNe

class ER:
  def __init__(self, prefixedER):
    self.prefixedER = prefixedER

  @staticmethod
  def erToAFNe(er):
    if (er.prefixedER == ''):
      return AFNe([], ['q0'], {}, 'q0', [])
    if (er.prefixedER == 'E'):
      return AFNe([], ['q0'], {}, 'q0', ['q0'])
    if (len(er.prefixedER) == 1):
      return AFNe([er.prefixedER], ['q0', 'q1'], { 'q0': [[er.prefixedER, 'q1']]}, 'q0', ['q1'])
    
    return AFNe()