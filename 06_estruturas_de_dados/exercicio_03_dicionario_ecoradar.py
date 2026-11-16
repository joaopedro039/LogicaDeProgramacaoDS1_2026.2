"""
EXERCÍCIO 03: Dicionário da Equipe EcoRadar
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Estruture um dicionário com 3 membros (matrícula -> cargo).
Leia uma matrícula via terminal e exiba a função correspondente cadastrada.
"""

# TODO: Desenvolva o algoritmo abaixo:

membros = {"1":"Desenvolvedor","2":"Analista de Dados","3":"Gerente de Projetos"}
membro = input("Digite o numero da matrícula: ")

if membro == "1":
    print(f"Cargo: {membros['1']}")
elif membro == "2":
    print(f"Cargo: {membros['2']}")
elif membro == "3":
    print(f"Cargo: {membros['3']}")
elif membro != "1" and membro != "2" and membro != "3":
    print("Cargo não encontrada")