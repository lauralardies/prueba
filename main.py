from punto2D import Punto2D
from punto3D import Punto3D
from base import Base
from derivada import Derivada
from clase_A import A
from clase_B import B
from clase_C import C
from clase_D import D 
from pared import Pared
from ventana import Ventana
from casa import Casa

# Ejercicio 1
print("Ejercicio 1")

a = Punto2D(1, 2) 
a.traslacion(-1, -2) 

b = Punto2D(-3, 0) 
b.traslacion(5, -1) 

c = Punto3D(1,5,-3) 
c.traslacion(0, -2, 1) 

# Ejercicio 2
print("Ejercicio 2")

base = Base() 
derivada = Derivada() 
 
base.A() 
derivada.A() 
print() 
base.B() 
derivada.B() 
base.C() 
derivada.C() 
derivada = base 
derivada.C() 

# El mensaje que se muestra en consola es el siguiente:
# >>> a
# >>> a
# >>>
# >>> b
# >>> bb
# >>> bb
# >>> c
# >>> cc
# >>> c

# Ejercicio 3
print("Ejercicio 3")

d = D(1, 2, 3)
# La función isinstance nos dice si la clase A queda contenida en la variable d, y lo mismo con las clases B y C. Como eso es verdad,
# nos devuelve true.
print(isinstance(d, A), isinstance(d, B), isinstance(d, C))
print(d.a, d.b, d.c)

# Ejercicio 4
print("Ejercicio 4")

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

from pared_cortina import ParedCortina

# Definimos que la pared cortina de nuestra casa, que en esta casa es la pared sur
pared_cortina = ParedCortina("SUR", 10)
casa.paredes[2] = pared_cortina

print(casa.superficie_cristal())