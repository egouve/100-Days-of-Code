#Jogo de adivinhação

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

def guess_game():
    jogar_de_novo = True
    while jogar_de_novo == True:
        dificuldade = input('Qual a dificuldade do jogo? Fácil ou Difícil? Digite F ou D\n').upper()
        numero = random.randint(1, 101)
        if dificuldade == 'D':
            vidas = 5
        elif dificuldade == 'F':
            vidas = 10
        while vidas > 0:
            tentativa = int(input('Escolha um número de 1 a 100: '))

            if tentativa > numero:
                print('Muito alto!')
                vidas -= 1
                if vidas == 0:
                    print('Uma pena, você perdeu.')
                elif vidas > 0:
                    print(f'Você tem mais {vidas} tentativas\n')

            elif tentativa < numero:
                print('Muito baixo!')
                vidas -= 1
                if vidas == 0:
                    print('Uma pena, você perdeu.')
                elif vidas > 0:
                    print(f'Você tem mais {vidas} tentativas\n')

            else:
                print('Acertou, parabéns!')
                vidas = 0

        continuar = input('Gostaria de jogar de novo? S ou N\n').upper()
        if continuar == 'N':
            jogar_de_novo = False
        else:
            guess_game()

guess_game()