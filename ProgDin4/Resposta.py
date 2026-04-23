#################################################################
## Tarefa 13
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 23/04/2026 13:34:39

def menor_caminho(m, n, matriz):
    matriz_de_caminhos = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                matriz_de_caminhos[i][j] = matriz[i][j]
            elif i == 0:
                matriz_de_caminhos[i][j] = matriz_de_caminhos[i][j-1] + matriz[i][j]
            elif j == 0:
                matriz_de_caminhos[i][j] = matriz_de_caminhos[i-1][j] + matriz[i][j]
            else:
                matriz_de_caminhos[i][j] = matriz[i][j] + min(matriz_de_caminhos[i-1][j], matriz_de_caminhos[i][j-1])
    return matriz_de_caminhos[m-1][n-1]


m,n =map(int,input().split(' '))
matriz = []
for i in range(m):
    matriz.append(list(map(int,input().split(' '))))

print(menor_caminho(m, n, matriz))
