#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Marcus Tullius Cicero'
SITENAME = u'caelestia.space'
SITEURL = u'http://calestia.space'

PATH = 'content'

TIMEZONE = 'America/Chicago'
THEME = 'pelican-clean-blog'
DEFAULT_LANG = u'en'

COLOR_SCHEME_CSS = 'tomorrow_night.css'
CUSTOM_CSS = 'bootstrap.css'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Markup
# TYPOGRIFY = True

# Enable/Disable Disqus Comments
DISQUS_SITENAME = "caelestia-space"
