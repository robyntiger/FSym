# take raw source code as series of characters
# group it into a series of chunks called tokens
import re

'''class Lexer:
    # Splits the string by emoticons
    def scanner(self, code):
        # keywords regex
        KEYWORDS = '(xP|:D|:O|:\)|\(:|;\)|;D|;O)'

        # splits by regex
        test =re.split(KEYWORDS, code)
        if test[-1] == '':
            test.pop() # to remove ending blank space

        # output each item
        for i in test:
            print(i)

test = Lexer()
test.scanner('11xP hi :D')'''

# split by ^^
# split each thing individually ???

class Lexer:
    def __init__(self):
        # all keywords the language uses kept in this regex
        # i'll add more later but this is it for now
        self.SPLITTERS = '(?=:3|:&|:P|xD|:/|8\)|:D|:D:D|:<|:<:D|:>|:>:D|:&:&|:L|:\(|:\)|:\||\|:|;\)|;D|;o|:d|(?=\^\^).*(?<=\^\^))'
        self.SEPERATORS = ':\||\|:|:\(|:\|'
        self.OPERATORS = ':&|:P|xD|:/|8\)|:D|:D:D|:<|:<:D|:>|:>:D|:&:&|:L'
        self.KEYWORDS = ';\)|;D|;o|:d'
        self.COMMENTS = '?=:3'
        self.LITERALS = '(?=\^\^).*(?<=\^\^))'

    # splits a string by a regex
    def splitter(self, regex, text):
        lines = re.split(regex, text)
        if lines[-1] == '':
            lines.pop()  # to remove ending blank space
        return lines

    # Splits the string by endlines (^^) then splits by keywords
    def line_scan(self, code):
        # keywords regex
        ENDLINE = '\:x'

        # splits by regex
        new_lines = self.splitter(ENDLINE, code)

        # create 2d array for each new line
        line_split = []

        # each array in line_split is each new line split by the keywords
        for i in range(len(new_lines)):
            line_split.append([])
            line_split[i] = self.splitter(self.SPLITTERS, new_lines[i])

        print(line_split)

        return line_split

    # tokenizes the split lines
    def tokenizer(self, text):
        # our code completely split using the previous functions
        code_to_tokenize = self.line_scan(text)
        token_values = ('T_IDENTIFIER', 'T_KEYWORD', 'T_SEPARATOR', 'T_OPERATOR', 'T_LITERAL', 'T_COMMENT', 'T_NEWLINE')

        # list where token sequences will be saved
        token_list = []

        # go through each line and tokenize it
        for i in code_to_tokenize:
            for j in i:
                # identifiers
                if j not in self.SPLITTERS:
                    token_list.append((token_values[0], j))
                # keywords
                if j in self.KEYWORDS:
                    token_list.append((token_values[1], j))
                # separators
                elif j in self.SEPERATORS:
                    token_list.append((token_values[2], j))
                # operators
                elif j in self.OPERATORS:
                    token_list.append((token_values[3], j))
                # literals
                if j in self.LITERALS or j.isdigit() or isinstance(j, bool):
                    token_list.append((token_values[4], j))
                # comments
                elif j in self.COMMENTS:
                    token_list.append((token_values[5], j))
            # new line
            token_list.append((token_values[6], "<new line>"))

        print(token_list)

test = Lexer()
test.tokenizer("hello:3HHHH:3HHH:xthere:x:D")