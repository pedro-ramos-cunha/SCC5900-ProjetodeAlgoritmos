#################################################################
## Tarefa 9
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 01/04/2026 00:42:48

t = int(input()) # Input number of test cases

for _ in range(t):
    N,K = map(int, input().split(' ')) # Input K and N

    motel_dist = list()
    for _ in range(N+1):
        motel_dist.append(int(input()))

    low = max(motel_dist)
    high = sum(motel_dist)
    resposta = high

    while low <= high:
        mid = (low + high) // 2
        
        dias_necessarios = 1
        soma_atual = 0
        for d in motel_dist:
            if soma_atual + d > mid:
                dias_necessarios += 1
                soma_atual = d
            else:
                soma_atual += d
        
        if dias_necessarios <= K + 1:
            resposta = mid
            high = mid - 1
        else:
            low = mid + 1

    print(resposta)


