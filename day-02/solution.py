'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("passwords.txt", "r")
password_templates = list(f.read().split("\n"))



'''
    PART 1: OLD POLICY

    Complexity: O(n^2)
'''
'''
# Total number of valid passwords
valid_passwords = 0

# Iterate through the password templates
for password_template in password_templates:
    policy, letter, password = password_template.split(" ")

    # Strip the ":" from the letter
    letter = letter[:-1]

    # Determine minimum and maximum occurence of letter
    policy_min, policy_max = [int(x) for x in policy.split("-")]

    # Count how many occurences of letter in password
    occurence = password.count(letter)

    # Determine validity
    if (occurence >= policy_min) and (occurence <= policy_max):
        valid_passwords += 1

print(valid_passwords)
'''


'''
    PART 2: NEW POLICY

    Complexity: O(n)
'''

# Total number of valid passwords
valid_passwords = 0

# Iterate through the password templates
for password_template in password_templates:
    # Parse the password template
    policy, letter, password = password_template.split(" ")

    # Strip the ":" from the letter
    letter = letter[:-1]

    # Determine first and second position of letter occurence
    policy_one, policy_two = [
        int(x)
            
        for x in policy.split("-")
    ]

    # Determine validity
    # This is the easiest method I could think of that requires a low (and 
    # consistent) amount of comparisons
    flag = 0
    
    if password[policy_one - 1] == letter:
        flag += 1

    if password[policy_two - 1] == letter:
        flag += 1

    if flag == 1:
        valid_passwords += 1

print(valid_passwords)