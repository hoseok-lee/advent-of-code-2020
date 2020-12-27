import math



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("numbers.txt", "r") as f:
    raw_lines = f.read()

# Sort all the integers
numbers = list(map(
    int,
    
    raw_lines.split("\n")
))



'''
    PART ONE: PERFORM TWO-SUM

    Complexity: O(n)

    This optimized two-sum algorithm uses hash-tables and constant-time look-up
    to find two numbers that sum to the target.
'''

def two_sum (numbers, target):
    # Keep a hash table of observed numbers
    checked_numbers = {}

    for number in numbers:
        complement = target - number

        # Check if the complement is part of the list
        if complement in checked_numbers:
            return [number, complement]

        checked_numbers[number] = number

    return None


'''
print(math.prod(two_sum(numbers, 2020)))
'''


'''
    PART TWO: PERFORM SIMPLE THREE-SUM

    Complexity: O(n^2)

    After doing some light research, it seems that any further optimizations of 
    the three-sum algorithm require a lot more work for little performance gain. 
'''

for idx, number in enumerate(numbers):
    result = two_sum(numbers[:idx] + numbers[(idx + 1):], 2020 - number)

    # If a three-sum has been found
    if result:
        print(math.prod([number] + result))

        break