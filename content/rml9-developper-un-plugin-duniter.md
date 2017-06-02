Title: Développer un plugin pour Duniter
Date: 2017-06-01 09h00
Slug: developper-un-plugin-pour-duniter
Authors: cgeek
Tags: ğ1, duniter, plugin, nœud spécialisé
Category: Développement

Pour ces RML9, nous aborderons une nouveauté qui sera présente dans la prochaine version de Duniter 1.3.0 : les *modules*, appelés aussi *plugins*.

Les modules sont des morceaux de code qui n'appartiennent pas au programme principal, et qui sont souvent développés par une personne tierce pour venir « se brancher » au code principal, sans le modifier directement.

C'est une façon de séparer les tâches et d'isoler le code dans la partie qui lui revient, afin de ne pas tout mélanger.

> Ceux ayant développé un [nœud spécialisé](/rml8-journee1-resume) suite aux RML8 n'auront aucun mal à transformer celui-ci en module, quelques minutes suffisent.

## Des exemples de modules

D'ores et déjà, Duniter est pourvu de 5 modules : 

* **duniter-keypair** fournit le trousseau de clés cryptographiques au nœud Duniter, par exemple un trousseau chiffré sur le disque

* **duniter-bma** expose le nœud sur le réseau Ğ1 via l'API BMA, ce module installe embarque et lance un serveur HTTP

* **duniter-crawler** contacte les autres nœuds du réseau en effectuant des requêtes HTTP, pour des opérations de synchronisation ou de partage de documents

* **duniter-prover** génère les nouveaux blocs et calcule la preuve de travail nécessaire à leur acceptation

* **duniter-ui** propose une interface graphique pour gérer son nœud Duniter

## Fonctionnalités apportées par un module

Un module intervient essentiellement à 2 niveaux :
 
### Ajouter une commande ou des options

Un module peut typiquement ajouter une commande au programme `duniter`. Par exemple, le module `rml9-hello-module` que nous installerons par la suite ajoute la commande `hello` :

    duniter hello
    Hello depuis le module RML9 !
    
Le module peut même ajouter des options :
 
    duniter hello --comment "Facile !"
    Hello depuis le module RML9 ! Facile !

### Injecter un service ou de la configuration

Un module peut intervenir à l'exécution, pour s'intégrer dans la vie d'un nœud qui fonctionne en permanence. C'est l'ajout d'un service. Par exemple `duniter-prover` attend le moment opportun pour calculer le prochain bloc, puis génère un bloc et calcule la preuve de travail correspondante, pour enfin propager le bloc trouvé. Tout cela en parallèle de l'exéction normale du nœud.

Optionnellement, un module peut intervenir au moment du chargement et de la sauvegarde de la configuration du nœud : c'est le cas de `duniter-keypair`, qui charge un trousseau en mémoire et s'occupe de son éventuel stockage sur le disque.


### Pré-requis

Pour exécuter le code qui suit, vous aurez besoin des programmes suivants :

