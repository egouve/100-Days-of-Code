# Checar se é número primo

def checar_numero_primo(numero):
    for n in range(2, numero):
        if numero % n == 0:
            print("Não é primo")
            return

    print("É primo")

numero = int(input('Escolha um número: '))

checar_numero_primo(numero)

