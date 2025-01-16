class MethodException(Exception):
    def __init__(self, *args, method:bool):
        self.method = method
    def __str__(self):
        return f"{self.method} не является методом поиска."
    
class MessageException(Exception):
    def __init__(self, *args,msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    