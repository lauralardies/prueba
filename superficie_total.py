class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion
        self.ventanas = []

class Ventana:
    def __init__(self, pared, superficie):
        self.pared = pared
        self.superficie = superficie
        self.pared.ventanas.append(self)
        
class Casa:
    def __init__(self, paredes):
        self.paredes = paredes

    def superficie_cristal(self):
        superficie = 0
        for pared in self.paredes:
            for ventana in pared.ventanas:
                superficie += ventana.superficie
        return superficie

# Definimos las paredes
pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")

# Definimos las paredes
ventana_norte = Ventana(pared_norte, 0.5)
ventana_oeste = Ventana(pared_oeste, 1)
ventana_sur = Ventana(pared_sur, 2)
ventana_este = Ventana(pared_este, 1)

# Definimos las paredes que forman la casa
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])

print(casa.superficie_cristal())

class ParedCortina(Pared, Ventana):

    def __init__(self, orientacion, superficie):
        Pared.__init__(self, orientacion)
        Ventana.__init__(self, self, superficie)

# Definimos que la pared cortina de nuestra casa, que en esta casa es la pared sur
pared_cortina = ParedCortina("SUR", 10)
casa.paredes[2] = pared_cortina

print(casa.superficie_cristal())