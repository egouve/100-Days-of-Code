#Criação de jogo jokenpo

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

jokenpo = [rock, paper, scissors]
jogada_player = int(input('O que você vai escolher? Escolha 0 para pedra, 1 para papel e 2 para tesoura. '))

jogada_pc = random.randint(0,2)

print(f'Você jogou {jokenpo[jogada_player]}')

print(f'Seu oponente jogou {jokenpo[jogada_pc]}')

jogadas = [jogada_player, jogada_pc]

if jogadas == [0,0] or jogadas == [1,1] or jogadas == [1,1]:
    print('Deu empate!')
elif jogadas == [0,2] or jogadas == [1, 0] or jogadas == [2,1]:
    print('Você venceu!')
else:
    print('Você perdeu!')



