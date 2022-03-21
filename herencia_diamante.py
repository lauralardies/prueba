class A:
    def __init__(self, a):
        self.a = a

class B(A):
    def __init__(self, a, b):
        A.__init__(self, a) # Define self.a = a
        self.b = b

class C(A):
    def __init__(self, a, c):
        A.__init__(self, a) # Define self.a = a
        self.c = c

class D(B, C):
    def __init__(self, a, b, c):
        B.__init__(self, a, b) # Define self.a = a y self.b = b
        C.__init__(self, a, c) # Define self.a = a y self.c = c

d = D(1, 2, 3)
# La función isinstance nos dice si la clase A queda contenida en la variable d, y lo mismo con las clases B y C. Como eso es verdad,
# nos devuelve true.
print(isinstance(d, A), isinstance(d, B), isinstance(d, C))
print(d.a, d.b, d.c)