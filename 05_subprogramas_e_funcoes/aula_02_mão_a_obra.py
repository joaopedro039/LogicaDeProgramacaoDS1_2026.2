calcular_acrescimo = lambda valor: valor + valor * 0.10
valor = float(input("Digite o valor: "))
resultado_valor_com_acresimo = calcular_acrescimo(valor)
print(f"Esse valor com um acresimo de 10% é: {resultado_valor_com_acresimo}")