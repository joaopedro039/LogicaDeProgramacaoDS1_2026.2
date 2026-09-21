soma = 0
while True:
    numero_digitado = int(input("digite um número inteiro: "))
    if numero_digitado != 0:
        soma = soma + numero_digitado   
    else:
        print(f"(flag de parada) a soma é: {soma}")
        break