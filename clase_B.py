from clase_A import A

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a) # Define self.a = a
        self.b = b
