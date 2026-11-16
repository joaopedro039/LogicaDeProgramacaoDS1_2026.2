"""
EXERCÍCIO 01: Lista de Monitores
Disciplina: Lógica de Programação com Python

ENUNCIADO:
1. Crie uma lista com o primeiro monitor: "Ryan Mesquita Damasceno".
2. Adicione 2 novos monitores com .append().
3. Demonstre a mutabilidade alterando o nome na posição 0.
4. Imprima a lista final.
"""

# TODO: Desenvolva o algoritmo abaixo:

Monitores_lista = ["Ryan Mesquita Damasceno"]

n1 = input("Digite o nome do primeiro monitor para adicionar: ")
Monitores_lista.append(n1)
n2 = input("Digite o nome do segundo monitor para adicionar: ")
Monitores_lista.append(n2)
Monitores_lista[0] = "Carlos"
print(Monitores_lista)