# command line test
from functions import *
import lexer

import sys

filename = sys.argv[1]

with open(filename, 'r') as file:
    data = file.read().replace('\n', '')

print(data)

'''command_line = Functions()

while True:
    curr_line = input("meow> ")

    if lexer(curr_line) != "Error":
        command_line.run_commands(lexer(curr_line))
    else:
        print("Error")'''
