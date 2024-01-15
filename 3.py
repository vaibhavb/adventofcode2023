import sys

def get_engine_parts(lines):
   for lineno, line in enumerate(lines):
     print(f"{lineno}: {line}")
     numbers = []
     engine_parts = []
     for chno, ch in enumerate(line):
       if ch.isdigit():
          digits.append(ch)
          
          #print(f"{chno}:D", end='')
       elif ch == ".":
          digits = []
          numbers.append(digit)
          print(f"{chno}:d", end='')
       else:
          print(f"{chno}:S", end='')
     print(digits)


if __name__ == "__main__":
   enginefile = sys.argv[1]
   enginelines = open(enginefile).read().strip().split("\n")
   get_engine_parts(enginelines)   
