cameo = input().lower().replace(" ","")
frase = input().lower()
def buscarPalabra(word,para):
    lenword = len(word)
    i = 0
    j=0
    while j < len(para):
        if word[i]==para[j]:
            i = i+1
        j = j+1
        if i==lenword:
            return j
    return -1
k = 0
matches=0
encontrada = -1
while k < len(frase):
    if cameo[0]==frase[k]:
        encontrada = buscarPalabra(cameo,frase[k:])
    if encontrada == -1:
        k=k+1
    else:
        matches = matches +1
        k = k+encontrada
print(matches)
    
