# command line test
from functions import *
from lexer import *


command_line = Functions()

while True:
    curr_line = input("meow> ")

    if lexer(curr_line) != "Error":
        command_line.run_commands(lexer(curr_line))
    else:
        print("Error")
