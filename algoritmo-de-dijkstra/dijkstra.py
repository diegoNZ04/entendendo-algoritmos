grafo = {}

grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}

infinito = float("inf")

custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

processados = []

def ache_no_custo_mais_baixo(custos):
	custo_mais_baixo = float("inf")
	vertice_custo_mais_baixo = None
	for vertice in custos: 
		custo = custos[vertice]
		if custo < custo_mais_baixo and vertice not in processados: 
			custo_mais_baixo = custo 
			vertice_custo_mais_baixo = vertice
	return vertice_custo_mais_baixo

vertice = ache_no_custo_mais_baixo(custos) 

while vertice is not None: 
	custo = custos[vertice]
	vizinhos = grafo[vertice]
	for v in vizinhos.keys(): 
		novo_custo = custo + vizinhos[v]
		if custos[v] > novo_custo: 
			custos[v] > novo_custo 
			pais[v] = vertice 
	processados.append(vertice) 
	vertice = ache_no_custo_mais_baixo(custos) 
 
 