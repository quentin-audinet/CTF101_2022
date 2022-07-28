# Plus de traces

## Difficulté : facile

### Description :

Vous avez réussi à localiser le bon dossier mais étrangement, rien ne semble mériter une telle protection… Il semblerait que Glady ait effacé ses traces. Le fichier serait donc perdu à tout jamais ?

### Analyse

Nous sommes dans un répertoire vide, à part le flag du challenge précédent. Heureusement, par défaut, lors d'un `rm` ou d'une action de suppression, il est seulement indiqué que la place qu'occupait le fichier est à nouveau libre. Seulement, les données sont toujours là ! Pour réellemlent formater un disque, il faudrait le réécrire complètement avec des données aléatoires ou que  des 0 par exemple.

Il est donc possible, s'il n'y a pas eu de réécriture par dessus de retrouver les données effacées. On peut pour cela utiliser le très bon outil *photorec*.

*Note: On peut aussi remarquer la présence d'un fichier dans .Trash-100/files/, il s'agissait ici d'une fausse piste mais ce répertoire représente la corbeille du disque.*

### Exploitation

On ouvre donc *photorec* avec `photorec image.dd`. On suit les étapes en sélectionnant d'abord le disque, puis la partition trouvée, en indiquant le format (ext4 automatiquement trouvé) et en choisissant l'espace libre (où rien n'est écrit, car on suppose que la zone est de nouveau considérée libre et que rien n'a été réécrit par dessus). On choisit la destination où les fichiers trouvés seront enregistrés et on lance l'opération !

*Photorec* nous trouve un fichier .docx et en l'ouvrant, une photo de Glady nous donnant le flag.

### Solution

flag: CTF101{feea8682b26cce407f3dc84b5a2c3bb5}