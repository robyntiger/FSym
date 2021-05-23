# command line test
from functions import *
from lexer import *

import sys

filename = sys.argv[1]

with open(filename, 'r') as file:
    data = str(file.read().replace('\n', ''))

command_line = Functions()

if lexer(data) != "Error":
    command_line.run_commands(lexer(data))
else:
    print("Error")


'''command_line = Functions()
while True:
    curr_line = input("meow> ")
    if lexer(curr_line) != "Error":
        command_line.run_commands(lexer(curr_line))
    else:
        print("Error")'''

