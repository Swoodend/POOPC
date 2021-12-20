class Error:
    def __init__(self, pos_start, pos_end, name, message):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.name = name
        self.message = message
        
    def to_string(self):
        msg =  f'{self.name}: {self.message} in '
        msg += f'File {self.pos_start.file_name}, line {self.pos_start.line + 1}'
        return msg
    
class IllegalCharacterError(Error):
    def __init__(self, pos_start, pos_end, message):
        super().__init__(pos_start, pos_end, 'IllegalCharacterError', message)
class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, message):
        super().__init__(pos_start, pos_end, 'InvalidSyntaxError', message)
