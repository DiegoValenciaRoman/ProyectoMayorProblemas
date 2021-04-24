altoPiso = int(input('alto de un piso'))
anchoPiso = int(input('ancho de un piso'))
largoPiso = int(input('largo piso'))
altoPuerta = int(input('alto puerta'))
anchoPuerta = int(input('ancho puerta'))
altoVentana = int(input('alto ventana'))
radioRespiradero = int(input('radio respiradero'))

areaPuerta = altoPuerta*anchoPuerta
primerPiso = 2*((altoPiso*largoPiso) - areaPuerta) + 2*(anchoPiso*altoPiso)
areaVentana = altoVentana*altoVentana
areaRespiradero = 3.14*radioRespiradero*radioRespiradero

demasPisos = 2*((altoPiso*largoPiso) - areaVentana*4) + 2*((anchoPiso*altoPiso) - areaRespiradero)

techo = largoPiso*anchoPiso

total = techo + 3*demasPisos + primerPiso

#print("m2 ",total)
tarros = total/3
print("{:.2f}".format(tarros))


