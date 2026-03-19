#################################################################
## Tarefa 6
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 19/03/2026 00:05:21


def backtracking(peso_sacola1,peso_sacola2, peso_mangas):
    if len(peso_mangas) == 0:
        return abs(peso_sacola1 - peso_sacola2)
    else:
        manga = peso_mangas[0]
        restante = peso_mangas[1:]
        return min(backtracking(peso_sacola1 + manga, peso_sacola2, restante), backtracking(peso_sacola1, peso_sacola2 + manga, restante))

nro_mangas = int(input())
peso_mangas = list(map(int, input().split()))

# Obrigado pausa para ir à academia 
# Tive o insight de fazer recursivamente, enquanto voltava
# Na ida tinha visto a imagem do link https://www.wscubetech.com/resources/dsa/backtracking-algorithm
# (primeira imagem que aparece quando procura "backtracking algorithm") no google

print(backtracking(0,0,peso_mangas))
