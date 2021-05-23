# command line test
from functions import *
from lexer import *


test = Functions()

while True:
    curr_line = input("meow> ")

    if lexer(curr_line) != "Error":
        test.run_commands(lexer(curr_line))
    else:
        print("Error")
