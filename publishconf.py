#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

AUTHOR = u'cgeek'
SITENAME = u'cblog'
SITEURL = 'https://blog.cgeek.fr'
RELATIVE_URLS = False
TIMEZONE = 'Europe/Paris'

PATH = 'content'
THEME = "medius"
DEFAULT_LANG = u'fr'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

STATIC_PATHS = ['images']

MEDIUS_WIDGETS = ['categories','tags','soutien']

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

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
