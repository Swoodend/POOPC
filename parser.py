from token import TokenType
from nodes import BinOpNode, NumberNode, UnaryOpNode
from error import InvalidSyntaxError

########################################################################################
# PARSER - build a syntax tree of the program from the tokens created by the lexer 
########################################################################################

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = -1
        self.advance()
        
    def advance(self):
        self.token_idx += 1
        
        if self.token_idx < len(self.tokens):
            self.current_tok = self.tokens[self.token_idx]
        
        return self.current_tok
    
    def expression(self):
        return self.bin_op(self.term, (TokenType.PLUS, TokenType.MINUS))

    
    def term(self):
        return self.bin_op(self.factor, (TokenType.MUL, TokenType.DIV))
    
    def factor(self):
        res = ParseResult()
        tok = self.current_tok
        
        if tok.type in (TokenType.PLUS, TokenType.MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if (res.error): return res
            return res.success(UnaryOpNode(tok, factor))
        
        elif tok.type in (TokenType.INT, TokenType.FLOAT):
            res.register(self.advance())
            return res.success(NumberNode(tok))
        
        elif tok.type == TokenType.LPAREN:
            res.register(self.advance())
            expr = res.register(self.expression())
            if res.error: return res
            if self.current_tok.type == TokenType.RPAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failure(tok.pos_start, tok.pos_end, f'Expected ")"')
        
        return res.failure(InvalidSyntaxError(tok.pos_start, tok.pos_end, f'Expected int or float but got {tok.type}'))
        
    def bin_op(self, func, ops):
        res = ParseResult()
        left = res.register(func())
        
        if res.error:
            return res
        
        while self.current_tok.type in ops:
            op_tok = self.current_tok
            res.register(self.advance())
            right = res.register(func())
            
            if res.error: return res
            left = BinOpNode(left, op_tok, right)
            
        return res.success(left)
    
    def parse(self):
        res = self.expression()
        if not res.error and self.current_tok.type != TokenType.EOF:
            return res.failure(InvalidSyntaxError(self.current_tok.pos_start, self.current_tok.pos_end, "Expected '+', '-', '*', '/'"))
        return res
    
    
class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None
    
    def register(self, res):
        if isinstance(res, ParseResult):
            if res.error:
                self.error = res.error
            return res.node
        return res
        
    def success(self, node):
        self.node = node
        return self
        
    def failure(self, error):
        self.error = error
        return self