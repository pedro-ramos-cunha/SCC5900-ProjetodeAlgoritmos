def encontrar_menor_caminho(n, trilhas):
    inf = float('inf')
    adj = [[] for _ in range(n)]

    for u, v, d in trilhas:
        u_idx, v_idx = u - 1, v - 1
        adj[u_idx].append((v_idx, d))
        adj[v_idx].append((u_idx, d))

    num_estados = 1 << n
    dp = [[inf] * n for _ in range(num_estados)]
    dp[1][0] = 0.
    for mask in range(1, num_estados):
        for u in range(n):
            dist_atual = dp[mask][u]
            if dist_atual == inf:
                continue
            
            for v, d in adj[u]:
                # Se o bit de v não está na mask
                if not (mask & (1 << v)):
                    proxima_mask = mask | (1 << v)
                    nova_dist = dist_atual + d
                    
                    if nova_dist < dp[proxima_mask][v]:
                        dp[proxima_mask][v] = nova_dist

    final_res = min(dp[num_estados - 1])
    return final_res if final_res != inf else -1

#Pega o valor de M e N 
trilha = []
n, m = map(int, input().split())

for _ in range(m):
    trilha.append(list(map(int,input().split(' '))))

print(encontrar_menor_caminho(n,trilha))