def heap_sort(vetor):
    """
        Heap Sort
    """
    def heapify(vetor, i, heap_tam):
        maior = i
        esq_i = 2 * i + 1
        dir_i = 2 * i + 2
        if esq_i < heap_tam and vetor[esq_i] > vetor[maior]:
            maior = esq_i

        if dir_i < heap_tam and vetor[dir_i] > vetor[maior]:
            maior = dir_i

        if maior != i:
            vetor[maior], vetor[i] = vetor[i], vetor[maior]
            heapify(vetor, maior, heap_tam)

    n = len(vetor)
    
    for i in range(n // 2 - 1, -1, -1):
        heapify(vetor, i, n)
    
    for i in range(n - 1, 0, -1):
        vetor[0], vetor[i] = vetor[i], vetor[0]
        heapify(vetor, 0, i)

    return vetor
