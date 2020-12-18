import re
import numpy as np
from functools import reduce



'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("notes.txt", "r")
sections = [
    section
    
    for section in f.read().split("\n\n")
]

# Categories
categories = [
    re.split(r"(.*): (.*) or (.*)", category)[1:-1]

    for category in sections[0].split("\n")
]

# Your ticket
your_ticket = [
    int(field)

    for field in (sections[1].split("\n")[1]).split(",")
]

# Nearby tickets
nearby_tickets = [
    [
        int(field)

        for field in nearby_ticket.split(",")
    ]

    for nearby_ticket in sections[2].split("\n")[1:]
]



'''
    PART 1: DETERMINE INVALID FIELDS

    Complexity: O(n * m)

    The algorithm combines all the invalid fields together to make the validity
    check simpler. The efficiency should not change; it's done in brute force.
'''

# Parse intervals into one list
raw_intervals = list(np.array([
    [
        field_interval
        
        for field_interval in category[1:]
    ]

    for category in categories
]).flat)

# Now that the fields have been merged into one list, parse each individual one
# This just converts string to integer, each interval as a subarray 
field_intervals = sorted([
    [
        int(value)
        
        for value in field_interval.split("-")
    ]

    for field_interval in raw_intervals
])

# The final list of merged intervals
merged_intervals = []

# Record the end of the previous interval to compare with
# Assumes that field_intervals is non-empty
last_end = -1

# Keep manual index counter to account for deletion
idx = 0

# Merge as many intervals as possible
for (start, end) in field_intervals:
    # There are two possible overlaps that will involve merging:
    #   1. The previous interval partially overlaps with the current interval
    #   2. The previous interval completely overlaps the current interval
    # When the algorithm merges, the last interval will be update and the
    # current interval will be removed

    # Note that the algorithm will also merge if the last interval ends when
    # the next interval starts
    if start <= last_end:
        # 1. Partial overlap
        if end > last_end:
            merged_intervals[-1][1] = end

        # 2. Complete overlap
        else:
            # When the last interval completely overlaps the current one, no new
            # intervals are needed to be created; just delete the current one
            # (the one that is overlapped)
            pass

    # Otherwise, just push to the final interval array
    else:
        merged_intervals.append([start, end])

    # Pass on the start and end intervals for the future pass and iterate
    last_end = end


# Validate each field with these new merged intervals
# Add to total sum
total_sum = 0

while idx < len(nearby_tickets):
    # Iterate through all the merged intervals and fields to record any fields
    # that are invalid
    invalid_fields = [
        field
        
        for field in nearby_tickets[idx]
        if not ([
            True
            
            for (start, end) in merged_intervals
            if start <= field <= end
        ])
    ]

    # If there are invalid fields found
    if invalid_fields:
        # Add to total sum
        total_sum += sum(invalid_fields)

        # Delete the ticket for part 2
        del nearby_tickets[idx]
        idx -= 1

    # Iterate
    idx += 1

#print(total_sum)



'''
    PART 2: DETERMINE FIELD TYPE

    The challenge in these two problems were mostly parsing the text for the
    correct information. The actual algorithm is not too complicated.
'''

# Arrange the nearby tickets by field instead of tickets
nearby_tickets_by_field = np.array(nearby_tickets).transpose().tolist()

# Parse categories to generate invalid interval
raw_intervals = [
    [
        field_interval
        
        for field_interval in category[1:]
    ]

    for category in categories
]

# Parse the raw interval strings to retrieve the two valid intervals
# Merge them into one single list, as the algorithm will unpack it properly
valid_intervals = [
    list(np.array([
        [int(x) for x in interval.split("-")]
        
        for interval in field_interval
    ]).flat)

    for field_interval in raw_intervals
]

# Dictionary that relates the index of the field by the name of the field
name_to_idx = {}

# A sorted list to keep track of how many and which each field is invalid for
invalid_matches = []

for (idx, ticket_field) in enumerate(nearby_tickets_by_field):
    # Generate a True/False list of whether the current ticket field in question
    # is valid or invalid for the i-th field
    invalid_match = [
        any([
            True

            for value in ticket_field
            if (not ((x0 <= value <= y0) or (x1 <= value <= y1)))
        ])
    
        for (x0, y0, x1, y1) in valid_intervals
    ]

    # Append to the sorted list
    # The number of invalid matches will be first in order to sort of increasing
    # invalid matches
    invalid_matches.append([
        invalid_match.count(False),
        idx,
        invalid_match
    ])

invalid_matches.sort()

# Iterate through in increasing number of invalid matches
# The algorithm assumes that every unknown ticket field has multiple matching 
# names fields, and is organized such that no two fields have the same amount of
# matching name fields, since that would cause ambiguity in the solution
for (number, unknown_idx, invalid_match) in invalid_matches:
    for (name_field_idx, invalid) in enumerate(invalid_match):
        if not invalid:
            # First come first serve
            if name_field_idx not in name_to_idx:
                name_to_idx[name_field_idx] = unknown_idx
                break

# Generate a list of category field names
category_names = [
    category[0]

    for category in categories
]

# Look for category field names including the word "departure" and multiply
# to the total product
total_product = 1
print(reduce(lambda x, y: x * y, [
    your_ticket[name_to_idx[idx]]

    for (idx, category_name) in enumerate(category_names)
    if "departure" in category_name
]))