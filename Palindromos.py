#-*- coding: utf-8 -*-
#SanMarE11
print("Ingresa la primera palabra")
f1 = list(input().upper())
for i in range(1, len(f1)):
    if(f1[i-1] == f1[len(f1)-i]):
        valido = True
    else:
        valido = False
        break
if(valido):
    print("La palabra {} es palindroma".format("".join(f1)))
else:
    print("No es palindromo")
