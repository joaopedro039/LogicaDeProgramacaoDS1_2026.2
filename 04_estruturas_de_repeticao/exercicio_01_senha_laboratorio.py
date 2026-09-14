"""
EXERCÍCIO 01: Senha Fixa do Laboratório
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Repita a leitura da senha até que o usuário digite a senha correta (2002).
Para cada tentativa incorreta, imprima "Senha Invalida".
Ao acertar, imprima "Acesso Permitido" e finalize o programa.
"""

# TODO: Desenvolva o algoritmo abaixo:
senha = "2002"
while True:
    senha_digita = input("Digite sua senha: ")
    if senha_digita == senha:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")