# Criar uma função que decriptografe uma mensagem

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def criptografar(text, shift):
    palavra_nova_criptografada = []
    for letter in text:
        index_letra = alphabet.index(letter)
        nova_letra = alphabet[index_letra + shift]
        palavra_nova_criptografada.append(nova_letra)

    palavra_nova_criptografada = ''.join(palavra_nova_criptografada)
    print(palavra_nova_criptografada)

def decriptografar(text, shift):
    palavra_nova_decriptografada = []
    for letter in text:
        index_letra = alphabet.index(letter)
        nova_letra = alphabet[index_letra - shift]
        palavra_nova_decriptografada.append(nova_letra)

    palavra_nova_decriptografada = ''.join(palavra_nova_decriptografada)
    print(palavra_nova_decriptografada)


if direction == 'encode':
    criptografar(text, shift)
elif direction == 'decode':
    decriptografar(text, shift)
else:
    print('Comando Inválido')