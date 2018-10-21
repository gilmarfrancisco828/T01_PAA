import random
ordem = ['aleatorios', 'crescentes', 'decrescentes']

try:
    qtd = int(input('Quantidade de numeros: '))

    # escolhaOrdem = int(input('0 - aleatorios\n1 - crescentes\n2 - decrescentes\n:'))

    for escolhaOrdem in range(len(ordem)):
        fileName = './Dados/dados_' + ordem[escolhaOrdem]+ '_' + str(qtd) + '.txt'
        afile = open(fileName, "w")
        
        for i in range(qtd):
            if escolhaOrdem == 0:
                line = str(random.randint(0, 10*qtd)) + '\n'
            elif escolhaOrdem == 1:
                line = str(i) + '\n'
            elif escolhaOrdem == 2:
                line = str(qtd-i) + '\n'
            else:
                print('Escolha uma ordem.')
                close()
            afile.write(line)
            # print(line)
except ValueError:
    print('Entre com um inteiro.')

afile.close()
