# Plus de traces

## Difficulté : facile

### Description :

Vous avez réussi à localiser le bon dossier mais étrangement, rien ne semble mériter une telle protection… Il semblerait que Glady ait effacé ses traces. Le fichier serait donc perdu à tout jamais ?

### Analyse

Nous sommes dans un répertoire vide, à part le flag du challenge précédent. Heureusement, bien souvent les fichiers ne sont pas réellement supprimés et un coup de `ls -all` révèle un dossier caché qui n'est autre que la corbeille.

### Exploitation

on se rend donc dans le dossier *.Trash-1000/files*  pour y trouver un document word **to_remove.docx**. Heureusement, il est encore intact et on y trouve à l'intérieur une belle image nous donnant le flag.

### Solution

flag: CTF101{feea8682b26cce407f3dc84b5a2c3bb5}