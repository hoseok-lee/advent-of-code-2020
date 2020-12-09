from dataclasses import dataclass


@dataclass
class Password:
    policy_min: str
    policy_max: str
    policy_str: str
    password:   str


'''
    PROCESS INPUTS
'''

# Open and parse input text
f = open("passwords.txt", "r")
unprocessed_input = list(f.read().split("\n"))

for password_template in unprocessed_input:
    policy, letter, password = password_template.split(" ")
    
    