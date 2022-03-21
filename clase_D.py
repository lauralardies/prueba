from clase_B import B
from clase_C import C

class D(B, C):
    
    def __init__(self, a, b, c):
        B.__init__(self, a, b) # Define self.a = a y self.b = b
        C.__init__(self, a, c) # Define self.a = a y self.c = c
