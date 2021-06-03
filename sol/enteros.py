import functools
suma = functools.reduce(lambda a,b:int(a)+int(b),list(str(input())))
print(str(suma)+' '+('par' if int(suma)%2==0 else 'impar'))