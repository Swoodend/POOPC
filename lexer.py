from token import Token, TokenType, DIGITS, VALID_CONSECUTIVE_DIGITS
from error import IllegalCharacterError
from position import Position

##########################################################
# LEXER - split stringified program into meaningful tokens
##########################################################

class Lexer:
    def __init__(self, text, file_name):
        self.text = text
        self.file_name = file_name
        self.pos = Position(-1, 0, -1, file_name, text)
        self.current_char = None
        self.advance()
        
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None
        
    def make_tokens(self):
        tokens = []
        
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(TokenType.PLUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TokenType.MINUS, pos_start=self.pos))
                self.advance()             
            elif self.current_char == '/':
                tokens.append(Token(TokenType.DIV, pos_start=self.pos))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TokenType.MUL, pos_start=self.pos))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TokenType.LPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TokenType.RPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char in DIGITS:
                consecutive_digits = []
                is_float = False
                pos_start = self.pos.copy()
                
                while self.current_char != None and self.current_char in VALID_CONSECUTIVE_DIGITS:
                    if self.current_char == '.':
                        if is_float: break
                        is_float = True
                         
                    consecutive_digits.append(self.current_char)
                    self.advance()
                
                if is_float:
                    tokens.append(Token(TokenType.FLOAT, float(''.join(consecutive_digits)), pos_start, self.pos))
                else:
                    tokens.append(Token(TokenType.INT, int(''.join(consecutive_digits)), pos_start, self.pos))
            else:
                pos_start = self.pos.copy()
                return [], IllegalCharacterError(pos_start, self.pos, "Encountered illegal character: '" + self.current_char + "'")
        
        tokens.append(Token(TokenType.EOF, pos_start=self.pos))                                
        return tokens, None
        
    