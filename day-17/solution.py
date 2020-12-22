import numpy as np
from scipy.ndimage import convolve

# Number of dimensions
__DIMENSIONS__ = 4

# Neighbour check kernel
__KERNEL__ = np.ones([3,] * __DIMENSIONS__)



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("initial-state.txt", "r") as f:
    raw_lines = f.read()

# Import universe
universe = (np.array([
    list(row)

    for row in raw_lines.split("\n")
]) == "#").astype(int)



'''
    PART 1 + 2: SIMULATE CUBES

    This algorithm uses convolution to generate an adjacency matrix of nearest
    neighbours, and generates a new universe for the next pass. 
'''

# Reshape universe for convolution
# Over-pad for constant convolution
universe = np.pad(universe[(None,) * (__DIMENSIONS__ - universe.ndim)], 10)

for _ in range(6):
    # Convolve with neighbour kernel
    neighbours = convolve(universe, __KERNEL__, mode="constant")

    # Generate a new universe with neighbour constraints
    # 1 if there are 3 neighbours (regardless of active or inactive)
    # or there's 4 neighbours and current cube is active
    universe = np.where(
        (universe & (neighbours == 4)) |
        (neighbours == 3), 
        
        1, 0
    )

print(np.sum(universe))