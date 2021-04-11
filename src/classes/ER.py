from .AFNe import AFNe

def _erToAFNeRecursive(prefixedER):
  if (prefixedER == ''):
    return AFNe([], ['q0'], {}, 'q0', [])
  if (prefixedER == 'E'):
    return AFNe([], ['q0'], {}, 'q0', ['q0'])
  if (len(prefixedER) == 1):
    return AFNe([prefixedER], ['q0', 'q1'], { 'q0': [[prefixedER, 'q1']]}, 'q0', ['q1'])
  
  return AFNe()

class ER:
  def __init__(self, prefixedER):
    self.prefixedER = prefixedER

  @staticmethod
  def erToAFNe(er):
    return _erToAFNeRecursive(er.prefixedER)