alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#@'

key = 19

message = """
Préparation pour gateau au chocolat de 500 Grammes. (Prévoir un glaçage au noix de pécan)

100 mL d'huile végetale
4 gros oeufs
100 Grammes de pépites de chocolat
200 Grammes de Beurre ou de Margarine
300 Grammes de Sucre Semoule
200 Grammes de farine

Ajoutez des élements de décor,tels que :

Biscuits en forme de poisson
Bonbons en forme de poisson
Déchets en forme de poisson
Débris en forme de poisson
Éthylbenzène de poisson
Ecorces de Réglisse
Composant organique en forme de poisson
Sédiments en forme de Sédiments
Beurre de cacahuète caramelisé en forme de poisson
Un zeste de citron
Résines Alpha
Résine de Polyester non saturée
Résines à fibre de verre
Composants volatiles de lait malté
9 gros jaunes d'oeufs
12 membranes géo-synthétiques moyennes
100 Grammes de Sucre Semoule
Une touche de "Comment tuer quelqu'un à mains nues "
2 verres de dés de Rhubarbe
3 verres de Rhubarbe en poudre
Une cuillerée à soupe de Rhubarbe tout usages
Une cuillerée à café de Rhubarbe rapée
3 cuillerées à soupe de Rhubarbe flambée
1 grosse Rhubarbe
Une Rhubarbe d'imagerie électromagnétique à sondes croisés
2 cuillerées à soupe de jus de Rhubarbe
Un flag de Rhubarbe CTF101{c4a83ca68ab72b18d48aa034fb5abb57}
Un repose tête ajustable en aluminium
Un injecteur électrique à aiguilles
Un injecteur électrique à aiguilles sans fil
Un outil d'injection d'aiguilles
Un pistolet à aiguilles
Des protèges cranes (Il contient tout les conservateurs agents de pénétration,gaz et substance chimique autorisée
our prévenir la putréfaction malodorante des tissus. )
"""


def decalage(message, key):
    encrypted = ""
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            index = (index + key) % len(alphabet)
            encrypted += alphabet[index]
        else:
            encrypted += letter
    return encrypted

encrypted = decalage(message, key)
print(encrypted)

decrypted = decalage(encrypted, -key)
print(decrypted)

with open('encrypted.txt', 'w') as f:
    f.write(encrypted)

with open('decrypted.txt', 'w') as f:
    f.write(decrypted)