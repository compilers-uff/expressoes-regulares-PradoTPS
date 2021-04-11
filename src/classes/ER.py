from .AFNe import AFNe

def _prefixed_er_to_dictionary(prefixed_er):
  result = {}
  result['operation'] = prefixed_er[0]

  expected_commas = 0
  current_position = 0
  for symbol in prefixed_er:
    if (symbol == '+' or symbol == '.'):
      expected_commas += 1

    if (symbol == '*' and expected_commas == 0):
      result['left'] = prefixed_er[2:-1]
      result['right'] = ''

      return result
    
    if (symbol == ','):
      expected_commas -= 1
      if (expected_commas == 0):
        result['left'] = prefixed_er[2:current_position]
        result['right'] = prefixed_er[current_position + 1:-1]

        return result

    current_position += 1

  raise Exception('Error on er to dictionary')

def _union_operation_AFNe(left_er, rigth_er):
  return AFNe([], ['q0'], {}, 'q0', [])

def _concatenation_operation_AFNe(left_er, rigth_er):
  return AFNe([], ['q0'], {}, 'q0', [])

def _successive_concatenation_operation_AFNe(er):
  return AFNe([], ['q0'], {}, 'q0', [])

def _erToAFNeRecursive(prefixed_er):
  if (prefixed_er == ''):
    return AFNe([], ['q0'], {}, 'q0', [])
  if (prefixed_er == 'E'):
    return AFNe([], ['q0'], {}, 'q0', ['q0'])
  if (len(prefixed_er) == 1):
    return AFNe([prefixed_er], ['q0', 'q1'], { 'q0': [[prefixed_er, 'q1']]}, 'q0', ['q1'])

  prefixed_er_dict = _prefixed_er_to_dictionary(prefixed_er)
  
  if (prefixed_er_dict['operation'] == '+'):
    return _union_operation_AFNe(_erToAFNeRecursive(prefixed_er_dict['left']), _erToAFNeRecursive(prefixed_er_dict['right']))
  if (prefixed_er_dict['operation'] == '.'):
    return _concatenation_operation_AFNe(_erToAFNeRecursive(prefixed_er_dict['left']), _erToAFNeRecursive(prefixed_er_dict['right']))
  if (prefixed_er_dict['operation'] == '*'):
    return _successive_concatenation_operation_AFNe(_erToAFNeRecursive(prefixed_er_dict['left']))
  
  raise Exception('Error on recursive er to afne')

class ER:
  def __init__(self, prefixed_er):
    self.prefixed_er = prefixed_er

  def erToAFNe(self):
    return _erToAFNeRecursive(self.prefixed_er)