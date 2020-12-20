from itertools import product

# Dimensions
__DIMENSIONS__ = 4



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("initial-state.txt", "r") as f:
    raw_file = f.read()

# Generate cube locations at tuples
universe = {
    (x, y) + (0,) * (__DIMENSIONS__ - 2)
    
    for y, row in enumerate(raw_file.split("\n"))
    for x, cell in enumerate(list(row))
    if (cell == "#")
}



'''
    PART 1 + 2: GENERATE CUBE FORMATIONS

    The algorithm only keeps a set of the coordinates of the currently occupied
    cube locations. At every pass, the algorithm checks every possible
    coordinate, looks at their neighbours, and checks if the coordinate exists
    in the list of cube locations (i.e. a cube is at that location). This is how
    the number of neighbours are determined. 

    filter() applies this neighbour check at every location and generates a new
    set of cube locations. 
'''

# Check neighbours
def check_neighbours (cube):
    # Generate list of all neighbouring coordinates
    neighbour_cubes = [range(_ - 1, _ + 2) for _ in cube]

    # Generate list of nearby active cubes, by intersecting with all actives
    neighbours = len(universe & set(product(*neighbour_cubes)))

    # Note that neighbours count original cube
    return ((cube in universe) and (neighbours == 4)) or (neighbours == 3)



# Iterate through 6 passes
for _ in range(6):
    universe = set(filter(
        check_neighbours, 
        
        product(range(-(_ + 10), (_ + 10)), repeat=__DIMENSIONS__)
    ))

print(len(universe))