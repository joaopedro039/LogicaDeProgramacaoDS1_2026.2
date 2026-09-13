"""
EXERCÍCIO 03: Fórmula de Bhaskara
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 3 valores de ponto flutuante (A, B e C) de uma equação do 2º grau.
- Se A for 0 ou delta for negativo, imprima "Impossivel calcular".
- Caso contrário, calcule e mostre as duas raízes (R1 e R2) formatadas com 5 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:
import math
a = float(input("Digite o ponto A: "))
b = float(input("Digite o ponto B: "))
c = float(input("Digite o ponto C: "))
delta = b**2-4*a*c
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    r1 = (-b+(math.sqrt(delta))) / (2*a)
    r2 = (-b-(math.sqrt(delta))) / (2*a)
    print(f"raiz 1 é igual á: {r1:.5f}")
    print(f"raiz 2 é igual á: {r2:.5f}")