import sys
from src.functions.matcher import match

def main():
  if (len(sys.argv) < 1): raise Exception('Must pass params "-f file word" or "er word"')

  if (sys.argv[1] == '-f'):
    file_name = sys.argv[2]
    word = sys.argv[3]

    file = open(file_name, 'r')

    for er in file:
      er = er.replace('\n','')
      print("match(" + er + "," + word + ") == " + match(er, word))
  else:
    er = sys.argv[1]
    word = sys.argv[2]

    print("match(" + er + "," + word + ") == " + match(er, word))

main()