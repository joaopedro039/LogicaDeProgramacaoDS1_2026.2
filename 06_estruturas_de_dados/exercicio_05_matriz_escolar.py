"""
EXERCÍCIO 05: Matriz Bidimensional Escolar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma matriz com 3 alunos [nome, nota1, nota2].
Percorra a matriz, calcule a média de cada um e exiba:
"Aluno: [Nome] | Média: [Média] | Situação: [Aprovado / Prova Final]"
(Critério: Média >= 6.0 aprovado).
"""

# TODO: Desenvolva o algoritmo abaixo:
nome1 = input("Digite o nome do aluno: ")
n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

nome2 = input("Digite o nome do aluno: ")
n1_2 = float(input("Digite sua primeira nota: "))
n2_2 = float(input("Digite sua segunda nota: "))

nome3 = input("Digite o nome do aluno: ")
n1_3 = float(input("Digite sua primeira nota: "))
n2_3 = float(input("Digite sua segunda nota: "))

alunos = [[nome1,n1,n2],[nome2,n1_2,n2_2],[nome3,n1_3,n2_3]]

media1 = 0
media2 = 0
media3 = 0
nome = ""

for linha in alunos:
    media = (linha[1] + linha[2]) / 2
    nome = linha[0]
    if nome == nome1:
        media1 += media
    elif nome == nome2:
        media2 += media
    elif nome == nome3:
        media3 += media

if media1 >= 6:
    print(f"Aluno: {nome1} | média: {media1} | Situação: aprovado")
else:
    print(f"Aluno: {nome1} | média: {media1} | Situação: Prova Final")
if media2 >= 6:
    print(f"Aluno: {nome2} | média: {media2} | Situação: aprovado")
else:
    print(f"Aluno: {nome2} | média: {media2} | Situação: Prova Final")
if media3 >= 6:
    print(f"Aluno: {nome3} | média: {media3} | Situação: aprovado")
else:
    print(f"Aluno: {nome3} | média: {media3} | Situação: Prova Final")