"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
x1 = int(input("Digite um número inteiro"))
y1 = int(input("Digite um número inteiro"))
y2 = y1 + 1
for num in range(x1,y2):
    if num % 5 == 2 or num % 5 == 3:
        print(num)