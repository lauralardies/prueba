class Punto2D():

    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y
        
    def traslacion(self, a, b):
        punto = [self.x + a, self.y + b]
        print(punto)
