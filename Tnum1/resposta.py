def divisores(nro):
    if nro < 1:
        return 0
    
    total_divisores = 1
    d = 2
    temp_n = nro
    while d * d <= temp_n:
        if temp_n % d == 0:
            cont = 0
            while temp_n % d == 0:
                cont += 1
                temp_n //= d
            total_divisores *= (cont + 1)
        d += 1
    if temp_n > 1:
        total_divisores *= 2
        
    return total_divisores

t = int(input())
for _ in range(t):
    n = int(input())
    print(divisores(n))