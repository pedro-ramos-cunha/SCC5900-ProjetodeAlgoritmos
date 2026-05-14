def jogo_das_avelas(nro_de_avelas):
    g = [0] * (nro_de_avelas + 1)
    
    for i in range(2, nro_de_avelas + 1):
        proximos_estados = set()
        if i >= 2: proximos_estados.add(g[i-2])
        if i >= 3: proximos_estados.add(g[i-3])
        if i >= 5: proximos_estados.add(g[i-5])
        mex = 0

        while mex in proximos_estados:
            mex += 1
        g[i] = mex
    return "Tico" if g[nro_de_avelas] > 0 else "Teco"

t = int(input())
for _ in range(t):
    nro_de_avelas = int(input())
    resultado = jogo_das_avelas(nro_de_avelas)
    print(resultado)