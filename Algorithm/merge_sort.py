def merge_sort(vetor):
    """
        Merge Sort
    """
    tam = len(vetor)
    if tam > 1:
        meio = tam // 2
        
        esq_metade = merge_sort(vetor[:meio])
        dir_metade = merge_sort(vetor[meio:])

        i = 0
        j = 0
        k = 0

        esq_tam = len(esq_metade)
        dir_tam = len(dir_metade)
        
        while i < esq_tam and j < dir_tam:
            if esq_metade[i] < dir_metade[j]:
                vetor[k] = esq_metade[i]
                i += 1
            else:
                vetor[k] = dir_metade[j]
                j += 1
            k += 1

        while i < esq_tam:
            vetor[k] = esq_metade[i]
            i += 1
            k += 1

        while j < dir_tam:
            vetor[k] = dir_metade[j]
            j += 1
            k += 1

    return vetor