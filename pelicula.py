#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      anderson
#
# Created:     15/08/2017
# Copyright:   (c) anderson 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from pila import *

class Pelicula:
    def __init__(self,nombre,fecha,director):
        self.nombre = nombre
        self.fecha = fecha
        self.director = director

p = Pila()

pel = Pelicula('pel','1980','Pablo')
pel2= Pelicula('pp','1800','Pablo')

p.meter(pel)
p.meter(pel2)
lista_busqueda = p.buscar('director','Pablo')
for i in range (len (lista_busqueda)):
        print (lista_busqueda[i].nombre,lista_busqueda[i].fecha,lista_busqueda[i].director)