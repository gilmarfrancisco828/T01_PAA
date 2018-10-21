# import time
# import Algorithm
# qtd = [1000, 5000, 10000, 15000, 20000, 25000]
# tipos = ['aleatorios', 'crescentes', 'decrescentes']
# for q  in qtd:
#     print('Quantidade: ' + str(q))
#     for t in tipos:
#         print('Ordem: ' + t)
        
#         #lendo o arquivo
#         fileName = './Dados/' + str(q) + str(t) + '.txt' 
#         afile = open(fileName, "w")

#         #faz o slpit do arquivo no vetor
#         vetor = [int(line.rstrip('\n')) for line in afile]

#         #Guarda tempo inicial
#         inicio = time.time()
#         # executa a bateria de testes para o algoritmo
#         Algorithm.bubble_sort.bubble_sort(vetor)
#         total = time.time() - inicio
#         print('BubbleSort: ' + str(total))
    
#     print('\n')
