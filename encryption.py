def crypt_message(message, key):
    #Utilizando o mapa caótico para criptografar a mensagem com sequências aleatórias
    message_cript_map = crypt_message_map(message, float(key[2:5]))
    #Utilizando a tabela ascii para criptografar a mensagem descolacando alguns caracteres 
    message_cript_ascii = crypt_message_ascii(message_cript_map, key)
    #Utilizando a função xor para criptografar a mensagem
    message_cript_xor = crypt_message_xor(message_cript_ascii, key)
    
    return message_cript_xor


def decrypt_message(message, key):

    message_descrypt_xor = decrypt_message_xor(message, key)
    message_descrypt_ascii = descrypt_message_ascii(message_descrypt_xor, key)
    message_decrypt_map = decrypt_message_map(message_descrypt_ascii, float(key[2:5]))

    return message_decrypt_map

#INÍCIO DE MAPAS CAÓTICO
def logistic_map(x,r):
    return r * x * (1 - x)

def generate_chaos_sequence(seed, length):
    r = 3.9
    chaotic_sequence = [seed]

    for _ in range(length):
        seed = logistic_map(seed, r)
        chaotic_sequence.append(seed)

    return chaotic_sequence

def crypt_message_map(message, key):
    chaotic_sequence = generate_chaos_sequence(key, len(message))
    ascii = []

    for character, chaotic_value in zip(message, chaotic_sequence):
        value_ascii = ord(character)
        value_ascii = (value_ascii + int(chaotic_value * 10000)) % 127
        ascii.append(value_ascii)

    message_crypt = ''.join(chr(value) for value in ascii)
    return message_crypt

def decrypt_message_map(message, key):
    chaotic_sequence = generate_chaos_sequence(key, len(message))
    ascii = []

    for character, chaotic_value in zip(message, chaotic_sequence):
        value_ascii = ord(character)
        value_ascii = (value_ascii - int(chaotic_value * 10000)) % 127
        ascii.append(value_ascii)

    message_crypt = ''.join(chr(value) for value in ascii)
    return message_crypt

#FIM DE MAPAS CAÓTICOS

#INÍCIO DO DESLOCAMENTO TABELA ASCII
def crypt_message_ascii(message, key):
    ascii = []
    for character in message:
        value_ascii = ord(character)
        value_ascii = (value_ascii + int(key[:2])) % 127

        ascii.append(value_ascii)
        
    message_cript = ''.join(chr(value) for value in ascii)
    return message_cript

def descrypt_message_ascii(message, key):
    ascii = []
    for character in message:
        value_ascii = ord(character)
        value_ascii = (value_ascii - int(key[:2])) % 127

        ascii.append(value_ascii)
    message_decript = ''.join(chr(value) for value in ascii)

    return message_decript

#FIM DO DESLOCAMENTO TABELA ASCII

#INÍCIO DA FUNÇÃO XOR
def crypt_message_xor(message, key):
    binaries = []
    for character in message:
        value_ascii = ord(character)
        value_binary = bin(value_ascii)[2:]
        value_binary = value_binary.zfill(8)
        value_binary = '0b'+value_binary
  
        #xor
        binary_xor = int(value_binary,2) ^ int(key[-10:], 2)
        binary_xor = bin(binary_xor)[2:].zfill(8) 
        binary_xor = '0b'+binary_xor
        binaries.append(binary_xor)
        print(binaries)
    
    crypted_message = ''.join([chr(int(binary, 2)) for binary in binaries])

    return crypted_message

def decrypt_message_xor(message, key):
    binaries = []
    for character in message:
        value_ascii = ord(character)
        value_binary = bin(value_ascii)[2:]
        value_binary = value_binary.zfill(8)
        value_binary = '0b'+value_binary

        #xor
        binary_xor = int(value_binary,2) ^ int(key[-10:], 2)
        binary_xor = bin(binary_xor)[2:].zfill(8) 
        binary_xor = '0b'+binary_xor
        binaries.append(binary_xor)
    
    descrypted_message = ''.join([chr(int(binary, 2)) for binary in binaries])

    return descrypted_message

#FIM DA FUNÇÃO XOR

key = "100.70b10111001"

message = "Vinicius Teixeira Fernandes"
#message_crypt = crypt_message(message, key)
# print(message_crypt)

# mensagem_descrypt = decrypt_message(message_crypt, key)
# print(mensagem_descrypt)

message_bin = crypt_message_xor(message, key)
# print(message_bin)

# print(decrypt_message_xor(message_bin, key))