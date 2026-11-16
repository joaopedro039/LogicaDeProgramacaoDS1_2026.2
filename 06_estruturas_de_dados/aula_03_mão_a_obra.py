marca = input("Digite a marca do carro: ")
modelo = input("Digite o modelo do carro: ")
ano = input("Digite o ano do carro: ")

veiculo = {"marca":marca,"modelo":modelo,"ano":ano}

for i in veiculo:
    veiculo.items()
    print(f"A/O {i} do carro é {veiculo[i]}")