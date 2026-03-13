#################################################################
## Tarefa 4
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 08/03/2026 00:28:50

import heapq

while True:
    line1 = input()
    line1 = line1.split(' ')
    n = int(line1[0])
    m = int(line1[1])
    
    potes = []
    halturas = []
    if n == 0 and m == 0:
        break

    for x in range(n):
        heapq.heappush(potes, int(input()))
    
    for x in range(m):
        heapq.heappush(halturas, int(input()))

    
    



