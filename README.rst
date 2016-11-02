Installation du blog
====================

:date: 2016-11-01 19:08

> Les opérations sont réalisées en ``root``.

1. Clôner ce dépôt ::

    mkdir -p /opt/blog
    git clone https://github.com/c-geek/blog /opt/blog
    cd /opt/blog

2. Installer ``pelican`` ::

    sudo pip install pelican

3. Ajouter le theme ``medius`` a pelican ::

    sudo pelican-themes --install medius/

4. Produire le site web résultat ::

    pelican content/ -s publishconf.py

Le site web est alors consultable comme n'importe quel site HTML, en commençant par le fichier ``index.html``.
