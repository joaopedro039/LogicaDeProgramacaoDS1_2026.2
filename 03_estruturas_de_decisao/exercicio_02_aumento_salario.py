"""
EXERCÍCIO 02: Aumento de Salário Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de um colaborador da escola e aplique o percentual de reajuste:
- 0.00 a 400.00: 15%
- 400.01 a 800.00: 12%
- 800.01 a 1200.00: 10%
- 1200.01 a 2000.00: 7%
- Acima de 2000.00: 4%

Imprima: novo salário, valor do reajuste ganho e percentual aplicado.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario_colaborador = float(input("Digite seu salário: "))
if salario_colaborador < 400.01:
   novo_salario_15 = salario_colaborador + (salario_colaborador * 0.15)
   valor_reajuste_15 = (salario_colaborador * 0.15)
   taxa_15 = "15%"
   print(f"Novo salário: {novo_salario_15}, valor do reajuste ganho: {valor_reajuste_15} e percentual aplicado: {taxa_15}")
elif salario_colaborador >= 400.01 and salario_colaborador <= 800:
    novo_salario_12 = salario_colaborador + (salario_colaborador * 0.12)
    valor_reajuste_12 = (salario_colaborador * 0.12)
    taxa_12 = "12%"
    print(f"Novo salário: {novo_salario_12}, valor do reajuste ganho: {valor_reajuste_12} e percentual aplicado: {taxa_12}")
elif salario_colaborador >= 800.01 and salario_colaborador <= 1200:
    novo_salario_10 = salario_colaborador + (salario_colaborador * 0.10)
    valor_reajuste_10 = (salario_colaborador * 0.10)
    taxa_10 = "10%"
    print(f"Novo salário: {novo_salario_10}, valor do reajuste ganho: {valor_reajuste_10} e percentual aplicado: {taxa_10}")
elif salario_colaborador >= 1200.01 and salario_colaborador <= 2000:
    novo_salario_7 = salario_colaborador + (salario_colaborador * 0.07)
    valor_reajuste_7 = (salario_colaborador * 0.07)
    taxa_7 = "7%"
    print(f"Novo salário: {novo_salario_7}, valor do reajuste ganho: {valor_reajuste_7} e percentual aplicado: {taxa_7}")
else:
    novo_salario_4 = salario_colaborador + (salario_colaborador * 0.04)
    valor_reajuste_4 = (salario_colaborador * 0.04)
    taxa_4 = "4%"
    print(f"Novo salário: {novo_salario_4}, valor do reajuste ganho: {valor_reajuste_4} e percentual aplicado: {taxa_4}")

    