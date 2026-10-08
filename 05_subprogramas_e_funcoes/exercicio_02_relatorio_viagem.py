"""
EXERCÍCIO 02: Modularizando Relatório de Viagem
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie duas funções:
1. `calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel)`
2. `calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao)`

No programa principal, leia os dados, execute as funções e mostre o custo total da viagem.
"""

# TODO: Desenvolva as funções e o programa principal abaixo:

def calcular_custo_transporte(distancia_km, consumo_kml, preco_combustivel):
    custo_total = distancia_km / consumo_kml * preco_combustivel
    return custo_total 
def calcular_custo_alimentacao(qtd_pessoas, dias, diaria_alimentacao):
    custo_total1 = qtd_pessoas * diaria_alimentacao * dias
    return custo_total1

distancia_km = float(input("Digite a distancia em km: "))
consumo_kml = float(input("Digite o consumo por um km rodado: "))
preco_combustivel = float(input("Digite o preço da gasolina: "))
qtd_pessoas = int(input("Digite a quantidade de pessoas: "))
dias = int(input("Digite a quantidade de dias: "))
diaria_alimentacao = float(input("Digite o preço da alimentação diaria: "))

resultado_custo_final = calcular_custo_transporte(distancia_km,consumo_kml,preco_combustivel) + calcular_custo_alimentacao(qtd_pessoas,dias,diaria_alimentacao)
print(f"O custo total dessa viagem foi: {resultado_custo_final}")