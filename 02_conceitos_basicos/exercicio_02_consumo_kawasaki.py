"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:

distancia_total = float(input("Digite a distância total percorrida (em km): "))
total_de_combustivel = float(input("Digite o total de combustível gasto (em litros): "))
consumo_medio_motocicleta = distancia_total / total_de_combustivel
print(f"O consumo médio da motocicleta é: {consumo_medio_motocicleta:.2f} km/l")
