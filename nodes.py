class NumberNode:
    def __init__(self, token):
        self.token = token
        
    def __repr__(self):
        return f'{self.token}'

class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node
        
    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'
    
    
class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node
        
    def __repr__(self):
        return f'{self.op_tok}, {self.node}'