def tarifa_noturna(distancia):
    valor_final = 6 + 3.20 * distancia
    return valor_final

def tarifa_diurna(distancia):
    valor_final = 4 + 2.50 * distancia
    return valor_final

saldo = 0
while True:
    dis_corrida = float(input("Digite a distancia da corrida em km (valor de parada -1): "))
    if dis_corrida > 0:
        horario_corrida = input("Digite se corrida foi diurna ou noturna: ")
        horario_corrida = horario_corrida.lower()
        
        if horario_corrida == "diurna":
            resultado = tarifa_diurna(dis_corrida)
            print(f"O valor final da corrida foi: {resultado} R$")
            saldo += resultado
        elif horario_corrida == "noturna":
            resultado = tarifa_noturna(dis_corrida)
            print(f"O valor final da corrida foi: {resultado} R$")
            saldo += resultado
        else:
            print("Você digitou um horario invalido!")
            print("Digite de novo")
    if dis_corrida < 0:
        print("O truno acabou")
        print(f"o valor total ganho no dia foi: {saldo} R$")
        break