# the main file
import re

class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        self.stack.pop()

    def push(self, item):
        self.stack.append(item)

# split it by regex stuff
class Lexer:
    def __init__(self):
        # regex for all the commands
        self.COMMAND = ':)|:S|:@|xp|:D|:3|^^|:(|:p|:&|:O|xD|;)|(;|8)|(8|B)|:L|:d|:v|:]|[:|:\'(|:#'

    # splits a string by a regex
    def splitter(self, regex, text):
        lines = re.split(regex, text)

        for line in lines:
            if line == '':
                lines.remove('')

        return lines

# urghhh
if

'''while True:
    # a command line thingy
    user_input = input("meow> ")'''