'''
funcoes com retorno
return: finaliza a função. Sai da execução da função
podemos ter diferentes retornos sendo apenas um executado)
função podendo retornar qualquer tipo de dados até multiplos
valores

'''


def quadrado_de_7():
    return 7*7

# print(quadrado_de_7())
# print(quadrado_de_7())


# sai da função
'''

def diz_oi():
    return 'OI'
    print('teste')  # nunca será executada


print(diz_oi())
'''
'''
# vários returns
def func_retornos():
    v = False
    if v:
        return 4
    elif v is None:
        return 3
    return 't'
print(func_retornos())
'''

'''
retorna múltiplos valores
'''


def outra_func():
    return 2, 3, 4


print(outra_func())
#n1, n2, n3 = outra_func()
#print(n1, n2, n3)
