# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
# DICA ESTUDEM A BIBLIOTECA PYTHON RANDOM
import random
num = random.randint(0,5)
resposta = int(input("Digite qual número você acha que o computador pensou: "))
if resposta == num:
    print("Parabéns, você acertou!!!")
else:
    print("Você errou, seu perdedor!")
    