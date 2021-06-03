numero = int(input())
def pasos(numero):
    if(numero==1):
        return 0
    #mismo con operador ternario
    #return 1+pasos(numero/2) if numero%2==0 else 1+pasos(3*numero+1)
    if(numero%2==0):
        return 1+pasos(numero/2)
    return 1+pasos(3*numero+1)

print(pasos(numero))