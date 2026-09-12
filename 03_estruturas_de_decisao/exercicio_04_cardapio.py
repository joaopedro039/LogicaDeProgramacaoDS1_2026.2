"""
EXERCÍCIO 04: Cardápio da Lanchonete
Disciplina: Lógica de Programação com Python

TABELA:
1 - Cachorro Quente: R$ 4.00
2 - X-Salada: R$ 4.50
3 - X-Bacon: R$ 5.00
4 - Torrada Simples: R$ 2.00
5 - Refrigerante: R$ 1.50

ENUNCIADO:
Leia o código do item e a quantidade consumida.
Calcule e mostre o total a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
#cachorro quente = 1
#X-salada = 2
#X-bacon = 3
#Torrada Simples = 4
#Refrigerante = 5
item_consumido = input("Digite o código do item: ")
quantidade_consumida = int(input("Digite a quantidade consumida: "))
if item_consumido == "1":
    total_pagar_cachorro_quente = 4.00 * quantidade_consumida
    print(f"O valor total a pagar por esses/esse cachorros quentes é: {total_pagar_cachorro_quente}")
if item_consumido == "2":
    total_pagar_x_salada = 4.50 * quantidade_consumida
    print(f"O valor total a pagar por esses/esse X-saladas é: {total_pagar_x_salada}")
if item_consumido == "3":
    total_pagar_X_bacon = 5.00 * quantidade_consumida
    print(f"O valor total a pagar por esses/esse X-bacon é: {total_pagar_X_bacon}")
if item_consumido == "4":
    total_pagar_torrada_simples = 2.00 * quantidade_consumida
    print(f"O valor total a pagar por essas/essa torrada simples é: {total_pagar_torrada_simples}")
if item_consumido == "5":
    total_pagar_refrigerante = 1.50 * quantidade_consumida
    print(f"O valor total a pagar por esses/esse refrigerante é: {total_pagar_refrigerante}")