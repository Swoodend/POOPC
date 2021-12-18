from lexer import Lexer

class Shell:

    @staticmethod
    def run():
        while True:
            text = input('basic > ')
            result, error = Lexer(text).make_tokens()
            
            if (error):
                print(error.to_string())
            else:
                print(result)


if (__name__ == '__main__'):
    Shell.run()
