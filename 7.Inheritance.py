# Python program to
# demonstrate init with
# inheritance
 
class A(object):
    def __init__(self, something):
        print("A init called")
        self.something = something
 
 
class B(A):
    def __init__(self, something):
        # Calling init of parent class
        A.__init__(self, something)
        print("B init called")
        self.something = something
 
 
obj = B("Something")




# Python program to
# demonstrate init with
# inheritance
 
class A1(object):
    def __init__(self, something):
        print("A1 init called")
        self.something = something
 
 
class B1(A1):
    def __init__(self, something):
        print("B1 init called")
        self.something = something
        # Calling init of parent class
        A1.__init__(self, something)
 
 
obj = B1("Something")
