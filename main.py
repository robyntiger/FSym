# gonna rewrite the lexer since its broken and i kinda know what I'm doing now
import re

class Lexer:
    def __init__(self):
        # regexes for splitting lines up
        self.KEYWORD = ';\)|;D|;o|:d'
        self.SEPARATOR = ':\(|:\)|:\||\|:'
        self.OPERATOR = ':&|:P|xD|:/|8\)|:D|:D:D|:<|:<:D|:>|:>:D|:&:&|:L'
        self.LITERAL = '(?=\^\^).*(?<=\^\^)'
        self.COMMENT = '?=:3'
        self.ENDLINE = '/:x'

    # splits a string by a regex
    def splitter(self, regex, text):
        lines = re.split(regex, text)

        if lines[-1] == '':
            lines.pop()  # to remove ending blank space
        elif lines[0] == '':
            lines.pop(0)  # to remove beginning blank space
        else:
            pass

        return lines

        # Splits the string by endlines (^^) then splits by keywords
    def line_scan(self, code):
        # splits by regex
        new_lines = self.splitter(self.ENDLINE, code)

        # create 2d array for each new line
        line_split = []

        # each array in line_split is each new line split by the keywords
        for i in range(len(new_lines)):
            line_split.append([])
            #regexe_list = [self.KEYWORD, self.SEPARATOR,,,]
            #new_regex = "|".join(regexe_list)
            new_regex = re.compile("(%s|%s|%s|%s|%s)" % (self.KEYWORD, self.SEPARATOR, self.OPERATOR, self.LITERAL, self.COMMENT))
            print(new_regex)
            line_split[i] = self.splitter(new_regex, new_lines[i])

        print(line_split)

        return line_split

test = Lexer()
test.line_scan("test:3")