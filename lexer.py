# take raw source code as series of characters
# group it into a series of chunks called tokens
import re

class Lexer:
    # prints each char
    def scanner(self, code):
        i = 1
        for char in code:
            print('char ' + str(i) + ":" + char)
            i+1

    # initial lexer, splits only by whitespace
    def lexer(self, code):
        lexeme = ''
        for i in range(len(code)):
            if code[i] == ' ':
                print(lexeme)
                lexeme = ''
            else:
                lexeme = lexeme + code[i]
        print(lexeme)

    # experimental lexer thingy
    def lextest(self, code):
        # keywords regex
        KEYWORDS = '(xP|:D|:O|:\)|\(:|;\)|;D|;O)'
        test =re.split(KEYWORDS, code)
        if test[-1] == '':
            test.pop()

        print(test)

test = Lexer()
test.lextest('11xP hi :D')