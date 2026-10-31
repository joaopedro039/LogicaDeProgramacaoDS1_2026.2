def  indice_de_Massa_corporal(peso,altura):
    imc = peso / altura**2
    return imc

peso_normal = 0

while True:
    nome = input("Digite o nome do atleta: ")
    nome = nome.lower()
    if nome != "fim":
        peso = float(input("Digite o peso do atleta em kg: "))
        altura = float(input("Digite a altura do atleta em metros: "))
        resultado = indice_de_Massa_corporal(peso,altura)

        if resultado < 18.5:
            print("Abaixo do peso")
        elif resultado >= 18.5 and resultado <= 24.9:
            print("Peso normal")
            peso_normal += 1 
        elif resultado >= 25 and resultado <= 29.9:
            print("Sobrepeso")
        elif resultado >= 30 and resultado <= 34.9:
            print("Obesidade grau 1")
        elif resultado >= 35 and resultado <= 39.9:
            print("Obesidade grau 2")
        elif resultado >= 40:
            print("Obesidade grau 3 (mórbida)")
            
    if nome == "fim":
        print(F"A quantidade de atletas com peso normal é: {peso_normal}")
        break