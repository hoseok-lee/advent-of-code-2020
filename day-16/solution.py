import re



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("notes.txt", "r") as f:
    raw_lines = f.read()

# Categories
fields = [
    [
        name, 
        [int(x0), int(y0)],
        [int(x1), int(y1)]
    ]

    for (name, x0, y0, x1, y1) in re.findall(
        r"((?:\w+ ?)+): (\d+)-(\d+) or (\d+)-(\d+)",
        raw_lines
    )
]

# Your ticket
# Nearby tickets
your_ticket, *nearby_tickets = [
    list(map(int, ticket.split(",")))

    for ticket in re.findall(
        r"^((?:\d+,?)+)$",
        raw_lines,
        flags=re.MULTILINE
    )
]



'''
    PART 1: DETERMINE INVALID FIELDS

    Complexity: O(n * m)
'''

# Check whether current field is invalid against any of the fields
def field_invalid (field_value):
    return not any([
        (x0 <= field_value <= y0) or
        (x1 <= field_value <= y1)

        for field in fields
        for (name, (x0, y0), (x1, y1)) in fields
    ])


'''
# Print the sum of all invalid numbers
print(sum([
    ticket_field

    for ticket in nearby_tickets
    for ticket_field in ticket
    if field_invalid(ticket_field)
]))
'''


'''
    PART 2: DETERMINE FIELD TYPE

    The challenge in these two problems were mostly parsing the text for the
    correct information. The actual algorithm is not too complicated.
'''

# Generate list of valid tickets
valid_tickets = [
    ticket 

    for ticket in nearby_tickets
    if not any([
        field_invalid(ticket_field)

        for ticket_field in ticket
    ])
]

# Total product for final answer
total_product = 1

# List of currently available fields
available_indices = set(range(len(fields)))

# Iterate through all the possible fields
# This is to de-populate all the available indices, to indicate that we have
# found a solution for every field 
for _ in range(len(fields)):
    # Test each field against a certain column of values in the tickets
    for (idx, (name, (x0, y0), (x1, y1))) in enumerate(fields):
        # Find all the possible ticket fields that matches the current field
        all_possible_fields = [
            field_index

            for field_index in available_indices
            if all([
                (x0 <= ticket[field_index] <= y0) or
                (x1 <= ticket[field_index] <= y1)

                for ticket in valid_tickets
            ])
        ]

        # If only one match could be found, then it's the guaranteed solution
        if len(all_possible_fields) == 1:
            # Remove it from the available list of indices
            # all_possible_fields[0] is the index listed in the ticket list
            available_indices.remove(all_possible_fields[0])

            # Remove the determined field from the list of fields
            # Small optimization
            fields = fields[:idx] + fields[(idx + 1):]

            # Check if name starts with "departure"
            if name.startswith("departure"):
                total_product *= your_ticket[all_possible_fields[0]]

            break
            
print(total_product)