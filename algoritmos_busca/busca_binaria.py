def busca_binaria(alist, alvo):
    min = 0
    max = len(alist)-1
    while True:
        chute = (max + min) / 2
        if alist[chute] == alvo:
            return True
        if max == min:
            return False

        if alist[chute] < alvo:
            min = chute + 1
        elif alist[chute] > alvo:
            max = chute - 1

