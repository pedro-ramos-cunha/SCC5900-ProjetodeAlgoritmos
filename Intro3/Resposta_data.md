# Informações sobre tempo de execução da tarefa

|Tarefa 3                                          |
|:------|
|Curso: PPG-CCMC-ICMC-USP Mestrado em Ciência de Computação  |
|Nome: Pedro ramos Cunha                            |
|NUSP: 10892248 |
|Data de Submissão:  |

## Inputs e limites operacionais

Inputs são:
* "N" (número de entradas a seguir)
    * "query ID T" 
        * ID - Id da query
        * T - intervalo entre duas respostas consecutivas que o sistema deve 
fornecer (em segundos)
* K indica a quantidade as k primeiras execuções em ordem das querys informadas.

## Dados da Execução
|  Caso  |  Status | Tempo de CPU | Tam. de Memória Utilizado |     Mensagem     |
|:------:|:-------:|:------------:|:-------------------------:|:----------------:|
| Caso 1 | Correto |   0.0158 s   |           -1 Kb           | Resposta Correta |
| Caso 2 | Correto |   0.0162 s   |           -1 Kb           | Resposta Correta |
| Caso 3 | Correto |   0.3072 s   |           -1 Kb           | Resposta Correta |
| Caso 4 | Correto |   0.0219 s   |           -1 Kb           | Resposta Correta |
| Caso 5 | Correto |   0.0353 s   |           -1 Kb           | Resposta Correta |  



## Informações sobre a complexidade

 **Complexidade** 

 ![imagem_equacao](https://latex.codecogs.com/png.image?\bg{white}O_{(n,k)}=(n&plus;K)\times\log{n}&plus;s)

Onde:
* K é a quantidade das K primeiras queries executadas a ser mostrada
* N é queries informadas
* s é o custos de inicialização de variaveis e outros tempos esperados constantes.


