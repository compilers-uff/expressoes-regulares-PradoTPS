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
  concatenation_sigma = list(set(['E'] + left_er.Sigma + right_er.Sigma))
  concatenation_q = list(set(left_er.Q + right_er.Q))
  concatenation_delta = {
    **left_er.delta,
    **right_er.delta,
    left_er.F[0]: [
      ['E', right_er.q0]
    ]
  }
  concatenation_q0 = left_er.q0
  concatenation_f = [right_er.F[0]]

  return AFNe(
    concatenation_sigma,
    concatenation_q,
    concatenation_delta,
    concatenation_q0,
    concatenation_f
  )

def _successive_concatenation_operation_AFNe(er, depth):
  current_initial_state = 'q0' + str(depth)
  current_final_state = 'qf' + str(depth)

  successive_concatenation_sigma = list(set(['E'] + er.Sigma))
  successive_concatenation_q = list(set([current_initial_state, current_final_state] + er.Q))
  successive_concatenation_delta = {
    current_initial_state: [
      ['E', er.q0],
      ['E', current_final_state]
    ],
    er.F[0]: [
      ['E', er.q0],
      ['E', current_final_state]
    ],
    **er.delta
  }
  successive_concatenation_q0 = current_initial_state
  successive_concatenation_f = [current_final_state]

  return AFNe(
    successive_concatenation_sigma,
    successive_concatenation_q,
    successive_concatenation_delta,
    successive_concatenation_q0,
    successive_concatenation_f
  )

def _er_to_AFNe_recursive(prefixed_er, depth):
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
    return _union_operation_AFNe(_er_to_AFNe_recursive(prefixed_er_dict['left'], depth + 1), _er_to_AFNe_recursive(prefixed_er_dict['right'], depth + 2), depth)
  if (prefixed_er_dict['operation'] == '.'):
    return _concatenation_operation_AFNe(_er_to_AFNe_recursive(prefixed_er_dict['left'], depth + 1), _er_to_AFNe_recursive(prefixed_er_dict['right'], depth + 2), depth)
  if (prefixed_er_dict['operation'] == '*'):
    return _successive_concatenation_operation_AFNe(_er_to_AFNe_recursive(prefixed_er_dict['left'], depth + 1), depth)

  raise Exception('Error on recursive er to afne')

class ER:
  def __init__(self, prefixed_er):
    self.prefixed_er = prefixed_er.replace(' ', '')

  def print(self):
    print('\n########## ER ##########')
    print('Prefixed ER:', self.prefixed_er)
    print('########################')

  def to_AFNe(self):
    return _er_to_AFNe_recursive(self.prefixed_er, 0)