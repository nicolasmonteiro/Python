lista_Alun = list()
lista_Alun_Composta = list()
qntd_Alunos = 0
i = 0
media = 0
aluno = -1
qntd_Alunos = int(input('Quantos(as) Alunos(as)?'))

# adicionando os dados pelo teclado
for q in range(0, qntd_Alunos):
    lista_Alun.append(str(input('Digite o nome do(a) aluno(a): ')))
    lista_Alun.append(float(input('Digite a primeira nota ')))
    lista_Alun.append(float(input('Digite a segunda nota ')))
    media = (float(lista_Alun[i+1])+float(lista_Alun[i+2]))/2
    lista_Alun.append(float(media))
    # print(lista_Alun)
    lista_Alun_Composta.append(lista_Alun[i:])
    i += 4

# printando a tabela
print('Lista composta ', lista_Alun_Composta)
i = 0
print("No.\tNome\t\tMédia")
print('----------------------------------')
for a in range(0, len(lista_Alun_Composta)):
    print("%s\t%s\t\t%.2f" %
          (str(a), lista_Alun_Composta[a][i], lista_Alun_Composta[a][3]))
print('----------------------------------')

# printando as notas
while aluno != 999:
    if aluno != -1:
        print('Notas de ', lista_Alun_Composta[aluno]
              [i], ' são', lista_Alun_Composta[aluno][1:3])
        print('----------------------------------')
    aluno = int(input('Mostrar notas de qual aluno(a)? (999 interrompe) '))
