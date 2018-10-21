def selection_sort(vetor):
    """
        Selection Sort
    """

    tam = len(vetor)
    
    for i in range(tam):
        menor = i
        for k in range(i + 1, tam):
            if vetor[k] < vetor[menor]:
                menor = k
        vetor[menor], vetor[i] = (vetor[i], vetor[menor])
    return vetor
