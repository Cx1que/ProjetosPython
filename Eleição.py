contador_Eymael = 0
contador_kelmon = 0
contador_Daciolo = 0
voto_nulo = 0
voto_branco = 0

c = "s"
while c == "s":
    print("Digite 1 para EYMAEL, 2 para KELMON, 3 para DACIOLO, 4 para VOTAR EM BRANCO, 5 para VOTAR NULO:")
    voto = int(input("DIGITE SEU VOTO: "))

    if voto == 1:
        contador_Eymael += 1 

    elif voto == 2:
        contador_kelmon += 1

    elif voto == 3:
        contador_Daciolo += 1

    elif voto ==4:
        voto_nulo += 1

    else:
        voto_branco += 1
    c = input("DESEJA CONTINUAR? (s/n:")

    qtd_votos = contador_kelmon + contador_Eymael + contador_Daciolo + voto_nulo + voto_branco

porcent_Eymael = (contador_Eymael / qtd_votos) * 100
print("EYMAEL RECEBEU UM TOTAL DE {} VOTOS TOTALIZANDO {:.2f}% DOS VOTOS".format(contador_Eymael, porcent_Eymael))
porcent_Kelmon = (contador_kelmon / qtd_votos) * 100
print("PADRE KELMON RECEBEU UM TOTAL DE {} VOTOS TOTALIZANDO {:.2f}% DOS VOTOS".format(contador_kelmon, porcent_Kelmon))
porcent_Daciolo = (contador_Daciolo / qtd_votos) * 100
print("CABO DACIOLO RECEBEU UM TOTAL DE {} VOTOS TOTALIZANDO {:.2f}% DOS VOTOS".format(contador_Daciolo,porcent_Daciolo))
porcent_nulos = (voto_nulo / qtd_votos) * 100
print("OS VOTOS NULOS FORAM {} VOTOS TOTALIZANDO {:.2f}% DOS VOTOS".format(voto_nulo, porcent_nulos))
porcent_branco = (voto_branco / qtd_votos) * 100
print("OS VOTOS EM BRANCO FORAM {} VOTOS TOTALIZANDO {:.2f}% DOS VOTOS".format(voto_branco, porcent_branco))
