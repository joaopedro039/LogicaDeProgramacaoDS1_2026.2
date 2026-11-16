"""
EXERCÍCIO 04: Conjuntos (Set) de Disciplinas
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie 2 sets de estudantes (alunos_web e alunos_banco).
Calcule e imprima a Interseção (&) e a Diferença (-).
"""

# TODO: Desenvolva o algoritmo abaixo:
alunos_web = {"João","Pedro","Davi"}
alunos_banco = {"João","Pedro","Dantas"}

interseção = (alunos_web & alunos_banco)
diferença = (alunos_web - alunos_banco)
print(f"A interseção: {interseção}")
print(f"A diferença: {diferença}")