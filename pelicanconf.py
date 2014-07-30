#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Lance Chen'
SITENAME = u"Lance's blog"
SITEURL = ''

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = ''

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('', ''),)

# Social widget
#SOCIAL = (('', ''),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins', ]
PLUGINS = ['pelican_gist', 'render_math']

MARKUP = ('mkd',)

THEME = './themes/gum/'

GITHUB_URL = 'https://github.com/Lance0312'
TWITTER_URL = 'https://twitter.com/Lance0312'
DISQUS_SITENAME = 'bloglancetw'
ADDTHIS_PROFILE = 'ra-53d870897d773f31'

MENUITEMS = [('Archives','/archives.html'),]

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
