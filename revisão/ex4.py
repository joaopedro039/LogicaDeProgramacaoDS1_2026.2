ana = 0
joao = 0
maria = 0

while True:
    voto = int(input("Digite o número do seu cantido (valor da parada 0): "))
    if voto == 1:
        ana += 1
    elif voto == 2:
        joao += 1
    elif voto == 3:
        maria += 1
    elif voto == 0:
        print(f"A quantidade de votos do Ana foi: {ana}")
        print(f"A quantidade de votos do João foi: {joao}")
        print(f"A quantidade de votos do Maria foi: {maria}")
        if ana > joao and maria:
            print(f"O canditado vencedor é Ana!")
        elif joao > ana and maria:
            print(f"O canditado vencedor é joão!")
        else:
            print(f"O canditado vencedor é Maria!")
        break
    else:
        print("Número invalido digite outro") 