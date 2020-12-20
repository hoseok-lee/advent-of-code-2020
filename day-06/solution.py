'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("answers.txt", "r") as f:
    raw_lines = f.read()

# Split the file twice, once by double new-line and once by new-line
answers_grouped = [
    x.split("\n")
        
    for x in raw_lines.split("\n\n")
]



'''
    PART 1: PROCESS GROUPS

    Complexity: O(n)

    The solution simply requires counting the total number of unique letters in 
    each group and adding them all up.
'''
'''
# Force the strings into a set to ignore duplicates, and then find the length
total_count = sum([
    len(set("".join(group))) 
    
    for group in answers_grouped
])

print(total_count)
'''


'''
    PART 2: FIND COMMON ANSWERS

    Complexity: O(n^2)

    Using the sets from the previous part, you can find the intersection between 
    each individual in each group to find the common answers.
'''

total_count = 0

# Put each individual from each group's answers into a set and find the 
# intersection between all
for group in answers_grouped:
    # A set including all the possible answers
    result = set("abcdefghijklmnopqrstuvwxyz")

    # For each individual, update the new intersection
    for individual in group:
        result.intersection_update(set(individual))

    # Measure the total number of answers
    total_count += len(result)

print(total_count)