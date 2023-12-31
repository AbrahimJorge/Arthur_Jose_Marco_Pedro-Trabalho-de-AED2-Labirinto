"""
Auxilio do PDF do trabalho para a crição do Algoritimo 
https://colabweb.ufam.edu.br/pluginfile.php/113483/mod_resource/content/1/enunciado.pdf

Auxilio do PDF de alexandre gonçalves para criação do Algoritomo
https://www.inf.ufsc.br/~alexandre.goncalves.silva/courses/14s2/ine5633/trabalhos/t1/A%20%20%20Pathfinding%20para%20Iniciantes.pdf
"""

from GerarLab import *
      
#Função de heurística para o A*
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

#Função A*
def a_estrela(labirinto, inicio, fim):
    visitados = set()
    fila_prioridade = [(0, inicio, [])]

    while fila_prioridade:
        custo, atual, caminho = fila_prioridade.pop(0)

        if atual == fim:
            return caminho + [atual]

        if atual in visitados:
            continue

        visitados.add(atual)

        for proximo in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            novo = (atual[0] + proximo[0], atual[1] + proximo[1])
            if 0 <= novo[0] < len(labirinto) and 0 <= novo[1] < len(labirinto[0]) and labirinto[novo[1]][novo[0]] == 0:
                novo_custo = custo + 1
                novo_caminho = caminho + [atual]
                fila_prioridade.append((novo_custo + heuristica(fim, novo), novo, novo_caminho))

    return None