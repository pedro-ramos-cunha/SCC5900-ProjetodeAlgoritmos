#################################################################
## Tarefa 5
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 13/03/2026 14:05:00

tests = int(input())

for i in range(tests):
    C,Z = map(int, input().split(' '))
    positions = input().split(' ')
    positions = [int(x) for x in positions if len(x)>0]
    comp_positions = [abs(x-C) for x in positions]
    best_case =  []
    worst_case = []

    for i in range(len(positions)):
        best_case.append(min(positions[i],comp_positions[i]))
        worst_case.append(max(positions[i],comp_positions[i]))

    print(max(best_case),max(worst_case))
