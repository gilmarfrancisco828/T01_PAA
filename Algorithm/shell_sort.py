def shell_sort(vetor):
    """
        Shell Sort
    """
    # Marcin Ciura's gap sequence
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]

    for gap in gaps:
        i = gap
        while i < len(vetor):
            temp = vetor[i]
            j = i
            while j >= gap and vetor[j - gap] > temp:
                vetor[j] = vetor[j - gap]
                j -= gap
            vetor[j] = temp
            i += 1

    return vetor