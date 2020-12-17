'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("boarding-passes.txt", "r")
boarding_passes = [ \
    x \
        
    for x in list(f.read().split("\n")) \
]



'''
    PART 1: PROCESS BOARDING PASSES

    Complexity: O(n)

    This problem can be solved very easily by noticing that the boarding pass 
    is a binary representation of the row and column numbers. All the algorithm 
    has to do is replace F, B, L, and R with binary numbers and convert to 
    decimal.
'''
'''
seat_IDs = []

# Iterate through boarding passes
for boarding_pass in boarding_passes:
    # Determine row
    row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)

    # Determine column
    column = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)

    seat_IDs.append(row * 8 + column)

print(max(seat_IDs))
'''


'''
    PART 2: FIND SEAT

    Complexity: O(n)

    This problem can also be solved pretty quickly by sorting the seat ID's and 
    looking for the missing value.
'''

seat_IDs = []

# Iterate through boarding passes
for boarding_pass in boarding_passes:
    # Determine row
    row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)

    # Determine column
    column = int(boarding_pass[7:].replace("L", "0").replace("R", "1"), 2)

    seat_IDs.append(row * 8 + column)

# Sort seat ID's
seat_IDs = sorted(seat_IDs)

# initial previous seat ID
previous_seat_ID = seat_IDs[0] - 1

# Iterate through sorted seat ID's
for seat_ID in seat_IDs:
    # If there is a disjoint in the sorted list
    if seat_ID != (previous_seat_ID + 1):
        # The disjoint found should be +1 from your missing seat ID
        print(seat_ID - 1)

    previous_seat_ID = seat_ID