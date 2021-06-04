import functools
k = int(input())
ps1 = int(input())
ps2 = int(input())

def obtenerMultiplos(de,hasta=0):
    multiplos = []
    i = 0
    while de*i <=hasta:
        multiplos.append(de*i)
        i = i+1
    return multiplos

print(obtenerMultiplos(ps1,k),obtenerMultiplos(ps2,k))
resultado1=functools.reduce(lambda a,b:int(a)+int(b),obtenerMultiplos(ps1,k))
resultado2=functools.reduce(lambda a,b:int(a)+int(b),obtenerMultiplos(ps2,k))
print(resultado1,resultado2)
resultado3=[value for value in obtenerMultiplos(ps1,k) if value in obtenerMultiplos(ps2,k)]
print(resultado3)
resultado3=functools.reduce(lambda a,b:int(a)+int(b),resultado3)
print(resultado1+resultado2-resultado3)