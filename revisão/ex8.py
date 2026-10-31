valor_final = 0
while True:
    preco = float(input("Digite o preço do produto (valor de parada -1): "))
    if preco > 0:
        quantidade = int(input("Digite a quantidade de unidades que você comprou: "))
        preco_total = preco * quantidade
        valor_final += preco_total
    if preco < 0:
        if valor_final > 200: 
            valor_bruto = valor_final
            desconto = valor_final * 0.10
            valor_final -= desconto
        else:
            desconto = 0
            valor_bruto = valor_final
            valor_final = valor_final
        break
print(f"Valor Bruto: R${valor_bruto}")
print(f"Desconto (10%): R${desconto}")
print(f"Valor Final: R${valor_final}")