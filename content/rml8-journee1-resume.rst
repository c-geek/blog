RML8 : Résumé de la journée 1
#############################

:date: 2016-11-19 9h53
:tags: RML, RML8, monnaie libre, duniter
:slug: rml8-journee1-resume
:authors: cgeek
:category: Evénements

.. youtube:: cEuZrwjqDmk

Petite rétrospective sur cette première journée des RML8, où je ferai quelques commentaires sur les exercices réalisés.

Liens vers les présentations et vidéos
--------------------------------------

* cgeek et inso : `Présentation introductive`_
* cgeek : `Spécialiser son nœud Duniter : partie 1`_
* cgeek : `Spécialiser son nœud Duniter : partie 2`_

Vous pouvez également retrouver la liste complète des vidéos de l'ensemble des journées RML8 sur `la chaîne RML8`_.

Déroulement et objet des manipulations
--------------------------------------

Après l'introduction réalisée par inso et moi-même, la journée a été consacrée au code et plus particulièrement à la manipuation de Duniter et de sa base de données.

Le but affiché des exercices proposés était d'avoir une introduction au code de Duniter à travers la manipulation de son cœur et de ses données internes, notamment la blockchain. L'exécution et la modification des 5 fichiers exemples permet de s'approprier les concepts clés, l'organisation des données ainsi que de l'architecture, tout en montrant que le code du cœur peut être exploité à des fins diverses : c'est ce que j'ai appelé *spécialiser son nœud*.

Si vous souhaitez intervenir sur le cœur de Duniter, je vous invite fortement à exécuter ces 5 fichiers (demo1_hello_bloc.js, ..., demo5_websocket.js), à les modifier pour en changer légèrement le comportement, voire à en réaliser un nouveau pour votre propre compréhension et même réaliser une `pull request`_ pour partager votre exemple à d'autres.

Installation des outils
-----------------------

Si vous souhaitez réaliser de nouveau ces manipulations alors vous aurez besoin d'installer Git_, NVM_ et Yarn_.

Ensuite, il vous suffira d'exécuter les commandes suivantes (Linux). D'abord, installer NodeJS v6 ::

  nvm install 6

Rouvrez un nouveau terminal, puis lancez la commande suivante pour l'utiliser ::

  nvm use 6

Ensuite, dans le même terminal, clônez le dépôt dédié à cette journée RML8 ::
  
  git clone https://github.com/c-geek/rml8-noeud-specialise.git
  cd rml8-noeud-specialise

Puis installez les dépendances ::

  yarn

Réaliser une première synchronisation de son nœud
-------------------------------------------------

Avant toute chose, il convient de préparer votre nœud en se synchronisant sur une monnaie existante, en l'occurrence TestNet.

Dans votre terminal, toujours depuis le dossier clôné précédemment, lancez ::

  node demo4_dynamique.js sync duniter.org 8999

Votre nœud va alors se synchroniser en récupérant les données de la blockchain TestNet puis la stocker dans le dossier ``~/.config/duniter/rml8``. Tous les fichiers de démonstration (demo1 à demo5) bénéficieront de cette base de données.

Les exercices exemples
----------------------

* Exemple 1 : afficher le bloc courant

  Cet exemple vise simplement à montrer *une* manière d'exploiter le cœur de Duniter à travers son API. Cet exemple affiche dans le terminal le numéro du bloc courant dans la blockchain téléchargée.

  ::

    node demo1_hello_bloc.js

* Exemple 2 : extraction des données avec SQL

  Cet autre exemple part sur le même principe, sauf que l'extraction se fait avec une requête SQL. On invite alors les développeurs à réaliser d'autres requêtes en explorant préalablement la base de données avec des outils tels SQLiteman_.

  ::
  
    node demo2_sql.js

* Exemple 3 : le flux de données du nœud

  Ici, nous nous attardons sur le fait qu'un nœud Duniter peut être vu comme *un flux* par lequel entrent et sortent des données : blocs, identités, certifications, transactions, pairs, etc. Il est possible de capturer ce flux et d'en afficher les détails, voire de les mettre en forme pour produire un flux RSS (solution par ailleurs produite pendant la journée par mmu_man dans le fichier demo_rss.js).

  ::
  
    node demo3_flux.js

* Exemple 4 : afficher les données dans une page web

  Dans la veine des exemples 1 et 2, nous montrons ici qu'il est possible d'afficher les données de la blockchain dans une page web.

  ::
  
    node demo4_dynamique.js

* Exemple 5 : afficher les données en temps réél

  Conclusion logique des 4 exercices précédents, cet exemple montre qu'il est possible d'extraire les données de la blockchain, récupérer le flux de données et d'afficher le tout en temps réel dans une page web.

  ::
  
    node demo5_websocket.js


Exclusivité post-RML8 : 2 nouveaux exemples !
---------------------------------------------

Quand on aime la monnaie libre, on ne compte pas : je vous propose donc **2 nouveaux exemples exclusifs** qui permettront d'explorer la toile de confiance à l'aide du module ``wotb`` intégré à Duniter. Celui-ci est un petit outil axé performances (en C++) pour des tâches d'analyse de la toile.

* Exemple 6 : afficher les points de contrôle

  Les points de contrôle de la toile sont les bords de celle-ci, ils en limitent l'expansion à qui voudrait rejoindre la communauté en étant trop éloigné de ces points. A vous d'exécuter ce script pour découvrir qui sont les points de contrôle actuels.

  ::
  
    node demo6_wotb_sentries.js

* Exemple 7 : découverte de chemins entre 2 individus

  Une tâche que n'effectue pas Duniter, mais qui est indispensable à l'étude d'un individu dont on souhaiterai connaître le lien par rapport à soi ou à une connaissance : l'extraction des chemins de reconnaissance. Voyez par vous-même le résultat en exécutant ce fichier.

  ::
  
    node demo7_wotb_chemins.js


Suite à l'exécution de ces exemples, vous pouvez passer sur le forum_ ou le `salon XMPP`_ pour partager vos réactions ou obtenir des éclaircissements. Puis, si vous vous sentez à l'aise, vous pouvez `aller plus loin`_.

.. _`Monnaie, liberté et (bio)diversité`: https://www.youtube.com/watch?v=LZ9i39uQq8E 
.. _`Introduction aux concepts clés de Duniter`: https://www.youtube.com/watch?v=LZ9i39uQq8E
.. _`Spécialiser son nœud Duniter : partie 1`: https://www.youtube.com/watch?v=DnkQdG2GQBw
.. _`Spécialiser son nœud Duniter : partie 2`: https://www.youtube.com/watch?v=t3F-TPbIsjQ
.. _`la chaîne RML8`: https://www.youtube.com/channel/UCOhCvklzaKqN73njsh3ZnUw
.. _Git: https://git.com
.. _NVM: https://github.com/creationix/nvm#install-script
.. _Yarn: https://yarnpkg.com/en/docs/install
.. _SQLiteman: http://sqliteman.yarpen.cz/
.. _forum: https://forum.duniter.org
.. _`salon XMPP`: https://forum.duniter.fr/t/tutoriel-rejoindre-le-salon-xmpp-de-duniter-org/299
.. _`présentation introductive`: https://www.youtube.com/watch?v=LZ9i39uQq8E&index=4&list=PLMREUqep567tzBzZ4J3cCY-yt2i-dSvJ1&?t=3m45s
.. _`pull request`: https://help.github.com/articles/creating-a-pull-request/
.. _`aller plus loin`: https://github.com/duniter/duniter