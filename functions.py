class Functions:
    def __init__(self):
        self.stack = []
        self.prog = []

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

    def run_commands(self):
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
            try:
                switcher[item]()
            except:
                self.stack_push(item)  # pushes num to stack