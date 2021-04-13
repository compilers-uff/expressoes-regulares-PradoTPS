from classes.AFD import AFD
from classes.AFN import AFN
from classes.AFNe import AFNe
from classes.ER import ER

from functions.matcher import match

def main():
  afd = AFD(
    ['a','b'],
    ['q0', 'q1', 'q2'],
    {
      'q0': [
        ['a', 'q1'],
        ['b', 'q2']
      ],
      'q1': [
        ['a', 'q0'],
        ['b', 'q2']
      ],
      'q2': [
        ['a', 'q2'],
        ['b', 'q2']
      ]
    },
    'q0',
    ['q2']
  )

  er = ER('+(*(a),b)')
  afne = er.erToAFNe()
  afne.print()

main()