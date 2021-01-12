import numpy as np
import re
import warnings



'''
    PROCESS INPUTS
'''

# Suppress runtime warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=np.VisibleDeprecationWarning)

# Open and parse input text
with open("rules.txt", "r") as f:
    raw_lines = f.read()

# Production rules
R = {
    int(number): [
        list(map(int, pair.strip().split(" "))) if pair not in "ab" 
        else pair
        
        for pair in re.findall(
            r"((?:[0-9ab] ?)+)",
            rule
        )
    ]

    for (number, rule) in re.findall(
        r"(?:(\d+)): ((?:.+ ?)+)",
        raw_lines
    )
}

# Strings to parse
w_list = re.findall(
    r"^((?:\w+,?)+)$",
    raw_lines,
    flags=re.MULTILINE
)



'''
    PART 1: RUN RECURSIVE DESCENT ALGORITHM
    
    Algorithms such as CYK parse and Earley parse are not efficient for this
    problem, since there are quite a few redundant production rules during each
    recognition parse. This results in an unnecessarily large amount of data
    allocated for each input. Instead, a recursive descent parser, though less
    refined, only pulls the production rules necessary.
'''

def parse (w, to_parse):
    # Completed a parse
    if w == '' or to_parse == []:
        return w == '' and to_parse == []
    
    # Unpack first set of rules to parse
    rules = R[to_parse[0]]

    # Check if terminal
    if np.array(["a", "b"]) in np.array(rules):
        if w[0] in rules:
            # Recurse with the remaining strings
            return parse(w[1:], to_parse[1:])
        else:
            # Parse failed
            return False
    
    # Check if nonterminal
    else:
        # If there is a nonterminal, expand the first rule and recurse
        return any(
            parse(w, unchecked + to_parse[1:]) 
            
            for unchecked in rules
        )


'''
print(sum([
    parse(w, [0])

    for w in w_list
]))
'''


'''
    PART 2: MODIFIED RULES
    
    Luckily, the raw recursive descent parser ends when the string parse is
    completed, and will not enter any infinite loops. It will only explore 
    recursive branches if and only if the branching production rule directly
    matches the next character in the string.
'''

# Replace rules
R[8] = [[42], [42, 8]]
R[11] = [[42, 31], [42, 11, 31]]

print(sum([
    parse(w, [0])

    for w in w_list
]))