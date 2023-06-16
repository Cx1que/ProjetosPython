numero = 0
impar = []
par = []
for numero in range(1, 11):
    numero = int(input("Informe um número: "))
    if numero % 2 != 0:
        impar.append(numero)
    else:
        par.append(numero)
        
print("A quantidade de números PARES que você informou é {}".format(len(par)))
print("A quantidade de números IMPARES que você informou é {}".format(len(impar)))
