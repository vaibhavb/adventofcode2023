import sys
def parse_data(datalines):
    for data in datalines:
        print(data)

if __name__ == '__main__':
    if sys.argv[1] == 'test':
        filename = '5.in'
    datalines = open(filename).read().strip().split('\n')
    parse_data(datalines)
