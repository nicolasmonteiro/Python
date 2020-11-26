import random
lista_Num = list()
lista_Num_Sorteados = list()
qnt_Jogos = 0

for l in range(0, 60):
    lista_Num.append(l+1)

qnt_Jogos = int(input('Quantos jogos você quer sortear?'))
for h in range(0, qnt_Jogos):
    lista_Num_Sorteados.append(random.sample(lista_Num, 6))
    print('Jogo ', h+1, ': ', sorted(lista_Num_Sorteados[h]))
