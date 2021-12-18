from token import Token, TokenType, DIGITS, VALID_CONSECUTIVE_DIGITS
from error import IllegalCharacterError

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.advance()
        
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
        
    def make_tokens(self):
        tokens = []
        
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(TokenType.PLUS, None))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TokenType.MINUS, None))
                self.advance()             
            elif self.current_char == '/':
                tokens.append(Token(TokenType.DIV, None))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TokenType.MUL, None))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TokenType.LPAREN, None))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TokenType.RPAREN, None))
                self.advance()
            elif self.current_char in DIGITS:
                consecutive_digits = []
                is_float = False
                
                while self.current_char != None and self.current_char in VALID_CONSECUTIVE_DIGITS:
                    if self.current_char == '.':
                        if is_float: break
                        is_float = True
                         
                    consecutive_digits.append(self.current_char)
                    self.advance()
                
                type = TokenType.FLOAT if is_float else TokenType.INT
                tokens.append(Token(type, ''.join(consecutive_digits)))
            else:
                return [], IllegalCharacterError("Encountered illegal character: '" + self.current_char + "'")
                                
        return tokens, None
        
    