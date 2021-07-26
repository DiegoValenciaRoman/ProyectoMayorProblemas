
def buscarPalabra(word,para):
    lenword = len(word)
    i = 0
    j=0
    #print("washoooo")
    while j < len(para):
        if word[i]==para[j]:
            i = i+1
        j = j+1
        if i==lenword:
            return j
    return -1
def mainProgram():
    cameo = input().lower().replace(" ","")
    frase = input().lower()
    k = 0
    matches=0
    encontrada = -1
    if len(cameo)>len(frase):
        return 0
    while k < len(frase):
        #print(cameo[0],frase[k])
        if cameo[0]==frase[k]:
            encontrada = buscarPalabra(cameo,frase[k:])
        else:
            encontrada=-1
        #print(encontrada,k,len(frase),frase[k:])
        if encontrada == -1:
            k=k+1
        else:
            matches = matches +1
            k = k+encontrada
    return matches
    
print(mainProgram())