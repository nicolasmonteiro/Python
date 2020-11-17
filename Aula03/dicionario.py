#contatos = {'Yan': '1234-5678', 'Taty': '1234-5696'}
# print(contatos['Yan'])

# verifica se um canto está no nosso dicionário
#print('Yan' in contatos)
#print('1234-5678' in contatos)
#print('1234-5678' in contatos.values())
# print(contatos)
# Adicionar item ao dicionário
#contatos['João'] = '8887-7778'
# print(contatos)

# remover contato
#del contatos['João']
# print(contatos)


# lista de tuplas
'''
contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),
                  ('Ana', '8765-4321'), ('Marina', '8877-7788')]

contatos = dict(contatos_lista)
print(contatos['Ana'])
'''


# juntando agendas

meus_contatos = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                 'Ana': '8765-4321', 'João': '8887-7778'}

contatos_do_pedro = {'Yan': '1234-5678', 'Fernando': '4345-5434',
                     'Luiza': '4567-7654'}
'''
for nome in contatos_do_pedro:
    meus_contatos[nome] = contatos_do_pedro[nome]

print(meus_contatos)
'''

# jeito mais simples
# update() : Atualiza dicionário com pares chave/valor
meus_contatos.update(contatos_do_pedro)
print(meus_contatos)
