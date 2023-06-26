# A Sample class with init method
class Data:
 
    # __init__ method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Data('PowerBI')
p.say_hi()