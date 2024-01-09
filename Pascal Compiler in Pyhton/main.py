import re

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {self.value})"


class PascalLexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def error(self):
        raise Exception("Invalid character")

    def get_next_token(self):
        if self.pos >= len(self.text):
            return Token("EOF")

        current_char = self.text[self.pos]

        if re.match(r'\d', current_char):
            token = self.get_number()
        elif re.match(r'\+', current_char):
            token = Token("PLUS", current_char)
            self.pos += 1
        elif re.match(r'\s', current_char):
            self.pos += 1
            return self.get_next_token()
        else:
            self.error()

        return token

    def get_number(self):
        result = ""
        while self.pos < len(self.text) and re.match(r'\d', self.text[self.pos]):
            result += self.text[self.pos]
            self.pos += 1
        return Token("INTEGER", int(result))


# Example usage
text = "123 + 456"
lexer = PascalLexer(text)

while True:
    token = lexer.get_next_token()
    print(token)
    if token.type == "EOF":
        break
