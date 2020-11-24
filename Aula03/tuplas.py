# Note que é a vírgula que faz uma tupla, não os parênteses.
# dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado')
# print(type(dias))

# Assim como as listas, também podemos usar uma função para criar uma tupla passando um tipo que
# pode ser iterável como uma string ou uma lista.

# texto = 'python'
# print(tuple(texto))
lista = ('Mouse', 20.50, 'Teclado', 100.00, 'Monitor', 679.00)
i = 0
n = ""
print("Listagem de Preços")
for c in range(0, len(lista)+1):
    if(i != len(lista)):
        print(lista[i], ".......", "R$ ", lista[i+1])
        i += 2
