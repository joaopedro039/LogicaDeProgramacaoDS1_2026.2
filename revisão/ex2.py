temperatura = 0
quantidade = 0
temperatura_acima_35 = 0
while True:
    temperatura1 = float(input("DIgite a temperatura da estufa(valor parada 22): "))
    if temperatura1 != 22 and temperatura1 < 35:
        temperatura += temperatura1
        quantidade += 1
    elif temperatura1 > 35:
        temperatura += temperatura1
        quantidade += 1
        temperatura_acima_35 += 1 
    elif temperatura1 == 22:
        media = temperatura / quantidade
        print(f"A temperatura do período foi: {media}")
        print(f"A temperatura passou de 35 graus {temperatura_acima_35} vezes")
        break