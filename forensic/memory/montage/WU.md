# Savez-vous monter une clé USB ?

## Difficulté : facile

### Description :

Nicolas Glady a égaré une clé USB et celle-ci semble contenir des informations très intéressantes ! Nous avons effectué une copie du lecteur, commencez par trouver comment le monter.

### Analyse

Nous sommes en présence d'un fichier qui est, d'après la description du challenge, un lecteur que nous devons monter.
Pour cela, rien de plus simple ! Il suffit d'exécuter en administrateur la commande `mount`.

### Exploitation

On exécute donc `sudo mount disk.image /mnt` (/mnt peut être remplacé par n'importe quel répertoire pour accueillir le disque)

En affichant le contenu de **/mnt** on découvre de nombreux dossiers aux noms aléatoires ainsi qu'un fichier flag.txt ! C'est lui qui nous intéresse pour le moment.

### Solution

flag: CTF101{c5473b1eabfd20eff523a7710760e977}