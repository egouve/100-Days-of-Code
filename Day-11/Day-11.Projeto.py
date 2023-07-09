# Criar um jogo de BlackJack
import random
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cartas = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cartas_jogador = random.choices(cartas, k=2)
soma_cartas = sum(cartas_jogador)
print(f' Suas cartas são: {cartas_jogador}')
print(f'A soma de suas cartas é: {soma_cartas}\n\n')

cartas_pc = [random.choice(cartas)]
soma_cartas_pc = sum(cartas_pc)

print(f'As cartas da mesa são: {cartas_pc}')
print(f'A soma das cartas da mesa é: {soma_cartas_pc}\n')

def deal():
    soma_cartas = sum(cartas_jogador)
    burst = False
    while burst == False:
        if soma_cartas > 21:
            burst = True
            return burst
        nova_rodada = input('Gostaria de uma nova carta? S para sim, N para não\n').upper()

        if nova_rodada == 'S':
            if soma_cartas + cartas[0] > 21:
                cartas[0] = 1
            nova_carta = random.choice(cartas)
            cartas_jogador.append(nova_carta)
            soma_cartas = sum(cartas_jogador)
            print(f' Suas cartas são: {cartas_jogador}')
            print(f' A soma das suas cartas é: {soma_cartas}\n')
            if soma_cartas < 21:
                deal()
            else:
                print('Soma das cartas é maior que 21. Você perdeu.')

        elif nova_rodada == 'N':
            nova_carta_pc = random.choice(cartas)
            cartas_pc.append(nova_carta_pc)
            soma_cartas_pc = sum(cartas_pc)
            print(f'As cartas da mesa são: {cartas_pc}')
            print(f'A soma das cartas da mesa é: {soma_cartas_pc}\n')
            while soma_cartas_pc < 17:
                nova_carta_pc = random.choice(cartas)
                cartas_pc.append(nova_carta_pc)
                soma_cartas_pc = sum(cartas_pc)
                print('A soma das cartas da mesa são menores que 17. Pescando outra carta.')
                print(f'As cartas da mesa são: {cartas_pc}')
                print(f'A soma das cartas da mesa é: {soma_cartas_pc}\n')

            if soma_cartas_pc > 21:
                print('A mesa estourou o limite de pontuação. Você venceu!')
                burst = True
                return burst

            elif soma_cartas_pc > soma_cartas:
                print(f'A pontuação da mesa é {soma_cartas_pc}, e a sua é {soma_cartas}!\n'
                      f'Você perdeu.')
                burst = True
                return burst

            elif soma_cartas_pc == soma_cartas:
                print(f'A pontuação da mesa é {soma_cartas_pc}, e a sua é {soma_cartas}!\n'
                      f'Deu empate!')
                burst = True
                return burst

            else:
                print(f'A pontuação da mesa é {soma_cartas_pc}, e a sua é {soma_cartas}!\n'
                      f'Você venceu!')
                burst = True
                return burst

deal()








