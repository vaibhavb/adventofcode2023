import sys

def get_calibration_value(input):
   result = 0
   numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
   replace_numbers =  ["z0ero", "o1ne", "t2wo", "t3hree", "f4our", "f5ive", "s6ix", "s7even", "e8ight", "n9ine"]
   for line in input:
     for n, number in enumerate(numbers):
       line = line.replace(numbers[n], replace_numbers[n])
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
