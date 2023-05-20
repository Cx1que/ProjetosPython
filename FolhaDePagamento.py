valorhora = float(input("Quanto você ganha por hora?"))
horasmes = float(input("Quantas horas você trabalha no mês?"))
salario_bruto = valorhora * horasmes
if salario_bruto < 900:
    fgts = salario_bruto * 0.11
    inss = salario_bruto * 0.10
    salario_liquido = salario_bruto - inss
    total_descontos = inss
    print("O seu salario liquido é: ",salario_liquido, "REAIS")
    print("Você ganha", fgts, "de FGTS")
    print("O valor total de descontos do seu salario é", total_descontos)
elif salario_bruto <= 1500:
    fgts = salario_bruto * 0.11
    inss = salario_bruto * 0.10
    imposto_renda = salario_bruto * 0.05
    salario_liquido = salario_bruto - inss - imposto_renda
    total_descontos = inss + imposto_renda
    print("O seu salario liquido é: ",salario_liquido, "REAIS")
    print("Você ganha",fgts, "de FGTS")
    print("Você paga",imposto_renda, "de imposto de renda")
    print("Você paga",inss, "de INSS")
    print("O valor total de descontos do seu salario é", total_descontos)
elif salario_bruto <= 2500:
    fgts = salario_bruto * 0.11
    inss = salario_bruto * 0.10
    imposto_renda = salario_bruto * 0.10
    salario_liquido = salario_bruto - inss - imposto_renda
    total_descontos = inss + imposto_renda
    print("O seu salario liquido é: ", salario_liquido, "REAIS")
    print("Você ganha", fgts, "de FGTS")
    print("Você paga", imposto_renda, "de imposto de renda")
    print("Você paga", inss, "de INSS")
    print("O valor total de descontos do seu salario é", total_descontos)
else:
    fgts = salario_bruto * 0.11
    inss = salario_bruto * 0.10
    imposto_renda = salario_bruto * 0.20
    salario_liquido = salario_bruto - inss - imposto_renda
    total_descontos = inss + imposto_renda
    print("O seu salario liquido é: ", salario_liquido, "REAIS")
    print("Você ganha", fgts, "de FGTS")
    print("Você paga", imposto_renda, "de imposto de renda")
    print("Você paga", inss, "de INSS")
    print("O valor total de descontos do seu salario é", total_descontos)
