'''
FSym
Robyn Leinster
'''

# THIS IS SO MESSY AAA

import re

class Run:
    def __init__(self):
        self.COMMAND = '(:\)|:S|:@|xp|:D|:3|^^|:\(|:p|:&|:O|xD|;\)|\(;|8\)|\(8|B\)|:L|:d|:v|:\]|\[:|:\'\(|:#| )'
        self.stack = [1, 2, 3]
        self.prog = []

    # splits a program up by command
    def split(self, program):
        self.prog = re.split(self.COMMAND, program)

        # remove empty lines & spaces
        self.prog = [item for item in self.prog if item.strip()]

    # pushes to stack
    def stack_push(self, *arg):
        for item in arg:
            self.stack.append(item)

    # pops stack and returns item
    def stack_pop(self):
        if self.stack:
            item = self.stack[-1]
            self.stack.pop()

            return item
        else:
            pass

    def run_commands(self, txt):
        # test
        switcher = {
            ':)': lambda: self.stack_pop(),
            ':@': lambda: self.stack_push(int(self.stack_pop()) + int(self.stack_pop())),
            ';)': lambda: [print(item) for item in self.stack]
        }

        test2 = [';)']

        for item in test2:
            switcher[item]()

test = Run()
test.run_commands("")