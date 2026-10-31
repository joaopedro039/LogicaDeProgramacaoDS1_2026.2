def calcular_juros (valor_inicial,taxa_de_juros_mensal,meses):
    saldo = valor_inicial
    meses += 1
    for mes in range(1,meses):
        montante = saldo * (taxa_de_juros_mensal + 1)
        saldo = montante
        print(f"Mês {mes}: {montante:.2f}")

valor_inicial = float(input("Digite o valor inicial: "))
taxa_de_juros_mensal = float(input("Digite a taxa de juros: "))
meses = int(input("Digite a quantidade de meses: "))
calcular_juros(valor_inicial,taxa_de_juros_mensal,meses)
