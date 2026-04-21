#################################################################
## Tarefa 11
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 12/04/2026 19:09:19


def maximizar_roubo(n, valores):
    if n == 0: return 0
    if n == 1: return valores[0]
    dp = [0] * n
    dp[0] = valores[0]
    dp[1] = max(valores[0], valores[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], valores[i] + dp[i-2])
    return dp[n-1]


n = int(input())
casas = []
casas = list(map(int, input().split()))
print(maximizar_roubo(n, casas)) # Saída: 12

