from src.functions.matcher import match

def tester():
  assert match('a', 'a') == 'OK'
  assert match('+(a,b)', 'a') == 'OK'
  assert match('.(a,b)', 'ab') == 'OK'
  assert match('*(+(a,b))', 'a') == 'OK'
  assert match('*(+(a,b))', 'aaa') == 'OK'
  assert match('*(+(a,b))', 'ab') == 'OK'
  assert match('*(+(a,b))', 'aba') == 'OK'
  assert match('*(+(a,b))', 'abababa') == 'OK'
  assert match('*(.(a,b))', 'abababab') == 'OK'
  assert match('+(*(.(a,b)),c)', 'c') == 'OK'
  assert match('+(*(.(a,b)),.(a,*(b)))', 'abbbbbbb') == 'OK'
  assert match('+(*(.(a,b)),.(a,*(b)))', 'abba') == 'Not OK'

tester()