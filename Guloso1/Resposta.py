#################################################################
## Tarefa 4
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 13/03/2026 09:50:03

import heapq

while True:
    line1 = input()
    line1 = line1.split(' ')
    n = int(line1[0])
    m = int(line1[1])
    
    potes = []
    halturas = []
    halturas_validas = []
    if n == 0 and m == 0:
        break

    for x in range(n):
        heapq.heappush(potes, int(input()))
    
    for x in range(m):
        heapq.heappush(halturas, int(input()))

    while len(potes) > 0 and len(halturas) > 0:
        if potes[0] <= halturas[0]:
            halturas_validas.append(halturas[0])
            heapq.heappop(potes)
            heapq.heappop(halturas)
        else:
            heapq.heappop(halturas)

    soma_alturas = sum(halturas_validas)
    if soma_alturas == 0 or len(potes) > 0:
        print('no')
    else:
        print(soma_alturas)
    



