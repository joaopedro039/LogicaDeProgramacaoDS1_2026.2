def distancia_e_tipo_de_cliente(distancia, cliente):
    valor_final = distancia * 0.50
    if distancia > 100:
        valor_final += 15 
    cliente = cliente.lower()
    if cliente == "vip":
        valor_final = valor_final - 0.20 * valor_final
    return valor_final

distancia = float(input("Digite a distância em km: "))
cliente = input("Digite o tipo do cliente. Vip ou padrão: ")
resultado = distancia_e_tipo_de_cliente(distancia,cliente)
print(f"O valor final do frete foi: {resultado}")