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

    # ignores everything after ':(' because that ends the program
    end_index = prog.index(':(')
    prog = prog[:end_index]

    # check if loop is opened and closed
    for item in prog:
        pass

    return prog

lexer(":) :/:( :o:#")