"""
EXERCÍCIO 03: Pares entre Cinco Números
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite 5 números inteiros ao usuário.
Utilize uma estrutura de repetição e um contador para verificar quantos números pares
foram digitados. Ao final, imprima a quantidade total.
"""

# TODO: Desenvolva o algoritmo abaixo:
numeros_pares = 0
for num in range(5):
   numero = int(input("digite um número: "))
   if numero % 2 == 0:
      numeros_pares += 1
print(f"a quantidade de números pares é: {numeros_pares}")