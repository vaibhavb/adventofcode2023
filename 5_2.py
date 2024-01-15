import sys


def process_row(datastring):
    datarow = [int(x) for x in datastring.split(" ")]
    return datarow


def parse_data(datalines):
    snowdata = {}
    map = " "
    for data in datalines:
        if data.startswith('seeds:'):
            map = 'seeds'
            snowdata.update({map: [int(x) for x in data.split(':')[1].strip().split(" ")]})
        elif data.startswith('seed-to-soil map:'):
            map = 'seed-to-soil'
        elif data.startswith('soil-to-fertilizer map:'):
            map = "soil-to-fertilizer"
        elif data.startswith('fertilizer-to-water map:'):
            map = "fertilizer-to-water"
        elif data.startswith('water-to-light map:'):
            map = "water-to-light"
        elif data.startswith('light-to-temperature map:'):
            map = 'light-to-temperature'
        elif data.startswith('temperature-to-humidity map:'):
            map = 'temperature-to-humidity'
        elif data.startswith('humidity-to-location map:'):
            map = "humidity-to-location"
        elif data.isspace() or data == " ":
            pass
        else:
            if data:
                if map not in snowdata.keys():
                    snowdata.update({map: [process_row(data)]})
                else:
                    snowdata[map].append(process_row(data))

    return snowdata


def getrangemap(data, r):
    rangemap = list()
    for r1 in r:
        does_intersect = False
        # do range matches
        for row in data:
            r2 = range(row[0], row[0] + row[2])
            r3 = range(row[1], row[1] + row[2])
            # does it intersect
            if r1.start < r2.stop or r1.stop < r2.stop:
                does_intersect = True
                print(f"Intersect - r1:{r1}, r2:{r2}, r3:{r3}")
                if r2.start < r1.start < r1.stop < r2.stop:
                    # r1:   ---
                    # r2: -------
                    # r3: -------
                    offset = r1.start - r2.start
                    size = r1.stop - r1.start
                    rangemap.append(range(r3.start + offset, r3.start + offset + size))
                elif r2.start < r1.start < r2.stop < r1.stop:
                    # r1:      ------ (seeds)
                    # r2: ------- (seeds in map)
                    # r3: ------- (soil in map)
                    size = r1.start - r2.start
                    rangemap.append(range(r3.start + size, r3.stop))
                    rangemap.append(range(r2.stop, r1.stop))
                elif r1.start < r2.start < r1.stop < r2.stop:
                    # r1: ------
                    # r2:    -------
                    # r3:    -------
                    size = r1.stop - r2.start
                    rangemap.append(range(r1.start, r2.start))
                    rangemap.append(range(r3.start, r3.start + size))
                else:
                    # overlap case
                    pass
            else:
                pass
        # No range matches
        if not does_intersect:
            rangemap.append(r1)

    return rangemap


# TODO: Find keyboard combination to switch to terminal from editor
if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        filename = '5.test'
    else:
        filename = '5.in'
    datalines = open(filename).read().strip().split('\n')
    # parse the data input and choose a data structure
    snowdata = parse_data(datalines)
    # print(snowdata)
    # find location for seeds
    locations = []
    seeds = snowdata["seeds"]
    seed_ranges = list()
    for i in range(0, len(seeds), 2):
        seed_ranges.append(range(seeds[i], seeds[i] + seeds[i + 1]))
    soil_ranges = getrangemap(snowdata['seed-to-soil'], seed_ranges)
    print(f"soil ranges - {soil_ranges}")
    fertilizer_ranges = getrangemap(snowdata['soil-to-fertilizer'], soil_ranges)
    print(f"fertilizer ranges - {fertilizer_ranges}")
    water_ranges = getrangemap(snowdata['fertilizer-to-water'], fertilizer_ranges)
    print(f"water ranges - {water_ranges}")
    light_ranges = getrangemap(snowdata['water-to-light'], water_ranges)
    print(f"light ranges - {light_ranges}")
    temp_ranges = getrangemap(snowdata['light-to-temperature'], light_ranges)
    print(f"temp ranges - {temp_ranges}")
    humidity_ranges = getrangemap(snowdata['temperature-to-humidity'], temp_ranges)
    print(f"humidity ranges - {humidity_ranges}")
    location_ranges = getrangemap(snowdata['humidity-to-location'], humidity_ranges)
    print(f"location ranges - {location_ranges}")
    # min_location_id = location_id if min_location_id is None or location_id < min_location_id else min_location_id
    min_range = min(location_ranges, key=lambda r: r.start)
    print(f"Min range {min_range} and minimum location is {min_range.start}")
    # print(f"Minimum true location is {min_location_id}")
