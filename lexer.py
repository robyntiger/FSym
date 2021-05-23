import re

# not sure if this even counts as a lexer anymore xD
COMMAND = '(:\)|;\)|:&|:S|:3|:D|:/|xD|x3|xp|:p|:d|:D|:o|:@|:\(|:#| )'
COMMAND_LIST = [':)',';)',':&',':S',':3',':/','xD','x3','xp',':p',':d',':D',':o',':@',':(', ':#']

# splits a program up by command
def lexer(program):
    prog = re.split(COMMAND, program)

    # remove empty lines & spaces, and anything that isnt a command
    prog = [item for item in prog if item.strip()]
    for item in prog:
        if item not in COMMAND_LIST:
            prog.remove(item)

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

    # check if there's an end line
    if ':(' not in prog:
        correct_syntax = False
    else:
        # ignores everything after ':('
        end_index = prog.index(':(')
        prog = prog[:end_index]

    if not correct_syntax:
        print("Error")
        return None
    else:
        return prog