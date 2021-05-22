'''
FSym
Robyn Leinster
'''

# THIS IS SO MESSY AAA

import re

class Run:
    def __init__(self):
        self.COMMAND = '(:\)|:S|:@|xp|:D|:3|^^|:\(|:p|:&|:O|xD|;\)|\(;|8\)|\(8|B\)|:L|:d|:v|:\]|\[:|:\'\(|:#| )'
        self.stack = []
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
        item = self.stack[-1]
        self.stack.pop()

        return item

    # adds top two numbers in stack
    def add(self):
        self.stack_push(int(self.stack_pop()) + int(self.stack_pop()))

    def run_commands(self, txt):
        self.split(txt)

        switcher = {
            ':)': self.stack_pop,
            ':@': self.add,
        }

        print(self.prog)

        for item in self.prog:
            try:
                # runs command
                switcher[item]()
            except:
                # if it's not a command, it's assumed to be a number
                self.stack_push(item)

        print(self.stack)

test = Run()
test.run_commands("2 2        :@")