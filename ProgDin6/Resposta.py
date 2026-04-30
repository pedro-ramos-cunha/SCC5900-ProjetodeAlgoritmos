#################################################################
## Tarefa 15
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 30/04/2026 17:09:26

def verificar_intercalacao(s1, s2, s3):
    n, m = len(s1), len(s2)
    
    # Se a soma dos tamanhos não bate, é impossível intercalar
    if n + m != len(s3):
        return False
    
    # Tabela DP inicializada com False
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 and j == 0:
                dp[i][j] = True
            # Verifica se o caractere de s3 veio de s1
            elif i > 0 and s1[i-1] == s3[i+j-1]:
                dp[i][j] = dp[i][j] or dp[i-1][j]
            # Verifica se o caractere de s3 veio de s2[cite: 2]
            if j > 0 and s2[j-1] == s3[i+j-1]:
                dp[i][j] = dp[i][j] or dp[i][j-1]
                
    return dp[n][m]

s1 = input()
s2 = input()
s3 = input()

print("True" if verificar_intercalacao(s1, s2, s3) else "False")