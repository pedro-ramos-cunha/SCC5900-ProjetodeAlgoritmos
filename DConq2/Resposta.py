#################################################################
## Tarefa 7
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 22/03/2026 13:10:18

#################################################################
## Checa se a rainha está em uma posição válida 
## Não pode estar na mesma linha (condição 1)
## Ou na mesma coluna (condição 2)
## Ou na mesma diagonal (condição 3) -- Esta ultima é indicada pela diferencça igual entre x0-x1 e y0-y1)

def check_if_valid(queens, new_queen):
    for queen in queens:
        if queen[0] == new_queen[0] or queen[1] == new_queen[1] or abs(queen[0] - new_queen[0]) == abs(queen[1] - new_queen[1]):
            return False
    return True




def backtracking_queens(slots_burned,queens_placed ,index):
    cases_success = 0
    for i in range(8):
        if check_if_valid(queens_placed, (index, i)) and (index, i) not in slots_burned:
            if index == 7:
                return 1

            queens_placed.append((index, i))
            cases_success += backtracking_queens(slots_burned,queens_placed, index + 1)
            queens_placed.pop()
    return cases_success

slots_burned = list()
for i in range(8):
    linha_tabuleiro = list(input())
    for j in range(8):
        if linha_tabuleiro[j] == '*':
            slots_burned.append((i, j))

cases_success = backtracking_queens(slots_burned,[], 0)
print(cases_success)