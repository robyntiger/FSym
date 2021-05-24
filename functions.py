class Functions:
    def __init__(self):
        self.stack = []
        self.prog = []
        self.curr_index = 0
        self.return_index = 0

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

    def loop(self):
        if self.stack[-1] != 0:
            # find matching ':p'
            i = 1
            index = self.curr_index
            while i > 0:
                index = index - 1
                if self.prog[index] == ':d':
                    i = i+1
                elif self.prog[index] == ':p':
                    i = i-1
                else:
                    pass

            self.curr_index = index
        else:
            pass

    # continue or go to end of loop
    def cont(self):
        if self.stack[-1] == 0:
            # find matching ':p'
            i = 1
            index = self.curr_index
            while i > 0:
                index = index + 1
                if self.prog[index] == ':p':
                    i = i + 1
                elif self.prog[index] == ':d':
                    i = i - 1
                else:
                    pass

            self.curr_index = index
        else:
            pass

    # not sure if this is even allowed but whatever qwq
    def swap(self):
        a = self.stack_pop()
        b = self.stack_pop()
        self.stack_push(a)
        self.stack_push(b)

    def run_commands(self, program):
        self.prog = program

        # new switcher yay
        switcher = {
            ':)': lambda: self.stack_pop(),
            ';)': lambda: self.swap(),
            ':&': lambda: self.stack_push(self.stack_pop()+self.stack_pop()),
            ':S': lambda: self.stack_push(self.stack_pop()-self.stack_pop()),
            ':3': lambda: self.stack_push(self.stack_pop()*self.stack_pop()),
            ':/': lambda: self.stack_push(int(self.stack_pop()/self.stack_pop())),
            'xD': lambda: self.stack_push(int(bool((not self.stack_pop())))),
            'x3': lambda: self.stack_push(int(bool((self.stack_pop() and self.stack_pop())))),
            'xp': lambda: self.stack_push(int(bool((self.stack_pop() or self.stack_pop())))),
            ':p': lambda: self.cont(),
            ':d': lambda: self.loop(),
            ':D': lambda: self.stack_push(self.stack[-1]),
            ':o': lambda: print(self.stack_pop(), end=''),
            ':@': lambda: print(chr(self.stack_pop()), end=''),
            ':#': lambda: [print(item, end='') for item in reversed(self.stack)]
        }

        while self.curr_index < len(self.prog):
            try:
                switcher[self.prog[self.curr_index]]()
            except:
                try:
                    if self.prog[self.curr_index].isdigit():
                        self.stack_push(int(self.prog[self.curr_index]))
                    else:
                        self.stack_push(ord(self.prog[self.curr_index]))
                except:
                    break

            self.curr_index = self.curr_index + 1