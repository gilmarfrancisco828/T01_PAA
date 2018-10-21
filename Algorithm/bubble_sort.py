def bubble_sort_m(vetor):
    """
        Bubble Sort com melhoramento
    """
    tam = len(vetor)
    for i in range(tam):
        troca = False
        for j in range(tam-1):
            if vetor[j] > vetor[j+1]:
                troca = True
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
        if not troca: break
    return vetor

def bubble_sort(vetor):
    """
        Bubble Sort sem melhoramento
    """
    tam = len(vetor)
    for i in range(tam):
        for j in range(tam-1):
            if vetor[j] > vetor[j+1]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return vetor
