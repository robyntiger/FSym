'''
FSym
Robyn Leinster
'''

# THIS IS SO MESSY AAA

import re

class Run:
    def __init__(self):
        #self.COMMAND = ':)|:S|:@|xp|:D|:3|^^|:(|:p|:&|:O|xD|;)|(;|8)|(8|B)|:L|:d|:v|:]|[:|:\'(|:#| '
        self.COMMAND = '(:\)|:S|:@|xp|:D|:3|^^|:\(|:p|:&|:O|xD|;\)|\(;|8\)|\(8|B\)|:L|:d|:v|:\]|\[:|:\'\(|:#| )'
        self.stack = []
        self.prog = []

    def split(self, program):
        self.prog = re.split(self.COMMAND, program)

        # for some reason it adds empty spaces and i dunno why
        # so get rid of them
        for item in self.prog:
            if item == '':
                self.prog.remove('')

    def commands(self):
        switcher = {
            ':3': print("placeholder"),
            ':S': print("placeholder"),
            ':@': print("placeholder"),
            ':$': print("placeholder"),
            'xp': print("placeholder"),
        }

        test = ":3"

        if test in switcher:
            switcher[test]

test = Run()
test.commands()