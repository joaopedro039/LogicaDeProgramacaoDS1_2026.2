n_pecas = int(input("Digite o número de peças que serão pesadas: "))
for i in range(n_pecas):
    peso = float(input("Digite o peso da peça: "))
    if i == 0:
        pesada = peso
        leve = peso
    else:
        if peso > pesada:
            pesada = peso
        if peso < leve:
            leve = peso 
print(f"A peça mais pesada pesa: {pesada}")
print(f"A peça mais leve pesa: {leve}")