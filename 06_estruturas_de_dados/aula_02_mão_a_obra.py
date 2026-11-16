n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))
n4 = int(input("Digite um número: "))

matriz =  [
    [n1, n2],
    [n3, n4]
]

soma_total = 0

for linha in matriz:
    for n in linha:
        soma_total += n

print(soma_total)