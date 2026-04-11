#################################################################
## Tarefa 8
## Nome: Pedro ramos Cunha
## NUSP: 10892248
## Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação 
## Data de Submissão: 01/04/2026 23:15:58

t = int(input())


def exponenciacao(base, exp, mod):
    resultado = 1
    base = base % mod
    
    while exp > 0:
        # Se o expoente for ímpar, multiplicamos o resultado pela base atual
        if exp % 2 == 1:
            resultado = (resultado * base) % mod
            
        # Elevamos a base ao quadrado
        base = (base * base) % mod
        
        # Dividimos o expoente por 2 (usamos // para divisão inteira em Python)
        exp = exp // 2
        
    return resultado

for _ in range(t):
    car, c = map(int, input().split())       
    print(exponenciacao(car, c, 1000000007))
