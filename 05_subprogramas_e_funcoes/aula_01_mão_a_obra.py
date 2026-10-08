def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    print(f"A média dessas três notas é: {media}")

n1 = float(input("Digite um nota: "))
n2 = float(input("Digite um nota: "))
n3 = float(input("Digite um nota: "))
calcular_media(n1,n2,n3)