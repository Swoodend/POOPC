from enum import Enum

DIGITS = '0123456789'
VALID_CONSECUTIVE_DIGITS = DIGITS + '.'

class TokenType(Enum):
    INT       = 'INT'
    FLOAT     = 'FLOAT'
    PLUS      = 'PLUS'
    MINUS     = 'MINUS'
    MUL       = 'MUL'
    DIV       = 'DIV'
    LPAREN    = 'LPAREN'
    RPAREN    = 'RPAREN'
    
class Token:
    def __init__(self, type, value = None):
        self.type = type
        self.value = value
        
    def __repr__(self):
        return f'{self.type}:{self.value}' if self.value else f'{self.type}'
        