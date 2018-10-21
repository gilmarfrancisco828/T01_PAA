def quick_sort_pivp(vetor):
    """
        Quick Sort Iterativo com o primeiro elemento como pivo
    """
    esq = 0
    dir = len(vetor) - 1

    def particiona(vetor, esq, dir):
        """
        particiona method
        """
        # Pivo primeiro elemento da lista
        piv = vetor[esq]
        i = esq + 1
        j = dir

        while 1:
            while i <= j and vetor[i] <= piv:
                i += 1
            while j >= i and vetor[j] >= piv:
                j -= 1
            if j <= i:
                break
            vetor[i], vetor[j] = vetor[j], vetor[i]
        vetor[esq], vetor[j] = vetor[j], vetor[esq]
        return j

    pilha = []
    pilha.append((esq, dir))

    while pilha:
        pos = pilha.pop()
        dir, esq = pos[1], pos[0]
        piv = particiona(vetor, esq, dir)

        if piv-1 > esq:
            pilha.append((esq, piv-1))

        if piv+1 < dir:
            pilha.append((piv+1, dir))

    return vetor


def quick_sort_pivm(vetor):
    """
        Quick Sort Iterativo com o primeiro elemento como pivo
    """
    esq = 0
    dir = len(vetor) - 1

    def particiona(vetor, esq, dir):
        """
        particiona method
        """
        # Pivo elemento do meio
        piv = vetor[int((dir-esq)/2)]
        i = esq + 1
        j = dir

        while 1:
            while i <= j and vetor[i] <= piv:
                i += 1
            while j >= i and vetor[j] >= piv:
                j -= 1
            if j <= i:
                break
            vetor[i], vetor[j] = vetor[j], vetor[i]

        vetor[esq], vetor[j] = vetor[j], vetor[esq]
        return j

    pilha = []
    pilha.append((esq, dir))

    while pilha:
        pos = pilha.pop()
        dir, esq = pos[1], pos[0]
        piv = particiona(vetor, esq, dir)

        if piv-1 > esq:
            pilha.append((esq, piv-1))

        if piv+1 < dir:
            pilha.append((piv+1, dir))

    return vetor
