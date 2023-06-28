# Escrever um algoritmo que lê 5 valores para a,
# um de cada vez, e conta quantos destes valores são negativos, escrevendo esta informação.

numeros = []
negativos = []
for valor in range(1,6):
    valor = numeros.append(int(input("Informe um valor: ")))


for numero in numeros:
    if numero < 0:
        negativos.append(numero)

print("O total de números informados foram {}.".format(len(numeros)))
print("E deles, foram encontrados {} numeros negativos e são eles: {}".format(len(negativos), negativos))
