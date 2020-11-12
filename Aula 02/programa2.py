import random
random.seed()
sorteio = random.randint(1, 10)
for m in range(1, 4):
    numero = input("Qual seu palpite? ")
    if (sorteio == numero):
        print("Você acertou!")
        break
    elif(m != 3):
        print("tente novamente")
else:
    print("Você perdeu! Hoje não foi o seu dia")
print("Número sorteado: ", sorteio)
