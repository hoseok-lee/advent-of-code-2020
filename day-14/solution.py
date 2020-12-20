import re
import itertools



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("bit-mask.txt", "r") as f:
    raw_lines = f.read()

# Group each mask with the corresponding memory modules
programs = [
    [
        mask, 
        [
            [int(address), int(value)]
            
            for (address, value) in re.findall(
                r"mem\[(\d+)\] = (\d+)",
                memory
            )
        ]
    ]
    
    for (mask, memory) in re.findall(
        r"mask = ([X10]+)((?:\nmem\[(?:\d+)] = (?:\d+))*)",
        raw_lines
    )
]



'''
    PART 1: APPLY BIT MASKS TO MEMORY VALUE

    Complexity: O(n)

    This is a simple algorithm that iterates through each memory, keeps track of
    the lastest update to a specific address, and applies the bitmasks. I used
    two bit masks:

        1. To force 0's in the final address (AND MASK)
        2. To force 1's in the final address (OR MASK)
'''
'''
# Use a dictionary to choose the most recent write to a certain address
memory_bank = {}

# Iterate through the programs
for general_mask, memory in programs:
    # Will set all 0 masks
    AND_mask = int(general_mask.replace("X", "1"), 2)

    # Will set all 1 masks
    OR_mask = int(general_mask.replace("X", "0"), 2)

    # Update memory bank to overwrite already written addresses
    memory_bank.update({
        mem_addr: (AND_mask & mem_val) | OR_mask

        for (mem_addr, mem_val) in memory
    })

print(sum(memory_bank.values()))
'''


'''
    PART 2: APPLY BIT MASKS TO MEMORY ADDRESS

    Complexity: O(n * m)

    Instead of manually turning on and off every bit and calculating every new
    possible address, the algorithm generates a base address and adds/substracts
    every possible combination of the bit values (in decimal). 

    For example, if "X" was in the first and fourth position, the algorithm
    would first generate the base address assuming all the "X" bits were turned
    on. From here, the algorithm subtracts every possible combination of the 
    first and fourth bit position (i.e turn them off). There are only four 
    combinations of two positions: 

        1. First and fourth both on
        2. First on
        3. Fourth on
        4. First and fourth both off

    This will generate a list of all possible addresses. The algorithm then just
    needs to populate the memory bank dictionary.
'''

# Use a dictionary to choose the most recent write to a certain address
memory_bank = {}

# Retrieve all combinations of bit combinations
def sum_combinations (possible_bits):
    # Store a list of the sum of each combination
    all_sum_combinations = []
    
    # Iterate through all possible sizes of combinations
    for length in range(1, (len(possible_bits) + 1)):
        all_sum_combinations += [
            sum(comb)
            
            for comb in list(itertools.combinations(possible_bits, length))
        ]

    return all_sum_combinations + [0]



# Iterate through the programs
for (general_mask, memory) in programs:
    # Retrieve an index of all the floating bits
    floating_bits = [
        2 ** (len(general_mask) - (result.start() + 1))

        for result in re.finditer("X", general_mask)
    ]

    # Iterate through the memory
    # Each memory generates a certain list of possible addresses
    for (mem_addr, mem_val) in memory:
        # Calculate base memory address
        base_addr = int(general_mask.replace("X", "1"), 2) | mem_addr

        # Update memory bank to overwrite already written addresses
        # Calculate every possible address using combinatorics
        memory_bank.update({
            (base_addr - each_sum_comb): mem_val

            for each_sum_comb in sum_combinations(floating_bits)
        })

print(sum(memory_bank.values()))