#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'cgeek'
SITENAME = u'cblog'
SITEURL = u'http://localhost:8556'

PATH = 'content'
THEME = "medius"

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images']

MEDIUS_WIDGETS = ['categories','tags']

MEDIUS_AUTHORS = {
  'cgeek': {
    'description': """
      Fondateur du logiciel Duniter, développeur acharné. Aspirant à une économie libre.
    """,
    'image': 'https://forum.duniter.org/user_avatar/forum.duniter.org/cgeek/120/279_1.png',
    'links': (('github', 'https://github.com/c-geek'),
              ('twitter', 'https://twitter.com/twicedd'),
              ('asterisk', 'https://diaspora-fr.org/people/f9d13420f9ff013197aa01beea1f31e2'),
              ('envelope', 'mailto:admin@duniter.org'),)
  }
}

MEDIUS_CATEGORIES = {
  'Evénements': {
    'description': 'Passés, présents et à venir !',
    'thumbnail': '/images/event.png'
  },
  'Développement': {
    'description': 'Bouts de code à tester',
    'thumbnail': '/images/coding.png'
  }
}

PLUGINS = [
  'pelican_youtube',
]

# Blogroll
LINKS = (('duniter.org', 'https://duniter.org/'),
         ('creationmonetaire.info', 'http://creationmonetaire.info/'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/twicedd'),
          ('Diaspora*', 'https://diaspora-fr.org/people/f9d13420f9ff013197aa01beea1f31e2'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
