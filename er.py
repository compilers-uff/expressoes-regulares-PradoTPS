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

      if match(er, word): response = "OK"
      else: response = "Not OK"

      print("match(" + er + "," + word + ") == " + response)
  else:
    er = sys.argv[1]
    word = sys.argv[2]

    if match(er, word): response = "OK"
    else: response = "Not OK"

    print("match(" + er + "," + word + ") == " + response)

main()