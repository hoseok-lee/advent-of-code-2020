from copy import deepcopy



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("instructions.txt", "r") as f:
    raw_lines = f.read()

# Parse instructions
instructions = [
    [
        x.split()[0], 
        int(x.split()[1])
    ]

    for x in raw_lines.split("\n")
]



'''
    PART 1: EXECUTE PROGRAM

    Complexity: O(n)

    This algorithm executes the instructions while also detecting for an
    infinite loop.
'''

def execute (instructions):
    # Copy instruction set
    test_instr = deepcopy(instructions)

    # Current program pointer
    cursor = 0
    accumulator = 0

    while cursor < len(test_instr):
        instr_type, instr_val = test_instr[cursor]

        # Flag as visited
        test_instr[cursor][0] = "end"

        # Perform jump
        if instr_type == "jmp":
            cursor += instr_val

        # Accumulate
        elif instr_type == "acc":
            accumulator += instr_val
            cursor += 1

        # No operation
        elif instr_type == "nop":
            cursor += 1
            
        # Already executed instruction at current pointer
        elif instr_type == "end":
            break

    return (accumulator, (cursor == len(test_instr)))

#print(execute(instructions))



'''
    PART 2: MANIPULATE PROGRAM

    Complexity: O(n^2)

    This algorithm flips "jmp" with "nop" and vice versa until the program
    executes until the end.
'''

# Flips instructions only if it's "jmp" or "nop"
def flip (instr_type):
    return ("jmp" if instr_type == "nop" else "nop")



# Run through instructions and test each flip change
for (cursor, instruction) in enumerate(instructions):
    instr_type, instr_val = instruction

    if instr_type != "acc":
        # Flip instrutions
        instructions[cursor][0] = flip(instr_type)

        # Test new set of instructions
        accumulator, finished = execute(instructions)

        # If unsucesful
        if finished is not True:
            # Flip back
            instructions[cursor][0] = instr_type

        # Otherwise, end algorithm
        else:
            print(accumulator)
            break