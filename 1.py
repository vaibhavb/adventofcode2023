import sys

def get_calibration_value(input):
   result = 0
   for line in input:
     digits = []
     for c in line:
        if c.isdigit():
           digits.append(c)
     val = int(digits[0] + digits[-1])
     print(val)
     result = result + val
   print(result)

if __name__ == "__main__":
   filename = sys.argv[1]
   lines = open(filename).read().strip().split('\n')
   get_calibration_value(lines) 
