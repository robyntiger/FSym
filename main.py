'''
FSym
Robyn Leinster
'''

# THIS IS SO MESSY AAA

import re

class Run:
    def __init__(self):
        self.COMMAND = '(:\)|;\)|:&|:S|:3|:D|:/|:#| )'
        self.stack = [97]
        self.prog = []

    # splits a program up by command
    def split(self, program):
        self.prog = re.split(self.COMMAND, program)

        # remove empty lines & spaces
        self.prog = [item for item in self.prog if item.strip()]

    # pushes to stack
    def stack_push(self, item):
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
        self.split(txt)
        print(self.prog)

        # new switcher yay
        switcher = {
            ':)': lambda: self.stack_pop(),
            ';)': lambda: self.stack_push(self.stack[-1]),
            ':&': lambda: self.stack_push(self.stack_pop()+self.stack_pop()),
            ':S': lambda: self.stack_push(self.stack_pop()-self.stack_pop()),
            ':3': lambda: self.stack_push(self.stack_pop()*self.stack_pop()),
            ':/': lambda: self.stack_push(self.stack_pop()/self.stack_pop()),
            ':D': lambda: self.stack_push(int(1)),
            ':o': lambda: print(self.stack_pop()),
            ':@': lambda: print(chr(self.stack_pop())),
            ':#': lambda: [print(item) for item in self.stack]
        }

        for item in self.prog:
            switcher[item]()
            '''try:
                switcher[item]()
            except:
                self.stack_push(item) # pushes num to stack'''

test = Run()
test.run_commands(":@")