# Informações sobre tempo de execução da tarefa

Informações acerca dos resultados obtidos

## Dados da Execução

| Caso 	| Status 	| Tempo de CPU 	| Tam. de Memória Utilizado 	| Mensagem 	|
|:---:	|:---:	|:---:	|:---:	|:---:	|
| Caso 1 	| Correto 	| 0.2091 s 	| -1 Kb 	| Resposta Correta 	|
| Caso 2 	| Correto 	| 0.0184 s 	| -1 Kb 	| Resposta Correta 	|
| Caso 3 	| Correto 	| 0.0598 s 	| -1 Kb 	| Resposta Correta 	|
| Caso 4 	| Correto 	| 0.4011 s 	| -1 Kb 	| Resposta Correta 	|

## Informações sobre a complexidade

**Tempo: O(n + s)**

* O loop de contagem percorre os n números do vetor → O(n)
* O loop de pares vai de 1 até s/2 → O(s)
* As operações de dicionário dentro dos loops são O(1)

Total: O(n + s)
Como os limites são n ≤ 10⁶ e s ≤ 10⁴, na prática o gargalo é o primeiro loop (leitura dos números), o que é ótimo.
Espaço: O(min(n, s))