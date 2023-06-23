#Step 1

word_list = ["aardvark", "baboon", "camel"]

# TO DO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TO DO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# tO DO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

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

letras_escolhidas_anteriormente = []
while '_' in palavra:
    letra_escolhida = input('Escolha uma letra\n').lower()

    if letra_escolhida not in alfabeto:
        print('Por favor, escolha uma letra válida.\n')
    elif letra_escolhida in letras_escolhidas_anteriormente:
        print('Por favor, escolha uma letra ainda não informada.\n')
    else:
        if letra_escolhida in palavra_escolhida:
            for letra in range (n_letras):
                if palavra_escolhida[letra] == letra_escolhida:
                    palavra[letra] = letra_escolhida

            palavra_string = ' '.join(palavra)
            print(palavra_string)
            print('Muito bom!\n')

        else:
            print('Errou!\n')

    letras_escolhidas_anteriormente.append(letra_escolhida)

if '_' not in palavra:
    print('Você venceu!')




