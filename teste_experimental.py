import time, inspect
import Algorithm as alg
qtd = [1000, 5000, 10000, 15000, 20000, 25000, 50000, 100000]
tipos = ['aleatorios', 'crescentes', 'decrescentes']
funcoes = inspect.getmembers(alg, inspect.isfunction)
resultados = []

for t  in tipos:
    print('Ordem: ' + t[:-1])
    resultados = []
    for q in qtd:
        # print('Quantidade: ' + str(q))
        #lendo o arquivo de dados
        fileName = './Dados/dados_' + str(t) + '_' + str(q) + '.txt' 
        afile = open(fileName, "r")

        #faz o slpit do arquivo no vetor
        vetor = [int(x) for x in afile.read().split()]
        for f in funcoes:
            # Faz uma copia do vetor, pois python passa por referencia
            vetor_copia = vetor[:]
            #Guarda tempo inicial
            inicio = time.time()
            # executa a bateria de testes para o algoritmo
            f[1](vetor_copia)
            total = time.time() - inicio
            print("\t%-16s"%f[1].__name__ + ": \t %.25f"%total)
            resultados.append(str(q) + " " + f[1].__name__ + " %.25f"%total + "\n");
        # fechando o arquivo e efetivando as modificacoes
        afile.close()
    # Abre o arquivo que vai conter os resultados dos testes
    fileName = './Resultados/results_' + str(t) + '.txt'
    afile = open(fileName, "w")
    
    # Escreve o resultado dos testes no arquivo 
    for line in resultados:
        afile.write(line)
    # Fecha e efetiva o salvamento dos dados
    afile.close()

    print('\n')
