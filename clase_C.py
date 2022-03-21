from clase_A import A

class C(A):
    def __init__(self, a, c):
        A.__init__(self, a) # Define self.a = a
        self.c = c