* [Git](https://git-scm.com/)

        sudo apt install git

* [Node.js v6 ou supérieur](https://nodejs.org/en/)

        curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash
        nvm install 6

* [Yarn](https://yarnpkg.com/lang/en/docs/install/)

        curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
        echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
        sudo apt-get update && sudo apt-get install yarn

* [Python 2](https://www.python.org/downloads/)
    
**Pour Windows** : une fois Git, Node.js et Yarn installés, lancez la commande :
  
    npm install --global --production windows-build-tools

## 1. Développer un module : `rml9-hello-module`

Le but est d'exécuter notre tout premier module, qui va bêtement afficher « *Hello depuis le module RML9 !* ».

    git clone https://dev.cgeek.fr/cgeek/rml9-hello-module.git
    cd rml9-hello-module
    yarn
    
Puis, testez le bon fonctionnement du module :

    node run.js hello
    Hello depuis le module RML9 !

### Changer le message affiché

Un premier exercice simple, pour vérifier que vous modifiez bien le bon fichier : modifiez le message affiché en changeant la chaîne de caractère du fichier `index.js`, dans lequel se trouve le code de votre module : 

    node run.js hello
    Hello depuis le module RML9, version modifiée !

### Ajouter la commande `nb-membres`

Deuxième exercice simple, décommenter le bloc nommé `Exercice 2`, puis lancer la commande suivante : 

    node run.js nb-membres
    La monnaie Ğ1 contient 0 membres.

Bien sûr, cette proposition n'est pas vraie : la monnaie Ğ1 contient en réalité plus de 130 membres. Mais la base de données de notre nœud est vide. Synchronisons la blockchain Ğ1 pour changer cela :

    
    node run.js sync g1.duniter.org 80
    Progress:
    
    Download: [||||||||||||||||||||] 100 %
    Apply:    [||||||||||||||||    ] 84 %

Ceci est possible car le module `duniter-crawler` est présent dans les dépendances *de développement* de notre projet. Vous pouvez le vérifier dans le fichier `package.json` : 

```json
{
  "name": "rml9-hello-module",
  "version": "1.0.0",
  "main": "index.js",
  "license": "GPLv3",
  "devDependencies": {
    "duniter": "1.3.x",
    "duniter-crawler": "1.3.x"
  },
  "peerDependencies": {
    "duniter": "1.3.x"
  }
}
```

> Si nous ajoutions d'autres modules dans la partie `devDependencies`, puis modifiions le fichier `run.js` en conséquence, nous pourrions ajouter d'autres commandes pour notre fichier de test `run.js`.

La synchronisation est terminée ? Bien, relançons la commande `nb-membres` :

    node run.js nb-membres
    La monnaie Ğ1 contient 137 membres.

Cette fois-ci, le compte est bon !

### Ajouter l'option `--sentries`

Troisième exercice, décommenter le bloc nommé `Exercice 3` qui active l'option `--sentries` dans la commande `nb-members`. Si cette option fonctionne, alors nous obtenons le nombre de membres référents dans la monnaie :
 
    node run.js nb-membres --sentries
    La monnaie Ğ1 contient 81 membres référents.
    
## 2. Installer des modules

Nous avons désormais notre premier module développé, prêt à être installé et utilisé. Oui mais, comment installe-t-on un module Duniter ? Et surtout, où ?

### Cloner le projet Duniter

C'est en fait *au sein du nœud Duniter* que nous installons le module. Nous y branchons notre module, nous étendons le cœur du logiciel, ses fonctionnalités de base.

Le plus simple pour notre exemple est de récupérer les sources : 

    cd ..
    git clone -b dev https://github.com/duniter/duniter.git
    cd duniter
    yarn
    bin/duniter --version
    
La dernière commande doit afficher `1.3.2`. Si vous avez bien cette version, nous pouvons continuer.
 
### Installer notre module `rml9-hello-duniter`

D'abord, faisons une vérification : 

    bin/duniter hello
    Unknown command 'hello'. Try --help for a listing of commands & options.

La commande est inconnue. C'est normal, puisque le module RML9 n'est pas installé avec Duniter. Nous allons toutefois l'ajouter : 

    bin/duniter plug file://$PWD/../rml9-hello-module

Puis relançons la commande `hello` :

    bin/duniter hello
    Hello depuis le module RML9, version modifiée !

Puis la commande `nb-membres` :

    bin/duniter nb-membres
    La monnaie Ğ1 contient 137 membres.
    
Puis la commande `nb-membres --sentries` :

    bin/duniter nb-membres --sentries
    La monnaie Ğ1 contient 81 membres référents.
    
Si vous avez ces messages, c'est que le module `rml9-hello-module` a bien été *branché* en tant que module à votre nœud Duniter !

**Vous avez donc réussi à produire votre 1er module Duniter et à l'ajouter à votre nœud local !**

Maintenant, vous pouvez effectuer des modifications sur ce module, ou même en créer un nouveau, puis le publier sur une adresse publique (par exemple sur un dépôt GitHub) et permettre à n'importe qui de l'installer sur sa propre instance !

### Installer un autre module `rml9-mass-duniter`

Voici un module que j'ai développé, et qui affiche quelques informations sur la masse monétaire. Pour l'ajouter :

    bin/duniter plug git+https://dev.cgeek.fr/cgeek/rml9-mass-module.git
    
Puis pour connaître la masse monétaire :

    bin/duniter masse
    La masse monétaire effective est de 74581.87 Ğ1

Nous pouvons également connaître la masse théorique : 

    bin/duniter masse --theorique
    La masse monétaire théorique est de 74590.00 Ğ1
    
Ainsi que la masse détruite (correspond aux comptes nettoyés du fait d'un solde < 1,00 Ğ1)

    bin/duniter masse --detruite
    La masse monétaire détruite est de 8.13 Ğ1
    
Comme vous pouvez le constater, il est très facile d'ajouter de nouvelles fonctionnalités à son nœud qu'une personne tierce aurait développé.

## 3. Les modules et Duniter UI

Nous arrivons à l'étape ultime : nous allons installer des modules *depuis l'interface graphique de Duniter*.

Pour ce faire, démarrer Duniter avec son UI : 

    bin/duniter direct_webstart
    
Nous pouvons alors visiter l'adresse http://localhost:9220 pour accéder à l'UI, puis aller dans la partie Settings > Modules : 

![](/images/modules_ui_1.png)

Nous pouvons faire un 1er constat : nous avons là une liste de modules, et tous nous sont connus. Nous y retrouvons les modules importants estampillés « required » ainsi que nos 2 modules précédemment installés `rml8-hello-module` et  `rml8-mass-module`.

### Ajout de modules via l'UI

Nous aurions pu ajouter nos modules via cette page plutôt qu'en ligne de commande. Faisons le test en ajoutant un 3ème module : `git+https://dev.cgeek.fr/cgeek/duniter-ui-cesium.git`

----

![](/images/modules_ui_2.png)

----

Puis cliquez sur « Installer ». Vous pourrez suivre rapidement l'installation :

----

![](/images/modules_ui_3.png)

----

Enfin dès que celle-ci est terminée, vous devriez obtenir un nouveau module `duniter-ui-cesium` dans la liste, ainsi qu'une notification de redémarrage dans le coin supérieur droit de l'interface :

![](/images/modules_ui_4.png)

Je vous invite alors à redémarrer, et constater l'apparition d'un nouveau bouton « Cesium » :

![](/images/modules_ui_5.png)

Qui quand on clique dessus, nous ouvre une fenêtre d'un Cesium embarqué :

![](/images/modules_ui_6.png)

### Ajout d'un second module web

Ajouter le module `git+https://dev.cgeek.fr/cgeek/rml9-web-module.git`. Tester. Modifier à votre guise.

## Extra : déboguer votre module

Nécessite Chromium/Opera :

    sudo apt install chromium-browser
    
Puis `node-inspector` :

    npm install -g node-inspector
    
Retourner dans le module `rml9-hello-module` :

    cd rml9-hello-module
    node-debug run.js hello

## Conclusion

Il est désormais possible de développer des modules pour la version 1.3.x de Duniter, à paraître dans les prochaines semaines. Les modules permettent l'ajout de nouvelles fonctionnalités, d'étendre le cœur et de partager ses développements à de nombreux nœuds Duniter, notamment pour augmenter son instance locale.

Toutefois, il convient de s'assurer de leur provenance et de leur contenu.
