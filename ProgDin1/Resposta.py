#################################################################
## Tarefa 10
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 12/04/2026 18:49:23


def custo_minimo_escalada(n, custos):
    dp = [0] * (n + 1)
    
    dp[0] = custos[0]
    dp[1] = custos[1]
    
    for i in range(2, n):
        dp[i] = custos[i] + min(dp[i-1], dp[i-2])
    
    dp[n] = min(dp[n-1], dp[n-2])
    return dp[n]

# Exemplo do enunciado
n = int(input())
custos = []
custos = list(map(int, input().split()))
print(custo_minimo_escalada(n, custos)) 