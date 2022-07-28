# Trouver son chemin

## Difficulté : facile

### Description :

On dirait bien que notre cher directeur ne veut pas qu’on retrouve l’endroit où il a caché son secret. Mais il doit bien y avoir un moyen de retrouver le bon chemin…

### Analyse

Nous sommes toujours dans l'image montée, et on nous dit qu'un fichier est caché au milieu de tous ces dossiers. Il nous faut donc trouver un fichier. On peut pour celà utiliser la commande `find`.

### Exploitation

On exécute donc `find . -type f` pour rechercher tous les fichiers (non dossier) à partir du répertoire courant.

On trouve plusieurs fichiers dont un *./eb2fcdb/711a6/66d8e/bdac1/48521/8a99e/flag.txt*. Le fichier nous dit que le flag est la concaténation des répertoires supérieurs. 

### Solution

flag: CTF101{eb2fcdb711a666d8ebdac1485218a99e}