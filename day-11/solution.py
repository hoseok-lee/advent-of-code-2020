import numpy as np
import itertools
from copy import deepcopy
from scipy.ndimage import convolve

__KERNEL__ = np.ones([3, 3])



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("seats.txt", "r") as f:
    raw_lines = f.read()

# Split every character into its own cell
seat_map = np.array([
    list(row)
        
    for row in list(raw_lines.split("\n"))
])



'''
    PART 1: DIRECT NEIGHBOURS ARE ADJACENT

    The algorithm uses convolution to generate a matrix of nearest neighbours
    for every cell. It simply brute-force iterates through until no change is
    made from one pass to the next.
'''
'''
# To make sure that seats are only placed on valid places
available = (seat_map == "L").astype(int)

# The previous and current state of convolution
current_state = np.zeros(seat_map.shape).astype(bool)
previous_state = None

# Generate seats until no changes are created
while not np.array_equal(previous_state, current_state):
    # Pass on state at beginning since it's a while loop
    previous_state = deepcopy(current_state)

    # Convolve with neighbour kernel
    neighbours = convolve(previous_state, __KERNEL__, mode="constant")

    # Can only place seats where seats exist
    current_state = np.where(
        available & (
            (previous_state & (neighbours < 5)) |
            (neighbours == 0)
        ),

        1, 0
    )

print(np.sum(current_state))
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