import re

# not sure if this even counts as a lexer anymore xD
COMMAND_LIST = [':)',';)',':&',':S',':3',':/','xD','x3','xp',':p',':d',':D',':o',':@',':(', ':#']

# checks if character is ascii
def isascii(string):
    if len(string) > 1:
        return False
    else:
        if ord(string) < 128:
            return True

# splits a program up by command
def lexer(program):
    correct_syntax = True

    # split by space
    prog = program.split()

    # check if loop is opened and closed
    func_count = []
    correct_syntax = True

    i = 0
    while i < len(prog) and correct_syntax:
        curr_item = prog[i]

        if curr_item == ':p':
            func_count.append(':p')

        elif curr_item == ':d':
            if len(func_count) == 0:
                correct_syntax = False
            else:
                func_count.pop()

        i = i + 1

    # check if everything is a valid command
    for item in prog:
        if item in COMMAND_LIST or item.isdigit() or isascii(item):
            continue
        else:
            correct_syntax = False

    # return error or program
    if not correct_syntax:
        return "Error"
    else:
        return prog