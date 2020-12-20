__X_INCREMENT__ = 3
__Y_INCREMENT__ = 1



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("map.txt", "r") as f:
    raw_lines = f.read()

# Simply split the latitudes by new lines
map_latitudes = list(raw_lines.split("\n"))



'''
    PART 1: WALK ONE SLOPE

    Complexity: O(n)

    This algorithm essentially iterates through each latitude of the map and 
    observes a specific x-position, thus requiring exactly O(n) iterations.
    The illusion of the extension of the map can be solved by using modulus on 
    the x-position after incrementing.
'''
'''
# Number of trees encountered
trees_encountered = 0

# Current location on the map
map_longitude = 0
map_latitude = 0

# Map size
map_width = len(map_latitudes[0])
map_height = len(map_latitudes)

# Iterate through the map
while map_latitude < map_height:
    # Hit a tree
    if map_latitudes[map_latitude][map_longitude] == "#":
        trees_encountered += 1

    # Incremement with wrap-around modulus
    map_longitude = (map_longitude + __X_INCREMENT__) % map_width
    map_latitude += __Y_INCREMENT__

print(trees_encountered)
'''


'''
    PART 2: WALK FIVE SLOPES

    Complexity: O(n)
'''

# All the possible slopes the sled can take
slope_queue = [
    (1, 1), 
    (3, 1), 
    (5, 1), 
    (7, 1), 
    (1, 2)
]

# The final answer asks for the total product
# Initially set it to 0, and multiply-equals each pass
total_product = 1

for slope in slope_queue:
    # Overwrite the slopes
    __X_INCREMENT__, __Y_INCREMENT__ = slope

    # Perform part 1 algorithm with the new slope
    trees_encountered = 0

    # Current location on the map
    map_longitude = 0
    map_latitude = 0

    # Map size
    map_width = len(map_latitudes[0])
    map_height = len(map_latitudes)

    # Iterate through the map
    while map_latitude < map_height:
        # Hit a tree
        if map_latitudes[map_latitude][map_longitude] == "#":
            trees_encountered += 1

        # Incremement with wrap-around modulus
        map_longitude = (map_longitude + __X_INCREMENT__) % map_width
        map_latitude += __Y_INCREMENT__

    # Contribute to final product
    total_product *= trees_encountered

print(total_product)