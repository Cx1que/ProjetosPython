respostas= []

print("Responda as perguntas com < 0 > para NÃO ou < 1 > para SIM")

telefone = respostas.append(int(input("Telefonou para a vitima? ")))
local = respostas.append(int(input("Esteve no local do crime? ")))
morar = respostas.append(int(input("Mora perto da vitima? ")))
dever = respostas.append(int(input("Devia para a vitima?")))
trabalho = respostas.append(int(input("Já trabalhou com a vitima?  ")))

qtd = (sum(respostas))

if qtd < 2:
    print("Você não tem nada a ver com a cena do crime, pode se retirar.")
elif qtd == 2:
    print("Você se tornou SUSPEITO da investigação! ")
elif qtd == 3 or qtd == 4:
    print("Você é CUMPLICE! ")
else:
    print("Você é o ASSASINO da vítima!")
