"""
DESAFIO 04: REFATORAÇÃO INVESTIGATIVA
Disciplina: Lógica de Programação com Python

RELATÓRIO DA INVESTIGAÇÃO:
O código monolítico repete cálculos de desconto e impostos várias vezes.

SUA MISSÃO:
1. Crie uma função calcular_preco_final(preco_base, taxa_desc, taxa_imp) com return.
2. Crie um procedimento exibir_relatorio_item(numero_item, preco_final) com print.
3. Teste suas funções refatoradas.
"""

# TODO: Desenvolva as funções modulares abaixo:

def calcular_preco_final(preco_base, taxa_desc, taxa_imp):
    preco_final = preco_base - (preco_base * taxa_desc) + (preco_base * taxa_imp)
    return preco_final
def exibir_relatorio_item(numero_item):
    relatorio = (f"O número do item é : {numero_item} é o seu preço final é: {preco_final_1}")
    return relatorio
preco_base = float(input("Digite o preço base: "))
taxa_desc = float(input("Digite a taxa em decimal do desconto (10% = 0.10): "))
taxa_imp = float(input("Digite a taxa em decimal do imposto (10% = 0.10): "))
numero_item = int(input("Digite o número do item: "))

preco_final_1 = calcular_preco_final(preco_base,taxa_desc,taxa_imp)
relatorio_item_1 = exibir_relatorio_item(numero_item)
print(relatorio_item_1)