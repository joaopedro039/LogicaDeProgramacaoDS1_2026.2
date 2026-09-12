"""
EXERCÍCIO 01: Imposto de Renda de Lisarb
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia o salário de uma pessoa em Rombus (R$).
- Até R$ 2000.00: Isento
- De R$ 2000.01 até R$ 3000.00: 8% sobre o excedente de R$ 2000.00
- De R$ 3000.01 até R$ 4500.00: 18% sobre o excedente de R$ 3000.00 + 8% da faixa anterior
- Acima de R$ 4500.00: 28% sobre o que ultrapassar R$ 4500.00 + impostos anteriores

Imprima "Isento" ou o valor total do imposto formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
salario_pessoa = float(input("Digite o seu sálario: "))
if salario_pessoa <= 2000:
    print("O seu salário não tem nenhuma taxa.")
elif salario_pessoa >= 2000.01 and salario_pessoa <= 3000:
    imposto_final_ate_3000 =(salario_pessoa * 0.08)
    print(f"A taxa sobre o seu salário é de (8%), imposto final: {imposto_final_ate_3000:.2f}")
elif salario_pessoa >= 3000.01 and salario_pessoa <= 4500:
    imposto_final_ate_4500 =(salario_pessoa * 0.08 + salario_pessoa * 0.18)
    print(f"A taxa sobre o seu salário é de (18% + 8%), imposto final: {imposto_final_ate_4500:.2f}")
else:
    imposto_final_acima_de_4500 = (salario_pessoa * 0.08 + salario_pessoa * 0.18 + salario_pessoa * 0.28)
    print(f"A taxa sobre o seu salário é de (28% + 18% + 8%), imposto final: {imposto_final_acima_de_4500:.2f}")