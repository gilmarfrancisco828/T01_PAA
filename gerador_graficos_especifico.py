import matplotlib.pyplot as plt
import numpy as np
import inspect
import Algorithm as alg
qtd = [1000, 5000, 10000, 15000, 20000, 25000, 50000, 100000]
tipos = ['aleatorios', 'crescentes', 'decrescentes']
funcoes = inspect.getmembers(alg, inspect.isfunction)
qplot = 0
for t  in tipos:
    plt.figure(qplot)
    fileName = './Resultados/results_' + str(t) + '.txt'
    afile = open(fileName, "r")
    vetor = [x for x in afile.read().split("\n")]
    for i in range(0, len(funcoes)):
        vetorplot = []
        for j in range(0, len(funcoes)-1):
            print(vetor[i+j*len(funcoes)].split(" "))
            yval = float(vetor[i+j*len(funcoes)].split(" ")[2])
            vetorplot.append(yval)
            print(str(yval))
        plt.plot(qtd, vetorplot, linewidth=1.5,  marker='o')

    plt.legend([f[1].__name__ for f in funcoes], loc='best')
    plt.title("Dados:" + t)
    plt.grid(True)
    plt.xlabel("Tamanho da entrada : n")
    plt.ylabel("Tempo: s")
    plt.savefig('./Resultados/Graficos/' + t + '.png')
    # plt.show()
    qplot = qplot+1