notas = []
for item in range(0, 10):
    nota = int(input("Informe a nota {}: ".format(item)))
    notas.append(nota)
print(notas)
media = sum(notas) / 10
print(media)

for index in range(len(notas)):   #o range esta lendo os valores de len (indices)
    valor = notas[index]            #recebendo o indice da lista
    print("A sua nota {} foi {}".format(index, valor))
