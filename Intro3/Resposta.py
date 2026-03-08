#################################################################
## Tarefa 3
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 08/03/2026 19:22:06

import heapq

n = int(input())
heap = []

for q in range(0,n):
    query_data = input().split()
    ID = int(query_data[1])
    T = int(query_data[2])
    heapq.heappush(heap, (T, ID, T))  # (próximo_disparo, ID, intervalo)

K = int(input())

for timeline in range(0,K):
    tempo, ID, intervalo = heapq.heappop(heap)
    print(ID)
    heapq.heappush(heap, (tempo + intervalo, ID, intervalo))



        
