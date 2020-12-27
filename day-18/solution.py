import ast



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("expressions.txt", "r") as f:
    raw_lines = f.read()

expressions = raw_lines.split("\n")



'''
    PART 1: MULTIPLICATION DEMOTION

    Complexity: O(n)

    This algorithm uses AST parsing and Python's built-in eval() function to
    override the multiplication order. Expressions are pre-processed by
    replacing certain operations and correcting them in AST parsing.
'''

def special_evaluate (expression):
    # Set up AST parse for eval() function
    root = ast.parse(expression, mode="eval")

    for node in ast.walk(root):
        # Only switch binary operations
        if type(node) == ast.BinOp:
            # Promote division to addition
            node.op = ast.Add() if type(node.op) == ast.Div else ast.Mult()

    # Compile for eval()
    return eval(compile(root, "", "eval"))


'''
print(sum([
    special_evaluate(expression.replace("+", "/"))
    
    for expression in expressions
]))
'''


'''
    PART 2: ADDITION PROMOTION

    Complexity: O(n)
'''

print(sum([
    special_evaluate(expression.replace("*", "-").replace("+", "/"))
    
    for expression in expressions
]))