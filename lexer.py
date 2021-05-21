import re

class Lexer:
    def __init__(self):
        # regexes for splitting lines up
        self.KEYWORD = ';\)|;D|;o|:d'
        self.SEPARATOR = ':\(|:\)|:\||\|:'
        self.OPERATOR = ':&|:P|xD|:/|8\)|:D|:D:D|:<|:<:D|:>|:>:D|:&:&|:L'
        self.LITERAL = '(?=\^\^).*(?<=\^\^)'
        self.COMMENT = '(?=:3)'
        self.ENDLINE = '/:x'

    # splits a string by a regex
    def splitter(self, regex, text):
        lines = re.split(regex, text)

        for line in lines:
            if line == '':
                lines.remove('')

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
            new_regex = re.compile("(%s|%s|%s|%s|%s)" % (self.KEYWORD, self.SEPARATOR, self.OPERATOR, self.LITERAL, self.COMMENT))
            line_split[i] = self.splitter(new_regex, new_lines[i])

        return line_split

    # search string for regex
    def search_string(self, regex, word):
        new_regex = re.compile(regex)

        if new_regex.search(word):
            return True
        else:
            return False

    # tokenizes the split lines
    def tokenizer(self, text):
        code_to_tokenize = self.line_scan(text)
        print(code_to_tokenize)
        token_values = ('T_KEYWORD', 'T_SEPARATOR', 'T_OPERATOR', 'T_LITERAL', 'T_COMMENT', 'T_IDENTIFIER', 'T_NEWLINE')

        # list where token sequences will be saved
        token_list = []

        for i in code_to_tokenize:
            for j in i:
                if self.search_string(self.KEYWORD, j):
                    token_list.append((token_values[0], j))
                elif self.search_string(self.SEPARATOR, j) or self.search_string(self.ENDLINE, text):
                    token_list.append((token_values[1], j))
                elif self.search_string(self.OPERATOR, j):
                    token_list.append((token_values[2], j))
                elif self.search_string(self.LITERAL, j):
                    token_list.append((token_values[3], j))
                elif self.search_string(self.COMMENT, j):
                    token_list.append((token_values[4], j))
                else:
                    token_list.append((token_values[5], j))

            token_list.append((token_values[6], "<newline>")) # newline

        print(token_list)

test = Lexer()
test.tokenizer("test^^please god work^^test:3f;D")