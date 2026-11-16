def calcular_inss(valor_salario):
    valor_final = valor_salario - valor_salario * 0.12
    return valor_final

def valor_desconto(salario,porcentagem):
    valor_final = salario - salario * porcentagem
    return valor_final

while True:
    escolha = input("Digite se vc quer calcular o (inss) ou (salario). (valor parada fim): ")
    escolha = escolha.lower()
    if escolha == "inss":
        valor_salario = float(input("digite o valor do seu salario: "))
        resultado = calcular_inss(valor_salario)
        print(f"O valor do seu salario com o desconto do inss é: {resultado}")
    if escolha == "salário" or escolha == "salario":
        valor_salario = float(input("digite o valor do seu salario: "))
        porcentagem = float(input("Digite a porcentagem de desconto (ex 0.10): "))
        resultado = valor_desconto(valor_salario,porcentagem)
        print(f"O valor do salario com o desconto é: {resultado}")
    if escolha == "fim":
        print("O código acabou!")
        break