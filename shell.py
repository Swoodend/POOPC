from lexer import Lexer

from parser import Parser

class Shell:

    @staticmethod
    def run():
        while True:
            text = input('basic > ')
            tokens, lexError = Lexer(text, '<stdout>').make_tokens()
            
            if (lexError):
                print(lexError.to_string())
                continue
                
            parser = Parser(tokens)
            ast = parser.parse()
            
            if(ast.error):
                print(f'{ast.error.message}')
                continue
            else:
                print(ast.node)            

if (__name__ == '__main__'):
    Shell.run()
