
n = int(input())
mapeo = {0:"a",1:"b",3:"c"}
a=0
b=0
c=0
for x in range(n):
    x= input().split()
    a = a+ int(x[0])
    b = b+ int(x[1])
    c = c+ int(x[2])
lista = [a,b,c]
mayor = max(lista)
menor = min(lista)
mayorNum = mapeo[lista.index(mayor)]
menorNum = mapeo[lista.index(menor)]
print("mayor venta "+mayorNum+"="+str(mayor)+", menor venta "+menorNum+"="+str(menor))


