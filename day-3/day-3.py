__X_INCREMENT__ = 3
__Y_INCREMENT__ = 1



'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("map.txt", "r")
map_latitudes = list(f.read().split("\n"))



'''
    PART 1: PROCESS INPUTS

    Complexity: O(n)

    This algorithm essentially iterates through each latitude of the map and observes a specific x-position, thus requiring exactly O(n) iterations.
    The illusion of the extension of the map can be solved by using modulus on the x-position after incrementing.
'''
'''
trees_encountered = 0

map_longitude = 0
map_latitude = 0

map_width = len(map_latitudes[0])
map_height = len(map_latitudes)

while map_latitude < map_height:
    if map_latitudes[map_latitude][map_longitude] == "#":
        trees_encountered += 1

    map_longitude = (map_longitude + __X_INCREMENT__) % map_width
    map_latitude += __Y_INCREMENT__

print(trees_encountered)
'''


'''
    PART 2: PROCESS INPUTS

    Complexity: O(n)
'''

slope_queue = [
    (1, 1), 
    (3, 1), 
    (5, 1), 
    (7, 1), 
    (1, 2)
]

total_product = 1

for slope in slope_queue:
    __X_INCREMENT__, __Y_INCREMENT__ = slope

    trees_encountered = 0

    map_longitude = 0
    map_latitude = 0

    map_width = len(map_latitudes[0])
    map_height = len(map_latitudes)

    while map_latitude < map_height:
        if map_latitudes[map_latitude][map_longitude] == "#":
            trees_encountered += 1

        map_longitude = (map_longitude + __X_INCREMENT__) % map_width
        map_latitude += __Y_INCREMENT__

    total_product *= trees_encountered

print(total_product)