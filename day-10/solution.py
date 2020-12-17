import numpy as np
from functools import cache



'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("voltages.txt", "r")
voltages = sorted([int(x) for x in list(f.read().split("\n"))])
voltages = np.array([0] + voltages + [(voltages[-1] + 3)])



'''
    PART 1: CALCULATE AND COUNT DIFFERENCES

    The differences can be done quite efficiently using numpy vectors and roll()
    function.
'''

# Calculate differences
differences = np.subtract(voltages, np.roll(voltages, 1))

# The last value will roll over causing the first value to be subtracted
differences[0] = voltages[0]

# Account for the last voltage difference of 3 between the outlet and the device
#print(np.count_nonzero(differences == 1) * \
#    (np.count_nonzero(differences == 3) + 1))



'''
    PART 2: COUNT POSSIBILITIES

    Note that the tribonacci sequence returns the total number of combinations
    of a steadily increasing sequence while mainting a difference of no greater
    than 3.
'''

# Calculates the n-th tribonacci number
# functools.cache helps memoize cached tribonacci values
@cache
def tribonacci(n):
    initial_trib = [0, 0, 1]

    for i in range(n - 3):
        initial_trib.append(sum(initial_trib[i:(i+3)]))

    return initial_trib[-1]



# Total number of possible arrangements
# Set to 1 since we're multiplying combinations
total_count = 1

# Last index of the position of a difference of 3
# Used to measure the current length of sub-sequence of 1's
last_three_diff = 0

# Ignore first difference
for i, difference in enumerate(differences[1:]):
    if (difference == 3):
        # Measure the length of the sub-sequence of 1's
        sub_length = i - last_three_diff

        # Calculate the tribonacci sequence and multiply to total combinations
        total_count *= tribonacci(sub_length + 3)

        # Update the last recorded position of 3
        last_three_diff = i + 1

print(total_count)