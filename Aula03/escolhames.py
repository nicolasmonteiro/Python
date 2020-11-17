meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
mes = 1
while(mes != 13):
    mes = int(input("Escolha um mês (1-12): "))
    if 1 <= mes < 13:
        print('O mês é {}'.format(meses[mes-1]))
    else:
        print('O mês não existe')
