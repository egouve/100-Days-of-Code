# Checar se é número primo

def checar_numero_primo(numero):
    for n in range(2, 8):
        if numero % numero == 0 and numero % n != 0:
            print('É primo')
            return
        else:
            print('Não é primo')
            return


numero = int(input('Escolha um número: '))

checar_numero_primo(numero)

