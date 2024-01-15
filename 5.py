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

def getmap(data, idx):
    for row in data:
        if idx in range(row[1], row[1]+row[2]):
            print(f"Is {idx} is in range({row[1]}, {row[2]})")
            return (row[0] + (idx - row[1]))
    return idx

# TODO: Find keyboard combination to switch to terminal from editor
if __name__ == '__main__':
    if sys.argv[1] == 'test':
        filename = '5.test'
    else:
        filename = '5.in'
    datalines = open(filename).read().strip().split('\n')
    # parse the data input and choose a data structure
    snowdata = parse_data(datalines)
    print(snowdata)
    # find location for seeds
    locations = []
    for seed_id in snowdata['seeds']:
        # find soil code
        soil_id = getmap(snowdata['seed-to-soil'], seed_id)
        #print(f"For seeds {seed_id} we have soil {seed_id}")
        # find soil to fertilizer
        fertilizer_id = getmap(snowdata['soil-to-fertilizer'], soil_id)
        #print(f"For soil {soil_id} we have fertilizer {fertilizer_id}")
        # fertilizer-to-water
        water_id = getmap(snowdata['fertilizer-to-water'], fertilizer_id)
        #print(f"For fertilizer {fertilizer_id} we have water {water_id}")
        # water-to-light
        light_id = getmap(snowdata['water-to-light'], water_id)
        # light-to-temperature
        temp_id = getmap(snowdata['light-to-temperature'], light_id)
        # temperature-to-humidity
        humidity_id = getmap(snowdata['temperature-to-humidity'], temp_id)
        # humidity-to-location
        location_id = getmap(snowdata['humidity-to-location'], humidity_id)
        print(f"Seed {seed_id}, soil {soil_id}, fertilizer {fertilizer_id}, water {water_id}, "
              f"light {light_id}, temperature {temp_id}, humidity {humidity_id}, location {location_id}")
        locations.append(location_id)
    print(f"Minimum location is {min(locations)}")