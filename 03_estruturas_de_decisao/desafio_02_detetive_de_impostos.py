"""
DESAFIO 02: O DETETIVE DE IMPOSTOS E LICENÇAS
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O sistema municipal de tributos possui falhas lógicas na ordem das condições,
fazendo com que faixas superiores nunca sejam atingidas.

SUA MISSÃO:
1. Reestruture as condições lógicas if/elif/else.
2. Calcule corretamente a taxa comercial com base no faturamento.
"""

# CÓDIGO ORIGINAL COM FALHA LÓGICA:
# faturamento = float(input("Informe o faturamento anual: "))
# if faturamento > 0:
#     taxa = faturamento * 0.05
# elif faturamento > 50000:
#     taxa = faturamento * 0.10
# elif faturamento > 100000:
#     taxa = faturamento * 0.15

# TODO: Escreva aqui a versão corrigida:
faturamento = float(input("Infrome o faturamento anual: "))
if faturamento >= 0 and faturamento <= 50000:
    taxa = faturamento * 0.05
    print(f"Essa é a taxa sobre o valor de (5%) {faturamento} R$: {taxa}")
elif faturamento > 50000 and faturamento <= 100000:
    taxa = faturamento * 0.10
    print(f"Essa é a taxa sobre o valor de (10%) {faturamento} R$: {taxa}")
else:
    taxa = faturamento * 0.15
    print(f"Essa é a taxa sobre o valor de (15%) {faturamento} R$: {taxa}")