def insertion_sort(vetor):
    """
        Insertion Sort
    """
    for i in range(1, len(vetor)):
        while 0 < i and vetor[i] < vetor[i - 1]:
            vetor[i], vetor[
                i - 1] = vetor[i - 1], vetor[i]
            i -= 1

    return vetor