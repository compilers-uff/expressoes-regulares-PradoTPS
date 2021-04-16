from classes.AFD import AFD
from classes.AFN import AFN
from classes.AFNe import AFNe
from classes.ER import ER

from functions.matcher import match

def main():
  er = ER('+(a,b)')
  er.print()
  afne = er.to_AFNe()
  afne.print()
  afn = afne.to_AFN()
  afn.print()
  afd = afn.to_AFD()
  afd.print()
  min_afd = afd.to_min_AFD()
  min_afd.print()
  print(min_afd.accepted('a'))

main()