'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("starting-numbers.txt", "r") as f:
    raw_lines = f.read()

# Convert to list of integers
starting_numbers = list(map(
    int, 
    
    raw_lines.split(",")
))



'''
    PART 1 + 2: PROCESS MEMORY GAME

    Complexity: O(n)

    The algorithm keeps a dictionary of numbers encountered so far and stores
    the last turn number that the number was mentioned 
'''

# Current and next number to generate
current_number = None
next_number = None

# Turn of the numbers
turn_numbers = {}

# Iterate through the turns from 1 to a specific turn number
for turn_number in range(1, (30000000 + 1)):
    # At the start, pop all the numbers from the starting numbers
    # This will overwrite the new number that was generated from last pass
    if (turn_number - 1) < len(starting_numbers):
        next_number = starting_numbers[turn_number - 1]

    # Retrieve the number that was generated last pass 
    current_number = next_number

    # If the current number has not yet been recorded
    if current_number not in turn_numbers:
        # Force the next number to be 0
        next_number = 0

    # Otherwise, calculate the age of the number using the dictionary
    else:
        next_number = (turn_number - turn_numbers[current_number])

    # Record in the dictionary
    # Note that this step is the same whether the current number is new or not
    turn_numbers[current_number] = turn_number

print(current_number)