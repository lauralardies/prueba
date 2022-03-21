class Punto3D():

    def __init__(self, x, y, z) -> None:
        self.x = x 
        self.y = y
        self.z = z
        
    def traslacion(self, a, b, c):
        punto = [self.x + a, self.y + b, self.z + c]
        print(punto)
