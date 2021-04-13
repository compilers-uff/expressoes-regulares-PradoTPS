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

def _union_operation_AFNe(left_er, right_er, depth):
  current_initial_state = 'q0' + str(depth)
  current_final_state = 'qf' + str(depth)

  union_sigma = list(set(['E'] + left_er.Sigma + right_er.Sigma))
  union_q = list(set([current_initial_state, current_final_state] + left_er.Q + right_er.Q))
  union_delta = {
    current_initial_state: [
      ['E', left_er.q0],
      ['E', right_er.q0],
    ],
    left_er.F[0]: [
      ['E', current_final_state]
    ],
    right_er.F[0]: [
      ['E', current_final_state]
    ],
    **left_er.delta,
    **right_er.delta
  }
  union_q0 = current_initial_state
  union_f = [current_final_state]

  return AFNe(
    union_sigma,
    union_q,
    union_delta,
    union_q0,
    union_f
  )

def _concatenation_operation_AFNe(left_er, right_er, depth):
  return AFNe([], ['q0'], {}, 'q0', [])

def _successive_concatenation_operation_AFNe(er, depth):
  return AFNe([], ['q0'], {}, 'q0', [])

def _erToAFNeRecursive(prefixed_er, depth):
  initial_state = 'q0' + str(depth)
  final_state = 'qf'+ str(depth)

  if (prefixed_er == ''):
    return AFNe([], [initial_state], {}, initial_state, [])
  if (prefixed_er == 'E'):
    return AFNe([], [initial_state], {}, initial_state, [initial_state])
  if (len(prefixed_er) == 1):
    return AFNe([prefixed_er], [initial_state, final_state], { initial_state: [[prefixed_er, final_state]]}, initial_state, [final_state])

  prefixed_er_dict = _prefixed_er_to_dictionary(prefixed_er)
  depth = depth * 2

  if (prefixed_er_dict['operation'] == '+'):
    return _union_operation_AFNe(_erToAFNeRecursive(prefixed_er_dict['left'], depth + 1), _erToAFNeRecursive(prefixed_er_dict['right'], depth + 2), depth)
  if (prefixed_er_dict['operation'] == '.'):
    return _concatenation_operation_AFNe(_erToAFNeRecursive(prefixed_er_dict['left'], depth + 1), _erToAFNeRecursive(prefixed_er_dict['right'], depth + 2), depth)
  if (prefixed_er_dict['operation'] == '*'):
    return _successive_concatenation_operation_AFNe(_erToAFNeRecursive(prefixed_er_dict['left'], depth + 1), depth)

  raise Exception('Error on recursive er to afne')

class ER:
  def __init__(self, prefixed_er):
    self.prefixed_er = prefixed_er

  def erToAFNe(self):
    return _erToAFNeRecursive(self.prefixed_er, 0)