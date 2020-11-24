herois = dict()
personagens = list()
#herois = {'nome': 'Mistica', 'univ': 'Marvel', 'grupo': 'X-men'}
for h in range(0, 3):
    herois['nome'] = str(input('nome do heroi/heroina: '))
    herois['univ'] = str(input('nome do univ: '))
    herois['grupo'] = str(input('nome do grupo: '))
    personagens.append(herois.copy())
print(personagens)
print(personagens[0]['univ'])
