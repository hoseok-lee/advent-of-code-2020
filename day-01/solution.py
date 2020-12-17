__GOAL__ = 2020



'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("numbers.txt", "r")
numbers = sorted([
    int(x)
    
    for x in list(f.read().split("\n"))
])



'''
    PART ONE: PERFORM TWO-SUM

    Complexity: O(n)
'''
'''
# Keep track of margins
left = 0
right = len(numbers) - 1

# While no intersection
while left < right:
    current_sum = numbers[left] + numbers[right]

    # Too high
    if current_sum > __GOAL__:
        right -= 1

    # Too low
    elif current_sum < __GOAL__:
        left += 1

    # Found number
    else:
        print(numbers[left] * numbers[right])
        break
'''


'''
    PART TWO: PERFORM SIMPLE THREE-SUM

    Complexity: O(n^2)

    After doing some light research, it seems that any further optimizations of 
    the three-sum algorithm require a lot more work for little performance gain. 
'''

# Only keep track of one margin at first
left = 0

# While the left is 3 numbers from the end
while left < (len(numbers) - 2):
    # Start from the left since it will only increase
    # No need to check any number less than left
    middle = left
    right = len(numbers) - 1

    # While no intersection
    while middle < right:
        current_sum = numbers[left] + numbers[middle] + numbers[right]

        # Too high
        if current_sum > __GOAL__:
            right -= 1

        # Too low
        elif current_sum < __GOAL__:
            middle += 1

        # Found number
        else:
            print(numbers[left] * numbers[middle] * numbers[right])
            break

    left += 1