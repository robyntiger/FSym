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

        # for some reason it adds empty spaces and i dunno why
        # so get rid of them
        for item in self.prog:
            if item == '':
                self.prog.remove('')

    # pushes to stack
    def push(self, *arg):
        for item in arg:
            self.stack.append(item)

    # pops stack and returns item
    def pop(self):
        item = self.stack[-1]
        self.stack.pop()

        return item

    # for debugging hhh
    def debug(self):
        print("BRUH")

    def run_commands(self, program):
        switcher = {
            ':)': self.pop,
            ':S': self.debug,
            ':@': lambda a, b: self.push(a+b),
            ':$': self.debug,
            'xp': self.debug
        }

        self.split(program)

        for item in self.prog:
            try:
                switcher[item](1, 4)
            except KeyError:
                # push
                pass

        print(self.stack)


test = Run()
test.run_commands(":)")