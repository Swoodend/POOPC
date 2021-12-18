class Error:
    def __init__(self, name, message):
        self.name = name
        self.message = message
        
    def to_string(self):
        return f'{self.name}: {self.message}'
    
class IllegalCharacterError(Error):
    def __init__(self, message):
        super().__init__('IllegalCharacterError',  message)
    