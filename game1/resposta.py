




def jogo_moedas(moedas):
    N = 15
    memo_grundy = {}

    def sprague_grundy(x, y):
        if not (1 <= x <= N and 1 <= y <= N):
            return None
        
        if (x, y) in memo_grundy:
            return memo_grundy[(x, y)]

        movimentos = [
            (x - 2, y + 1),
            (x - 2, y - 1),
            (x + 1, y - 2),
            (x - 1, y - 2)
        ]
        
        proximos_grundy = set()
        for mx, my in movimentos:
            valor = sprague_grundy(mx, my)
            if valor is not None:
                proximos_grundy.add(valor)
        
        # Calcula o MEX (Minimum Excluded value)
        mex = 0
        while mex in proximos_grundy:
            mex += 1
            
        memo_grundy[(x, y)] = mex
        return mex

    # O jogo começa com o XOR sum das moedas
    xor_sum = 0
    for x, y in moedas:
        xor_sum ^= sprague_grundy(x, y)
    
    return "Primeiro" if xor_sum > 0 else "Segundo"



t = int(input())

for _ in range(t):
    k = int(input())
    moedas = []
    for _ in range(k):
        moedas.append(list(map(int, input().split())))
    
    resultado = jogo_moedas(moedas)
    print(resultado)