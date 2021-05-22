# functions

stack = [1, 2, 3]

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

def run_commands(self):
    switcher = {
        ':)': self.stack_pop,
        ':@': self.add,
    }

    test = [":)"]

    for item in test:
        try:
            switcher[item]()
        except:
            self.stack_push(item)

print(stack)