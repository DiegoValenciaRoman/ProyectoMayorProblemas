numero = input()
def obtenerParidad(numero):
    resultado = 0
    for number in numero:
        resultado = resultado + int(number)
    return 'PAR' if resultado%2==0 else 'IMPAR'


print(obtenerParidad(str(numero)))