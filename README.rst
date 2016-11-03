Reproduire le blog
==================

:date: 2016-11-01 19:08

Première installation
---------------------

1. Créer un environnement virtuel python ::

    virtualenv ~/virtualenvs/pelican && cd ~/virtualenvs/pelican && source bin/activate

2. Clôner ce dépôt ::

    git clone https://github.com/c-geek/blog && cd blog

3. Installer ``pelican`` ::

    pip install pelican pelican-youtube

4. Ajouter le theme ``medius`` a pelican ::

    pelican-themes --install medius/

5. Produire le blog ::

    ./develop_server.sh start 8056

Le blog est alors disponible à l'adresse http://localhost:8056

Reprendre la dernière installation
----------------------------------

1. Rejoindre l'environnement virtuel python ::

    cd ~/virtualenvs/pelican && source bin/activate

2. Produire le blog ::

    ./develop_server.sh start 8056

Le blog est alors disponible à l'adresse http://localhost:8056
