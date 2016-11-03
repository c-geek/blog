RML8 : Journée 1
################

:date: 2016-11-02 14h50
:tags: RML, RML8, monnaie libre, duniter
:slug: rml8-journee1
:authors: cgeek
:category: Evénements
:thumbnail: /images/rml8.png

Je participerai aux `8èmes Rencontres des Monnaies Libres`_ a Toulouse du 17 au 20 Novembre 2016, et animerai en grande partie la journée du jeudi 17 dédiée au développement du cœur de Duniter. Mon intervention se situera de 10h30 à 12h00, puis de 14h00 à 18h00.

Nous aurons donc 5h30 pour coder et aborder la manipulation du code source du cœur.

Thème des RML8 : spécialisez votre nœud !
-----------------------------------------

Voici donc le thème que j'ai choisi pour ces RML à Toulouse : *spécialiser* un nœud Duniter.

Qu'est-ce donc ? Un nœud spécialisé est un nœud Duniter dont on a *étendu* les fonctionnalités. Par exemple, Remuniter_ est un nœud spécialisé. On le retrouve dans la liste des pairs du réseau comme n'importe quel autre, pourtant il possède une fonctionnalité bien à lui : rémunérer automatiquement les émetteurs de blocs avec de la monnaie qu'on lui a envoyée.

.. image:: /images/rml8-remuniter.png

Cette spécialisation est intéressante à double titre pour ces rencontres :

* Car les prochains grands développements de Duniter graviteront à coup sûr sur ce principe, le cœur arrivant à maturité.
* Spécialiser un nœud est une excellente façon d'approcher le cœur, car on le manipule directement.

Spécialiser un nœud sera donc, pour les participants, l'occasion *pour la toute première fois aux RML* de manipuler le code interne de Duniter et d'en comprendre avec aisance le fonctionnement. Car si réalité *le cœur est relativement simple*, il est important de donner explicitement les clés de lecture pour une appropriation rapide.

Vers l'ouverture du code de Duniter
-----------------------------------

Car le but de ces manipulations, outre le fait de réaliser des nœuds qui réaliseront ce que vous leur demanderez, est surtout *d'ouvrir le code de Duniter* à ceux qui souhaitent se l'approprier.

Un code libre ne l'est vraiment que relativement à ses utilisateurs, et si ces derniers ne sont pas en mesure de le faire (au moins les développeurs), alors on ne peut pas dire d'un logiciel qu'il est libre, peu importe sa licence.

Je souhaite donc que les participants puissent s'approprier le code, son organisation, ses concepts et ses modes d'utilisation. Ces RML8 seront un premier pas en ce sens.

.. code-block:: js

  /***********************************
  * Exemple de code de nœud spécialisé
  ************************************/

  const duniter = require('duniter');

  // Créer un nœud
  const node = duniter({ memory: true });

  // Se connecter à TestNet
  yield node.sync('duniter.org:8999');
  
  // Démarrer son nœud et le rendre visible du réseau
  yield node.start();
  
  const blocCourant = yield node.dal.getCurrentBlock();
  console.log('Bloc courant = #%s !', blocCourant.number); // Bloc courant = #51956 !

Vous y découvrirez donc :

* les composants principaux du logiciel et leur agencement
* comment y accéder *directement* et en faire ce que vous souhaitez

Préparez-vous !
---------------

Cette initiation au code **est réservée aux informaticiens**, de préférence des développeurs, et *peu importe votre langage de prédilection*. Car même si Duniter est écrit en JavaScript_ (plus précisément, en Node.js), cette initiation sera largement guidée et préparée pour que vous n'ayez qu'à jouer avec le code. Le but n'étant pas de faire de vous des développeurs JavaScript chevronnés.

Il sera également important `que vous suiviez le tutoriel de préparation avant de venir`_ : je mettrai à disposition celui-ci *1 semaine avant les RML8*, soit le 10 Novembre 2016. Celui-ci contiendra le code source utilisé pendant les RML8, ainsi que les instructions d'installation.

    L'installation est très simple et rapide pour les utilisateurs de Linux/Mac. Pour les Windowsiens, c'est plus long. **Prenez-vous y à l'avance**.

Au plaisir, donc, de vous retrouver pour cette journée de code !

.. _`8èmes Rencontres des Monnaies Libres`: http://www.monnaielibreoccitane.org/rml8/
.. _Remuniter: http://remuniter.cgeek.fr
.. _JavaScript: https://www.javascript.com/
.. _`que vous suiviez le tutoriel de préparation avant de venir`: https://github.com/c-geek/rml8-noeud-specialise
