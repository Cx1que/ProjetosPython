nota1 = float(input("Dígite a primeira nota: "))
nota2 = float(input("Dígite a segunda nota: "))
media = (nota1 + nota2) / 2

if media > 10:
    print("DESCULPE, SUA MÉDIA DEVE ESTAR ENTRE 0 E 10")
elif media >= 9:
    print("Sua primeira nota foi {}, a segunda {}, sua média é {}, e seu conceito foi A".format(nota1, nota2, media))
    print("VOCÊ ESTÁ APROVADO, PARABENS!")
elif media >= 7.5 <= 8:
    print("Sua primeira nota foi {}, a segunda {}, sua média é {}, e seu conceito foi B".format(nota1, nota2, media))
    print("VOCÊ ESTÁ APROVADO, PARABENS!")
elif media >= 6 < 7.5:
    print("Sua primeira nota foi {}, a segunda {}, sua média é {}, e seu conceito foi C".format(nota1, nota2, media))
    print("VOCÊ ESTÁ APROVADO, PARABENS!")
elif media > 4 < 6:
    print("Sua primeira nota foi {}, a segunda {}, sua média é {}, e seu conceito foi D".format(nota1, nota2, media))
    print("SINTO MUITO, VOCÊ FOI REPROVADO!")
else:
    print("Sua primeira nota foi {}, a segunda {}, sua média é {}, e seu conceito foi E".format(nota1, nota2, media))
    print("SINTO MUITO, VOCÊ FOI REPROVADO!")
