"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:

preco_final = lambda valor: valor - valor * 0.15

valor = float(input("Digite o valor do protudo: "))
valor_final = preco_final(valor)
print(f"O valor final do produto é: {valor_final}")