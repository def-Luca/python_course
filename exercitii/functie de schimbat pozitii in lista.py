def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


lista = [4, 5, 6, 1, 12,3]


print(lista.index(4))

swapPositions(lista, 0, 1)

print(lista)