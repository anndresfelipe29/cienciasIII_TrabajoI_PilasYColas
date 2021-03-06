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

from cola import *

class Parqueadero:
    def __init__(self,nombre,codigo,placa):
        self.nombre = nombre
        self.codigo = codigo
        self.placa = placa

p = Cola()

cliente1 = Parqueadero('rodrigo','01','95RX')
cliente2 = Parqueadero('juan','02','14GH')
cliente3 = Parqueadero('pablo','03','95IO')
cliente4 = Parqueadero('juan','04','18IL')
cliente5 = Parqueadero('camilo','05','9ORX')
cliente6 = Parqueadero('enrique','06','14UH')

p.meter(cliente1)
p.meter(cliente2)
p.meter(cliente3)
p.meter(cliente4)
p.meter(cliente5)
p.meter(cliente6)

lista_busqueda = p.buscar('nombre','juan')
for i in range (len (lista_busqueda)):
        print (lista_busqueda[i].nombre,lista_busqueda[i].codigo,lista_busqueda[i].placa)