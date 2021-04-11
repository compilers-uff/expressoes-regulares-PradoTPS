from classes.AFD import AFD
from classes.AFN import AFN
from classes.AFNe import AFNe
from classes.ER import ER

from functions.matcher import match

def main():
  print(AFD(
    ['a','b'],
    ['q0', 'q1', 'q2'],
    {
      'q0': [
        ['a', 'q1'],
        ['b', 'q2']
      ]
    },
    'q0',
    ['q1', 'q2']
  ))

  print(match(ER('+(a,b)'), 'ab'))

main()