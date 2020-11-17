# a) maior valor
# A função len () retorna o número de itens em um objeto.
# Quando o objeto é uma string, a função len ()
# retorna o número de caracteres na string.
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 12, 3, 3, -52]
maiorValor = lista[0]
menorValor = lista[0]
listaPares = []
ocorrenciasItem1 = 0
mediaElementos = 0
somaNegativos = 0
for index in range(0, len(lista)):
    # Maior valor
    if(maiorValor < lista[index]):
        maiorValor = lista[index]
        #print("maior valor em processo: ", maiorValor)
    if(menorValor > lista[index]):
        menorValor = lista[index]
    if(lista[index] % 2 == 0):
        listaPares.append(lista[index])
    if(lista[index] == lista[0]):
        ocorrenciasItem1 = ocorrenciasItem1+1
    # media
    mediaElementos = + mediaElementos + lista[index]
    if(lista[index] < 0):
        somaNegativos = somaNegativos + lista[index]
mediaElementos = mediaElementos / len(lista)
print("a)Maior Valor: ", maiorValor)
print("b)Menor Valor: ", menorValor)
print("c)Números pares: ", listaPares)
print("d) Número de ocorrências elem. 1: ", ocorrenciasItem1)
print("e) Média dos elementos: ", "%.2f" % mediaElementos)
print("f) Soma dos números negativos: ", somaNegativos)
