import sys


def parse_data(datalines):
    snowdata = {}
    mode = " "
    for data in datalines:
        if data.startswith('seeds:'):
            mode = 'seeds'
            snowdata.update({mode: [x for x in data.split(':')[1].strip().split(" ")]})
        elif data.startswith('seed-to-soil map:'):
            mode = 'seed-to-soil'
        elif data.startswith('soil-to-fertilizer map:'):
            mode = "soil-to-fertilizer"
        elif data.startswith('fertilizer-to-water map:'):
            mode = "fertilizer-to-water"
        elif data.startswith('water-to-light map:'):
            mode = "water-to-light"
        elif data.startswith('light-to-temperature map:'):
            mode = 'light-to-temperature'
        elif data.startswith('temperature-to-humidity map:'):
            mode = 'temperature-to-humidity'
        elif data.startswith('humidity-to-location map:'):
            mode = "humidity-to-location"
        elif data.isspace() or data == " ":
            pass
        else:
            if data:
                if mode not in snowdata.keys():
                    snowdata.update({mode: [[x for x in data.split(" ")]]})
                else:
                    snowdata[mode].append([x for x in data.split(" ")])
    print(snowdata)


# TODO: Find keyboard combination to switch to terminal from editor
if __name__ == '__main__':
    if sys.argv[1] == 'test':
        filename = '5.in'
    datalines = open(filename).read().strip().split('\n')
    parse_data(datalines)
