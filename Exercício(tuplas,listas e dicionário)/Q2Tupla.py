lista = ('Mouse  ', 20.50, 'Teclado', 100.00, 'Monitor', 679.00)
i = 0
n = ""

print('Listagem de Preços')
print('----------------------------------')
for c in range(0, len(lista)+1):
    if(i != len(lista)):
        print(lista[i], "\tR$ %.2f" % lista[i+1])
        i += 2
print('----------------------------------')
