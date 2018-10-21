import random

fileName = './Dados/' + str(input('Arquivo: '))
afile = open(fileName, "w")

try:
    qtd = int(input('Quantidade de numeros: '))
    for i in range(qtd):
        line = str(random.randint(0, 10*qtd)) + '\n'
        afile.write(line)
        # print(line)
except ValueError:
    print('Entre com um inteiro.')

afile.close()
