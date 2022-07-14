# PACT : Petite App Créée par Tarik

## Difficulté : facile / moyen

### Description :

Des vieuxAs nous ontenovyé un **APK** qui contiendrait le PACT de Tarik ! Avec ça impossible d'invalider. Seulement, l'application demande un mot de passe, mais les vieuxAs nous assurent qu'avec un peu de reverse, ça ne devrait pas être trop dur. A vous de jouer !

### Analyse

Nous avons à notre disposition un fichier APK et la description nous incite à le décompiler. On utilise alors l'outil jadx-gui pour obtenir un code Java lisible, et comprendre ce que fait l'application.

La fonction exécutée lors du clic sur le bouton nous intéresse tout particulièrement, en plus d'une fonction *XOR* qui renvoie le XOR de deux tableaux d'octets.

On s'intéresse alors aux lignes suivantes :
```java
String obj = MainActivity.this.password.getText().toString();

String str = new String(
    MainActivity.this.XOR(
        obj.getBytes(StandardCharsets.UTF_8), MainActivity.xorxor), StandardCharsets.UTF_8);

MainActivity.this.secret.setText(
    new String(MainActivity.this.XOR(
        MainActivity.encoded, obj.getBytes(StandardCharsets.UTF_8))));

if (!str.contentEquals("connaissez_vous_le_XOR?")) {
                    Toast.makeText(MainActivity.this, "Bah alors ? On s'est trompé ?", 1).show();
                }

```

La première ligne permet de récupérer le mot de pase fournit par l'utilisateur.

La seconde récupère sans `str` la chaîne de caractère xorée de ce mot de passe avec les octets de `xorxor`

Ensuite, on met dans un champ de texte le XOR d'un tableau nommé `encoded` avec le mot de passe de l'utilisateur, **non xoré** !

Enfin un test est efféctué afin de vérifier que `str` vaut bien `"connaissez_vous_le_XOR?"`.

### Exploitation

Il s'agit donc de trouver la chaîne à utiliser pour que son XOR avec `xorxor` donne bien connaissez_vous_le_XOR?.

Et c'est facile ! En effet une des propriétés du XOR est que si
$$ A \oplus B = C$$
Alors
$$ C \oplus B = A \oplus B \oplus B = A$$

Il nous suffit donc de xorer `$connaissez_vous_le_XOR?"\ avec le tableau `xorxor` pour obtenir le mot de passe !

On trouve alors **TarikLePlusBoQuiGereTro**.

Plus qu'à l'utiliser dans l'application pour déchiffrer le texte et obtenir le flag

### Solution

CTF101{9a4cfa35ee2cc9c370195e2ce3cef226}