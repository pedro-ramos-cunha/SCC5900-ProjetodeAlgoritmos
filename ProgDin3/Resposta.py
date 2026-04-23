#################################################################
## Tarefa 12
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 22/04/2026 22:46:38


def conjuntos_de_moedas(n, moedas, V):
    conjunto = [0] * (V + 1)
    conjunto[0] = 1
    
    for moeda in moedas:
        for i in range(moeda, V + 1):
            conjunto[i] += conjunto[i - moeda]
    return conjunto[V]

n_moedas = int(input())
lista_moedas =list(map(int,input().split(' '))) 
valor_alvo = int(input())

resultado = conjuntos_de_moedas(n_moedas, lista_moedas, valor_alvo)
print(resultado)  