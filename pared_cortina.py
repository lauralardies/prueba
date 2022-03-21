from pared import Pared
from ventana import Ventana

class ParedCortina(Pared, Ventana):

    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion)
        Ventana.__init__(self, self, superficie)