import random
import operator
jogadores = dict()
i = 1
valor = 0
empate = True


print('Valores sorteados: ')
for j in range(0, 4):
    jogadores['jogador'+str(j+1)] = random.randint(1, 6)

# modifica o random para ser único
while empate:
    for k, v in jogadores.items():
        r = random.randint(1, 6)
        if r not in jogadores.values():
            jogadores[k] = r
            empate = False
        else:
            r = random.randint(1, 6)
            empate = True
            # print(jogadores)

# imprime os números dos novos valores do dicionário
for k, v in jogadores.items():
    print(f'O {k} tirou  {v}')
# ordena descrente
ord_dic = sorted(jogadores.items(), key=operator.itemgetter(1), reverse=True)

print("Nova lista", ord_dic)

# exibe o ranking
print('Ranking dos jogadores: ')
for j in range(0, len(ord_dic)):
    print(i, 'º lugar:', ord_dic[j][0], 'com ', ord_dic[j][1])
    i += 1
