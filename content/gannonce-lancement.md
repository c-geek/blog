Title: Petites annonces payables en Ğ1 !
Date: 2017-05-02 17h00
Slug: gannonce-lancement
Authors: cgeek
Tags: ğannonce, ğ1
Category: Evénements
Thumbnail: /images/gannonce.png

Le lancement de Ğ1, première monnaie libre P2P de l'Histoire, a été officialisé [le 8 mars 2017 sur le site de Duniter](https://duniter.org/fr/g1-go). Depuis ce jour nous pouvons réaliser des échanges en monnaie libre Ğ1.

Toutefois aujourd'hui encore, nous ne disposons pas d'un site web qui centraliserait les offres de biens et services à vendre en Ğ1.

Alors en attendant cela, je vous propose une petite alternative : je vous présente [ğannonce](https://gannonce.cgeek.fr) ! Prononcez « j'annonce ».

![](/images/gannonce_1.png)

## Un prototype, c'est technique !

ğannonce est un petit site web permettant de poster des petites annonces afin de vendre biens et services dont les prix sont exprimés en Ğ1.

**Ce site est un prototype**. Il n'a pas pour but d'être utilisé sur le *long terme* comme site d'annonces pour les utilisateurs de Ğ1. D'ailleurs, je ne le maintiendrai que quelques mois sans ajouter de nouvelles fonctionnalités.

Le but de ğannonce est plutôt de donner un exemple technique d'application web basée sur la blockchain Ğ1.

Et *accessoirement*, nous pouvons nous en servir de façon temporaire pour mettre en avant biens et services que l'on souhaiterait vendre.

> Ce site est donc une sorte de présentation technique. Si vous n'êtes pas un minimum à l'aise avec la manipulation de votre trousseau cryptographique Ğ1, ne vous entêtez pas à vouloir y poster des annonces !

## Basé sur la blockchain

Vous n'aurez pas besoin de vous inscrire sur ğannonce de façon classique comme sur d'autres sites : pas besoin de pseudo, d'adresse e-mail ou d'informations personnelles. Non : tout ce dont vous aurez besoin sera de vous créer un porte-monnaie alimenté en Ğ1 (au moins 1,00 Ğ1 sur le porte-monnaie pour pouvoir créer un compte ğannonce).

Une fois en possession d'un tel porte-monnaie, vous pourrez créer votre compte de vendeur sur le site ğannonce.cgeek.fr et créer vos propres annonces, sans aucun frais !

C'est donc un excellent exercice pour vous habituer à manipuler des porte-monnaie !

![](/images/gannonce_exemple_compte.png)

## Avec du financement participatif !

Une des fonctionnalités particulières à ğannonce est la possibilité de créer des annonces de *financement participatif*. Qu'est-ce donc ?

C'est la possibilité de proposer une annonce pour le financement d'un bien ou d'un service, et d'avoir *un suivi automatique de son financement* via les transactions Ğ1 qui transitent dans la blockchain.

![](/images/gannonce_crowdfunding.png)

Le mécanisme est simple : ğannonce repère les transactions dans la blockchain Ğ1 dont le commentaire contient le motif `GANNONCE:CROWD:identifiant-de-l-annonce`.

Si donc je poste une annonce qui viserait à financer le développement de modifications importantes sur le logiciel Duniter, et que cette annonce portait l'identifiant `085c1060-b76e-4e4f-a4fb-e9ef598c870b` (généré automatiquement par ğannnonce), alors une personne qui enverrait de la monnaie au vendeur avec comme commentaire de transaction `GANNONCE:CROWDF:085c1060-b76e-4e4f-a4fb-e9ef598c870b` verrait celle-ci tracée par ğannonce et rendue visible explicitement dans l'annonce comme ayant participé du financement.

Et donc, tout le monde pourrait voir l'évolution du financement de cette annonce ! Pratique pour du financement pariticipatif.

Notez bien que **ğannonce n'est pas un intermédiaire** et n'est donc aucunement responsable des fonds qui transitent. L'outil agit comme simple aide à la visualisation d'un financement dans ce cas précis.

## Informations techniques

> Ce paragraphe est destiné aux développeurs.

Quelques informations concernant le code source de ğannonce.

ğannonce est disponible sur GitHub sous licence libre AGPL v3.0 en 2 dépôts :

* [gannonce-pod](https://github.com/c-geek/gannonce-pod) pour la partie serveur
* [gannonce-ui](https://github.com/c-geek/gannonce-ui) pour la partie graphique (site web)

### gannonce-pod

La partie serveur est en fait [un nœud spécialisé Duniter](https://blog.cgeek.fr/rml8-journee1-resume.html). C'est donc un nœud communiquant avec le réseau Ğ1 et qui possède la blockchain localement.

gannonce-pod étend les fonctionnalités du nœud en ajoutant une API de gestion de comptes ğannonce et de création d'annonces, ainsi que de suivi des transactions liées à une annonce.

gannonce-pod est écrit en JavaScript et fonctionne avec Node.js v6.

### gannonce-ui

La partie graphique est un site web fonctionnant sous [Ionic 2](https://ionicframework.com/docs/). C'est donc un pur site statique HTML/CSS/JS, qui peut être hébergé par n'importe quel serveur web.

Ce site communique par requêtes HTTP asynchrones avec un pod gannonce-pod prédéfini.

gannonce-ui repose sur Ionic 2 et donc [Angular 2](https://angular.io/), et le code source de gannonce-ui est majoritairement du TypeScript, un langage qui se compile en JavaScript.

Le site est par ailleurs buildé avec [Brunch](http://brunch.io/), outil formidable qui accélère fortement le développement en produisant rapidement les fichiers finaux du site à partir des sources.

## Un petit pas pour Ğ1, un grand pour les échanges

Malgré la complexité potentielle de cet outil ainsi que sa vocation de démonstration technique, *vous pouvez quand même utiliser ğannonce*.

Dites-vous simplement que c'est temporaire, technique, et qu'il vaudra mieux passer à un outil plus performant quand celui-ci verra le jour.

A bientôt sur ğannonce, j'ai d'ailleurs quelques développements à financer si le cœur vous en dit ! ;-)
