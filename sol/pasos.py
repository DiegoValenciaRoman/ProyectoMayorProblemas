entrada = input()
entrada = entrada.split(" ")
numero = int(entrada[0])
numero1 = int(entrada[1])
numero2 = int(entrada[2])

def pasos(numero):
    if(numero==1):
        return 0
    #mismo con operador ternario
    #return 1+pasos(numero/2) if numero%2==0 else 1+pasos(3*numero+1)
    if(numero%2==0):
        return 1+pasos(numero/2)
    return 1+pasos(3*numero+1)


numeros = [{"num":numero,"poder":pasos(numero)},
{"num":numero1,"poder":pasos(numero1)},
{"num":numero2,"poder":pasos(numero2)}]

listaOrdenada = sorted(numeros,key=lambda k:k['poder'],reverse=True)

print(str(listaOrdenada[0]['num'])+' '+str(listaOrdenada[1]['num'])+' '+str( listaOrdenada[2]['num']) )