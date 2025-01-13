def buscaMenor(arr):
    # Armazena o menor valor
    menor = arr[0]
    # Armazena o indice do menor valor
    menor_indice = 0
    
    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_indice = i
    return menor_indice

# Ordenacao em um array
def ordenacaoPorSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        # Encontra o menor elemento do array e adiciona ao novo array
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoPorSelecao([5, 3, 6, 2, 10])) # -> [2, 3, 5, 6, 10]