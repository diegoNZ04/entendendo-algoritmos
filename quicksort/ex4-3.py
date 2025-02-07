def maior(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_maior = maior(lista[1:])
    return lista[0] if lista[0] > sub_maior else sub_maior

nLista = [3, 6, 7]

print(maior(nLista))