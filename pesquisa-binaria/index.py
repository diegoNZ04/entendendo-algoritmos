def pesquisa_binaria(lista, item):
    # baixo e alto acompanham a parte da lista que você está procurando
    baixo = 0
    alto = len(lista) - 1
    
    # enquanto não conseguiu chegar a um unico elemento...
    while baixo <= alto:
        # verifica o elemento central
        meio = (baixo + alto)/2
        chute = lista[int(meio)]
        # acha o item
        if chute == item:
            return int(meio)
        # o chute foi muito alto
        if chute > item:
            alto  = meio - 1
        # o chute foi muito baixo
        else:
            baixo = meio + 1
    # O número não existe
    return None

# declaracao lista
minha_lista = [1, 2, 3, 4, 5, 6, 7, 8]

# chamada de funcão
print(pesquisa_binaria(minha_lista, 3)) # => 2
print(pesquisa_binaria(minha_lista, -1)) # => None

