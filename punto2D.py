class Punto2D():

    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y
        
    def traslacion(self, a, b):
        punto = [self.x + a, self.y + b]
        print(punto)

class Punto3D():

    def __init__(self, x, y, z) -> None:
        self.x = x 
        self.y = y
        self.z = z
        
    def traslacion(self, a, b, c):
        punto = [self.x + a, self.y + b, self.z + c]
        print(punto)

a = Punto2D(1, 2) 
a.traslacion(-1, -2) 

b = Punto2D(-3, 0) 
b.traslacion(5, -1) 

c = Punto3D(1,5,-3) 
c.traslacion(0, -2, 1) 