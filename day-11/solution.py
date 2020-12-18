import numpy as np
import itertools
from copy import deepcopy



'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("seats.txt", "r")
seat_map = np.array([
    [y for y in x]
        
    for x in list(f.read().split("\n"))
])



'''
    PART 1: DIRECT NEIGHBOURS ARE ADJACENT

    I was unable to find any optimizations to this problem besides using a 
    summed-area table to calculate the amount of adjacent neighbours. This 
    algorithm also avoids using deepcopy.
'''
'''
# Gather seat map size
height, width = seat_map.shape

# Generate occupancy map
occupancy_map = np.zeros((height, width), dtype=int)

# Count the number of changes
curr_changes = 0
prev_changes = -1

while True:
    # Calculate cumulative sum
    I = np.zeros((height + 1, width + 1), dtype=int)
    # Pad with zeros to account for seats along top and left edge
    I[1:(height + 1), 1:(width + 1)] = \
        occupancy_map.cumsum(axis=0).cumsum(axis=1)

    # Iterate through seat map
    for (y, row) in enumerate(seat_map):
        for (x, cell) in enumerate(row):
            # Skip floor tiles
            if cell == ".":
                continue

            # Gather bounds
            x0, y0 = max(0, (x - 1)), max(0, (y - 1))
            x1, y1 = min(width, (x + 2)), min(height, (y + 2))

            # Count neighbours
            # (I(D) + I(A)) - (I(B) + I(C))
            adjacency = \
                (I[y1][x1] + I[y0][x0]) - (I[y0][x1] + I[y1][x0])

            # Account for current seat
            if occupancy_map[y][x] == 1:
                adjacency -= 1

            # No seats nearby
            if adjacency == 0:
                occupancy_map[y][x] = 1
                curr_changes += 1

            # More than 4 seats nearby
            if adjacency >= 4:
                occupancy_map[y][x] = 0
                curr_changes += 1

    # Exit when you detect no change
    if prev_changes == curr_changes:
        break

    # Iterate through the changes
    prev_changes = curr_changes
    curr_changes = 0

print(np.sum(occupancy_map))
'''


'''
    PART 2: DIRECTIONAL NEIGHBOURS ARE ADJACENT

    I was unable to find a method to optimize the adjacency-finding algorithm
    for this part. This algorithm brute-force seeks the adjacency.
'''

# Calculates whether the given position is out of bounds within the shape
def out_of_bounds (shape, position):
    height, width = shape
    x, y = position

    return not ((0 <= x < width) and (0 <= y < height))



# Gather seat map size
height, width = seat_map.shape

# Generate occupancy map
# The current and previous seat map from the iterations
curr_seat_map = deepcopy(seat_map)
prev_seat_map = None

# Loop until the previous and current seat maps are the same
while not np.array_equal(prev_seat_map, curr_seat_map):
    # Copy over current seat map
    prev_seat_map = deepcopy(curr_seat_map)
    
    # Iterate through seat map
    for (y, row) in enumerate(seat_map):
        for (x, cell) in enumerate(row):
            # Skip floor tiles
            if cell == ".":
                continue

            # Total adjacency of current cell
            adjacency = 0

            # Only perform operations on valid seats
            for (dx, dy) in itertools.product([-1, 0, 1], repeat=2):
                # Skip no direciton
                if (dx, dy) == (0, 0):
                    continue

                # Travel in straight direction
                for i in itertools.count(1):
                    nx, ny = (x + (dx * i)), (y + (dy * i))

                    # Break out of bounds
                    if out_of_bounds(prev_seat_map.shape, (nx, ny)):
                        break

                    # Check seat
                    if prev_seat_map[ny][nx] != ".":
                        # Only count occupied seats
                        # Break on first occurence
                        adjacency += (prev_seat_map[ny][nx] == "#")
                        break

            # No seats nearby
            if adjacency == 0:
                curr_seat_map[y][x] = "#"

            # More than 4 seats nearby
            if adjacency >= 5:
                curr_seat_map[y][x] = "L"

print(np.count_nonzero(curr_seat_map == "#"))