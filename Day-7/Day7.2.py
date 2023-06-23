# Exercício é criar vidas no jogo da forca, para que o jogador tenha apenas 6 chances de acerto

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

vidas = 6
word_list = ["aardvark", "baboon", "camel"]
import random
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z']
palavra_escolhida = random.choice(word_list)
n_letras = len(palavra_escolhida)
palavra = []

for letra in range(n_letras):
    palavra.append('_')

palavra_string = ' '.join(palavra)
print(palavra_string)
print(stages[vidas])
letras_escolhidas_anteriormente = []

while '_' in palavra and vidas > 0:
    letra_escolhida = input('Escolha uma letra\n').lower()

    if letra_escolhida not in alfabeto:
        print('Por favor, escolha uma letra válida.\n')
    elif letra_escolhida in letras_escolhidas_anteriormente:
        print('Por favor, escolha uma letra ainda não informada.\n')
    else:
        if letra_escolhida in palavra_escolhida:
            for letra in range(n_letras):
                if palavra_escolhida[letra] == letra_escolhida:
                    palavra[letra] = letra_escolhida

            palavra_string = ' '.join(palavra)
            print(palavra_string)
            print('Muito bom!\n')
        else:
            vidas -= 1
            print(palavra_string)
            print('Errou!\n')

    print(stages[vidas])

    letras_escolhidas_anteriormente.append(letra_escolhida)

if '_' not in palavra:
    print('Você venceu!')
if vidas == 0:
    print('Você perdeu.')