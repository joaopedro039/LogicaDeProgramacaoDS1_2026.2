"""
EXERCÍCIO 05: Acesso à Bilheteria do Parque
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba a idade do visitante (valor base do ingresso: R$ 100,00):
- Menor que 12 anos: "Infantil" (50% de desconto -> R$ 50,00)
- Maior ou igual a 60 anos: "Melhor Idade" (Gratuidade -> R$ 0,00)
- Demais idades: "Integral" (R$ 100,00)

Imprima o tipo de bilhete e o valor final a pagar.
"""

# TODO: Desenvolva o algoritmo abaixo:
idade_visitante = int(input("Digite a sua idade: "))
valor_bilhete = 100
if idade_visitante < 12:
    tipo_infantil = "infantil"
    valor_final_menor_12 = valor_bilhete - (valor_bilhete * 0.50)
    print(f"O tipo do seu bilhete é {tipo_infantil} e você tem 50% de desconto! valor final: {valor_final_menor_12}")
elif idade_visitante >= 60:
    tipo_melhor_idade = "melhor idade"
    valor_melhor_idade = valor_bilhete - (valor_bilhete * 1.00)
    print(f"O tipo do seu bilhete é {tipo_melhor_idade} e você tem 100% de desconto! valor final: {valor_melhor_idade}")
else:
    tipo_integral = "integral"
    valor_integral = valor_bilhete
    print(f"O tipo do seu bilhete é {tipo_integral} e você tem 0% de desconto! valor final: {valor_integral}")