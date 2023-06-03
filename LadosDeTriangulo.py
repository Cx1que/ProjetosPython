lado1 = float(input("Dígite o primeiro lado: "))
lado2 = float(input("Dígite o segundo lado: "))
lado3 = float(input("Dígite o terceiro lado: "))
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Seu triângulo tem os três lados IGUAIS, portanto, é EQUILATERO!")
    elif lado1 == lado2 or lado2 == lado1 or lado1 == lado3:
        print("Seu triângulo tem dois lados IGUAIS, portanto, é ISÓCELESS")
    elif lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
        print("Sei triângulo não tem nenhum lado igual, portanto, é ESCALENO")
else:
    print("Os lados informados não formam um triângulo")
