"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
def calcular_pontuacao_total(fase1, fase2, fase3):
    pontuação_total_equipe = fase1 + fase2 + fase3
    return pontuação_total_equipe

f1 = float(input("Digite a pontuação da fase 1: "))
f2 = float(input("Digite a pontuação da fase 2: "))
f3 = float(input("Digite a pontuação da fase 3: "))

pontuação_final = calcular_pontuacao_total(f1,f2,f3)
print(f"A pontuação final dessa equipe foi: {pontuação_final}")