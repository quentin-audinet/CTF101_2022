message = """
Sans rigoler. Je pratique la MMA depuis maintenant 6 ans, de la boxe en parallèle depuis 7 ans, 
je pourrai. Ainsi que la musculation depuis 4 ans, 1m87 pour 86 kg. 
J'ai une vitesse de fou, et des réflexes identiques à ma vitesse. 
J'ai juste à l'attendre qu'il me charge, l'esquiver et lui donner des bonnes patates dans la tête. 
Je le lâcherai pas à la moindre erreur, le gorille est fini. 
T'auras toujours des puceaux d'ici pour penser que c'est impossible. 
Rien n'est impossible avec de la volonté déjà les amis, et de 2) c'est pas avec votre corps de lâche que vous allez faire quoi que ce soit. 
N'importe quel homme un minimum entraîné peut vaincre un gorille avec un couteau déjà. 
À main nue c'est pas forcément plus compliqué ça demande juste de la technique.
"""

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}"

key = "CTF101{61f6933f179df0c61cba100995e7ebea}"

def vigenere_encrypt(message, key):
    encrypted = ""
    for i, letter in enumerate(message):
        decalage = alphabet.index(key[i % len(key)])
        if letter in alphabet:
            index = alphabet.index(letter)
            index = (index + decalage) % len(alphabet)
            encrypted += alphabet[index]
        else:
            encrypted += letter
    return encrypted

def vigenere_decrypt(message, key):
    decrypted = ""
    for i, letter in enumerate(message):
        decalage = alphabet.index(key[i % len(key)])
        if letter in alphabet:
            index = alphabet.index(letter)
            index = (index - decalage) % len(alphabet)
            decrypted += alphabet[index]
        else:
            decrypted += letter
    return decrypted

encrypted = vigenere_encrypt(message, key)
print(encrypted)

decrypted = vigenere_decrypt(encrypted, key)
print(decrypted)

with open("encrypted.txt", "w") as f:
    f.write(encrypted)

with open("decrypted.txt", "w") as f:
    f.write(decrypted)



