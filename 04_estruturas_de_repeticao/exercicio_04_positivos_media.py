"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
estritamente_positivos = 0
soma = 0
for n in range(6):
    num = int(input("digite um número: "))
    if num > 0:
        estritamente_positivos += 1
        soma += num
media = soma / estritamente_positivos
print(f"\nA quantidade de positivos é: {estritamente_positivos}")
print(f"\nA soma desses números é: {soma}")
print(f"\na média aritmética deles é: {media:.1f}")
    