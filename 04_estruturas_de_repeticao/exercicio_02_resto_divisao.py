"""
EXERCÍCIO 02: Resto da Divisão por 5
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia dois valores inteiros X e Y.
Utilize o laço for para imprimir todos os inteiros entre X e Y (em ordem crescente)
cujo resto da divisão por 5 seja igual a 2 ou igual a 3.
"""

# TODO: Desenvolva o algoritmo abaixo:
x = int(input("Digite um valor inteiro: "))
y = int(input("Digite outro valor inteiro: "))
x2 = x + 1
y2 = y + 1
if y > x:
    print("números em ordem crescente:")
    for numeros_em_ordem_crescente in range(x2,y):
        print(numeros_em_ordem_crescente)
else:
    print("números em ordem crescente:")
    for numeros_em_ordem_crescente in range(y2,x):
        print(numeros_em_ordem_crescente)