"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:

valor_total = float(input("Digite o valor total investido na campanha (em R$): "))
numero_total_de_cliques = int(input("Digite o valor total de cliques obtidos: "))
custo_por_clique = valor_total / numero_total_de_cliques
print(f"O custo médio por clique é: {custo_por_clique} R$")
