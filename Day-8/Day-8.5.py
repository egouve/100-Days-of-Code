# Criar uma função que junte a criptografia e descriptografia

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(text, shift, direction):
    palavra_nova = []
    for letter in text:
        index_letra = alphabet.index(letter)
        if direction == 'encode':
            nova_letra = alphabet[index_letra + shift]
            palavra_nova.append(nova_letra)
        elif direction == 'decode':
            nova_letra = nova_letra = alphabet[index_letra - shift]
            palavra_nova.append(nova_letra)
        else:
            print('Comando Inválido')
            return

    palavra_nova = ''.join(palavra_nova)
    print(palavra_nova)

caesar(text, shift, direction)

