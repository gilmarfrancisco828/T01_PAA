import matplotlib.pyplot as plt
import numpy as np
import inspect
import Algorithm as alg
qtd = [1000, 5000, 10000, 15000, 20000, 25000, 50000, 100000]
tipos = ['aleatorios', 'crescentes', 'decrescentes']
funcoes = inspect.getmembers(alg, inspect.isfunction)
qplot = 0
for i in range(0, len(funcoes)):
    plt.figure(qplot)
    for t in tipos:
        fileName = './Resultados/results_' + str(t) + '.txt'
        afile = open(fileName, "r")
        vetor = [x for x in afile.read().split("\n")]
        algName = vetor[i].split(" ")[1]
        vetorplot = []
        for j in range(0, len(funcoes)-1):
            # print(vetor[i+j*len(funcoes)].split(" "))
            yval = float(vetor[i+j*len(funcoes)].split(" ")[2])
            vetorplot.append(yval)
            # print(str(yval))
        print(vetorplot)
        plt.plot(qtd, vetorplot, linewidth=1.5,  marker='o')
    plt.legend(tipos, loc='best')
    plt.title(algName)
    plt.grid(True)
    plt.xlabel("Tamanho da entrada : n")
    plt.ylabel("Tempo: s")
    plt.savefig('./Resultados/Graficos/' + algName + '.png')
    # plt.show()
    qplot = qplot+1