gabarito = ["A", "B", "C", "D", "E", "E", "D", "C", "B", "A"]
acertosAluno = []  # lista para contar os acertos de cada aluno
c = "S"
while c == "S":
    respostasAluno = [] #lista que contém as respostas gerais de todos alunos
    acertos = 0
    for i in range(10):
        respostas = input("Qual a resposta da questao {}? : ".format(i+1)).upper()
        respostasAluno.append(respostas) # adiciona as respostas em respostasAluno
        # comparar com o gabarito
        if respostas == gabarito[i]:   # compara as respostas com o gabarito
            acertos += 1
    acertosAluno.append(acertos) # adiciona apenas as respostas corretas na lista acertosAluno
        # outro aluno irá usar o sistema?
    c = input("Outro aluno deseja informar suas notas <S> para continuar: ").upper()

# maior e menor acerto
maiorAcerto = max(acertosAluno)
menorAcerto = min(acertosAluno)

# total de alunos que usaram o sistema
totalAlunos = len(acertosAluno)  # o total de alunos é contado a partir de cada 10 notas na lista acertosAluno

#printar tudo
print("====/==============/===============/====")
print("Maior acerto: ", maiorAcerto)
print("Menor acerto: ", menorAcerto)
print("Total de alunos:", totalAlunos)
print("====/==============/===============/====")
