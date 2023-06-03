# Válidador de CPF somente com o uso de IF e ELSE

cpf = str(input("Digite seu CPF: "))
    # Verifificando a quantidade de dígitos do CPF
if len(cpf) != 11:
    print("Seu CPF é INVALIDO")
    # Calculando o primeiro dígito do CPF
else:
    soma1 = int(cpf[0]) * 10 + int(cpf[1]) * 9 + int(cpf[2]) * 8 + int(cpf[3]) * 7 + int(cpf[4]) * 6 + int(cpf[5]) * 5 + int(cpf[6]) * 4 + int(cpf[7]) * 3 + int(cpf[8]) *2
    resto1 =soma1 % 11

if resto1 < 2:

    digito1 = 0
else:
    digito1 = 11 - resto1

    # Calculando o segundo dígito do CPF
soma2 = int(cpf[0]) * 11 + int(cpf[1]) * 10 + int(cpf[2]) * 9 + int(cpf[3]) * 8 + int(cpf[4]) * 7 + int(cpf[5]) * 6 + int(cpf[6]) * 5 + int(cpf[7]) * 4 + int(cpf[8]) *3 + digito1 * 2
resto2 = soma2 % 11

if resto2 < 2:

    digito2 = 0
else:
    digito2 = 11 - resto2

# Verificando se o CPF é VÁLIDO
if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
    print("Seu CPF é VÁLIDO")
else:
    print("CPF INVÁLIDO")
