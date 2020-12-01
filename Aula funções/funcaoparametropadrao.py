# parâmetro padrão
# valor padrão deve vim no final
'''
def exponecial(numero, potencia=2):
    return numero ** potencia


print(exponecial(2, 3))
'''

'''
def exponecial(numero=2, potencia=2):
    return numero ** potencia

# print(exponecial())
# print(exponecial(5))
# print(exponecial(potencia=3))
#print(exponecial(2, 5))
#print(exponecial(potencia=5, numero=2))


def somar(num1, num2=2, num3=3, num4=4):
    return num1+num2+num3+num4
print(somar(1))
'''


'''

# pq usar parametros padrão:
permite ser mais flexível
evita erros com parametros incorretos

'''
# funções como parâmetro


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def sub(num1, num2):
    return num1-num2


def div(num1, num2):
    return num1/num2


def exp(num1, num2):
    return num1**num2


print(mat(2, 3))
#print(mat(4, 3, sub))
#print(mat(4, 2, div))
#print(mat(4, 2, exp))
