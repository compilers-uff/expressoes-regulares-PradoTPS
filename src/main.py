from classes.AFD import AFD
from classes.AFN import AFN
from classes.AFNe import AFNe
from classes.ER import ER

from functions.matcher import match

def main():
  # afd = AFD(
  #   ['a','b'],
  #   ['q0', 'q1', 'q2'],
  #   {
  #     'q0': [
  #       ['a', 'q1'],
  #       ['b', 'q2']
  #     ],
  #     'q1': [
  #       ['a', 'q0'],
  #       ['b', 'q2']
  #     ],
  #     'q2': [
  #       ['a', 'q2'],
  #       ['b', 'q2']
  #     ]
  #   },
  #   'q0',
  #   ['q2']
  # )

  afne = AFNe(
    ['a', 'E'],
    ['q0', 'q1'],
    {
      'q0': [
        ['a', 'q0'],
        ['E', 'q1']
      ]
    },
    'q0',
    ['q1']
  )
  afn = afne.afneToAFN()
  afn.print()

  # er = ER('+(a,b)')
  # er.print()
  # afne = er.erToAFNe()
  # afne.print()
  # afn = afne.afneToAFN()
  # afn.print()

main()