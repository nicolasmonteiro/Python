import random
import time


def jogadas():
    jogada1 = random.randint(0, 2)
    time.sleep(1)
    jogada2 = random.randint(0, 2)
    return jogada1, jogada2


def jokenpo():
    jog1, jog2 = jogadas()
    elementos = ['pedra', 'papel', 'tesoura']
    if(jog1 == jog2):
        return 'Empate Jogador1: ' + elementos[jog1] + ' Jogador2: ' + elementos[jog2]
    if((jog1 == 0 and jog2 == 1) or
       (jog2 == 0 and jog1 == 1)):
        return 'O papel Venceu!' + 'Jogador 1: ' + elementos[jog1] + ' Jogador2: ' + elementos[jog2]
    elif((jog1 == 0 and jog2 == 2) or
         (jog2 == 0 and jog1 == 2)):
        return 'A Pedra Venceu!' + 'Jogador 1: ' + elementos[jog1] + ' Jogador2: ' + elementos[jog2]
    elif((jog1 == 2 and jog2 == 1) or
         (jog2 == 2 and jog1 == 1)):
        return 'A Tesoura Venceu!' + 'Jogador 1: ' + elementos[jog1] + ' Jogador2: ' + elementos[jog2]


print(jokenpo())
