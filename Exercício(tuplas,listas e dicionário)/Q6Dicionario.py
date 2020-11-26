jogador = dict()
gols = list()
partidas = 0
jogador['nome'] = str(input('Nome do(a) Jogador(a): '))
partidas = int(input('Quantas partidas ' + jogador['nome'] + ' jogou '))
for p in range(0, partidas):
    gols.append(int(input('Quantos gols na partida ' + str(p+1) + ' ? ')))

jogador['gols'] = gols
jogador['total'] = sum(gols)

print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-=' * 20)
print('O(A) jogador(a) ', jogador['nome'], 'jogou ', len(gols), ' partidas.')
for p in range(0, partidas):
    print('\t=> Na partida ', str(p+1), ' fez ', gols[p], ' gols.')
print('Foi um total de ', jogador['total'], 'gols.')
