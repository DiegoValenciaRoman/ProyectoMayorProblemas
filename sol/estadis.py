import functools
cantidad = int(input("cantidad"))
respuesta = {
    "mejor":-1,
    "peor":8,
    "frecmejor":0,
    "frecpeor":0
}
notas = []
def promedio(lista):
    return functools.reduce(lambda a,b:a+b,lista)/len(lista)
def mejorNota(lista):
    frec = 1
    mejor = -1
    for x in lista:
        if x>mejor:
            mejor =x
            frec= 1
        elif x==mejor:
            frec = frec+1
    return {"mejor":str(mejor),"frec":str(frec)}
for x in range(cantidad):
    notas.append(float(input()))

print("{0:.1f}".format(promedio(notas)) + ' ' +mejorNota(notas)["mejor"]+' '+mejorNota(notas)["frec"] )


