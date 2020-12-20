from collections import deque

# The length of the preamble
__PREAMBLE_LENGTH__ = 25

# The amount of new numbers that must be generated at each pass
__GENERATION_LENGTH__ = __PREAMBLE_LENGTH__ - 1



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("xmas.txt", "r") as f:
    raw_lines = f.read()

numbers = list(map(
    int,
    
    raw_lines.split("\n")
))



'''
    PART 1: SEEK SEQUENCE-BREAKING NUMBER

    This algorithm partially uses dynamic programming, as every iteration of the
    main while loop uses part of the solution that has been generated by the
    previous iteration.

    The key part of this algorithm is the list possible_numbers. This list is
    assumed to contain all the possible numbers that the next number in the 
    sequence can take. Before the algorithm runs, the list is populated with
    the preamble, performing every possible combination of the preamble and 
    storing it in the list.

    Note here that the list is kept in a way such that combinations for the 
    possible sums generated using the first number in the preamble (i.e. the
    first number to be removed once the next number in the sequence is
    acepted) is ALWAYS at the start of the list. To be exact, it will be the 
    first (__PREAMBLE_LENGTH__ - 1) numbers, since that is how many combinations
    one number can have with all the other numbers. 

    Using this list, it becomes trivial to check whether the next number in the
    sequence is a possible sum from the last __PREAMBLE_LENGTH__ numbers. If the
    algorithm validates that the new number is valid, the algorithm will push
    out the first (__PREAMBLE_LENGTH__ - 1) numbers mentioned in the last 
    paragraph. 

    Since only one new number is introduced to the sequence, the algorithm
    only needs to generate (__PREAMBLE_LENGTH__ - 1) new combinations. By
    pushing all the new combinations the new number can have with the old 
    sequence, the possible_numbers list still contains all the possible sums.
    
    From a DP perspective, part of the information used to solve the problem
    for the current while-loop iteration can be used to solve the problem for
    the next while-loop iteration. The current pass becomes a sub-problem for
    the future pass. 
'''

# Number that breaks the sequence
sequence_breaker = 0

# This function clears the first sectionof numbers of the total possible numbers
# The first section only contain possible sums involving the number that must be
# removed at the next pass (i.e. the number that gets pushed out once the new
# number is validated)
def clear_first_section (input_list):
    for x in range(__GENERATION_LENGTH__):
        input_list[0] = 0
        input_list.rotate(-1)



# A list of every possible number the next number in the sequence can take
# A deque is used to allow easy rotation in the clear_first_section() function
possible_numbers = deque([0] * (__GENERATION_LENGTH__ ** 2))

# Initialize the possible_numbers with the preamble
for i in range(0, __PREAMBLE_LENGTH__):
    # Iterate foward, generating every possible sum
    for j in range(i + 1, __PREAMBLE_LENGTH__):
        possible_numbers[
            (i * __GENERATION_LENGTH__) +
            (__GENERATION_LENGTH__ - j)
        ] = (numbers[i] + numbers[j])

# Move cursor to the first number after the preamble
cursor = __PREAMBLE_LENGTH__

while cursor < len(numbers):
    # Retrieve the number to generate during this pass
    number_to_validate = numbers[cursor]

    # Validate that this number is one of the possible sums that can be made
    if number_to_validate in possible_numbers:
        # Remove the validated number from the possible sums
        # This is to avoid the number being involved in the possible-sum
        # generation process
        possible_numbers[possible_numbers.index(number_to_validate)] = 0

        # Clear the first section, all the possible sums that involved the 
        # last number to be removed
        clear_first_section(possible_numbers)

    # Could not be validated
    else:
        sequence_breaker = number_to_validate
        break

    # Generate sums for the possible-sum list
    # Note here that we only need to generate __GENERATION_LENGTH__ amount of 
    # sums, since we're assuming possible_numbers already contain all the 
    # possible sums that do not include the new number we just validated;
    # therefore, the there are __GENERATION_LENGTH__ amount of new combinations
    # that can be made with this new introduction of the validated number
    for i in range(cursor - __GENERATION_LENGTH__, cursor):
        relative_position = (i - (cursor - __GENERATION_LENGTH__))
        # Iterate foward
        possible_numbers[
            (relative_position * __GENERATION_LENGTH__) +
            (__GENERATION_LENGTH__ - relative_position - 1)
        ] = (numbers[i] + numbers[cursor])

    cursor += 1

#print(sequence_breaker)



'''
    PART 2: FIND SUM OF CONTIGUOUS SET (SUB-ARRAYS)

    Complexity: O(n)

    This can be done easily using prefix arrays. The algorithm will use single
    traversal while building the prefix array, checking whether a sub-array has
    been found containing the desired sum.
'''

# Initialize prefix array
prefix_array = [0] * len(numbers)
prefix_array[0] = numbers[0]

# Store the sub array indices
starting_index = 0
ending_index = 0

# Traverse through the numbers and perform the algorithm 
for i in range(len(numbers) - 1):
    # Generate future prefix sum
    prefix_array[i + 1] = numbers[i + 1] + prefix_array[i]

    # Seek the difference between the current prefix sum and the sequence break
    difference = prefix_array[i] - sequence_breaker
    
    # Sub array found
    if difference in prefix_array:
        starting_index = prefix_array.index(difference) + 1
        ending_index = i
        break

# Create the sub-array and find the corresponding minimum and maximum
sub_array = numbers[starting_index:(ending_index + 1)]
print(min(sub_array) + max(sub_array))