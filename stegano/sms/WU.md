# PACT : Drôle de SMS

## Difficulté : facile

### Description :

Nous avons mis un keylogger sur le téléphone de Bensalem, mais vu son ancienneté, on ne comprend pas comment elle alimente son compte insta… Nous avons tout de même récupéré des données qu’elle aurait envoyées. Essayez de mettre de l’ordre là- dedans !

```
555 33 0 6 666 8 0 3 33 0 7 2 7777 7777 33 0 33 7777 8 0 6 88 555 8 444 8 2 7
```

Le flag est CTF101{md5(secret obtenu en majuscules)}

### Analyse

On remarque une suite de chiffre séparée par des espaces et les chiffres se répètent entre 1 et 4 fois. La description parle de SMS et de keylogger. On a donc récupérer les gestes de Glady sur son téléphone.

On comprend alors que Celui-ci a appuyé 3 fois sur le 5, puis 2 fois sur le 3 etc... C'est du MultiTap ! C'est comme ça qu'on envoyait des SMS quand les claviers n'avaient presque que des chiffres. A l'aide d'un outil en ligne ou manuellement avec une photo d'un ancien téléphone on décode aisément le message.

### Exploitation

On obtient alors le SMS 
```
LE MOT DE PASSE EST MULTITAP
```

On récupère donc le md5 de MULTITAP : `5a5a8f4f8882cec331b7c0d807f6bcc8`

### Solution

Le flag est alors CTF101{5a5a8f4f8882cec331b7c0d807f6bcc8}