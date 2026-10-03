"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:
nivel_de_empolgacao = int(input("Digite seu nível de empolgação de 1 a 5: "))
letras_a = ""
for i in range(nivel_de_empolgacao):
    letras_a += "a"
print("feliz nat"+letras_a +"l!")