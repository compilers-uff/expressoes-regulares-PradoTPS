from ..classes.AFD import AFD
from ..classes.AFN import AFN
from ..classes.AFNe import AFNe
from ..classes.ER import ER

def match(er, word):
  if ER(er).to_AFNe().to_AFN().to_AFD().to_min_AFD().accepted(word):
    return 'OK'
  else:
    return 'Not OK'