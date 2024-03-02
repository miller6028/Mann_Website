#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import datetime
import pathlib
import re

from markdown_include.include import MarkdownInclude

# The Pelican settings are documented here:
#   https://docs.getpelican.com/en/stable/settings.html
# and the Flex theme's settings are documented here:
#   https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings

# Pelican general site settings
# Depending on the scope of changes, you may want to change "westlanetv.org"
# in the SITEURL to wherever the staging site is so links point within the
# staging site.
SITEURL = 'https://westlanetv.org'
SITENAME = 'West Lane Translator Inc.'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# The Flex theme can accommodate our non-blog site well and is MIT license
THEME = 'Flex'

# Flex general site settings
SITETITLE = SITENAME
SITESUBTITLE = 'Serving the Central Oregon Coast since 1959'
SITEDESCRIPTION = \
    "Information about West Lane Translator's HDTV and FM translators."
AUTHOR = 'West Lane Translator Inc.'
COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = '2011-' + str(datetime.datetime.today().year)
ROBOTS = 'index, follow'
FAVICON = SITEURL + '/images/favicon.ico'
SITELOGO = SITEURL + '/images/logo.jpg'
# Flex Dark Mode settings per:
#   https://github.com/alexandrevicenzi/Flex/wiki/Dark-Mode
THEME_COLOR = 'light'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True  # Uses JavaScript

# Enable some Markdown extensions.  The list of available extensions and
# documentation for them is available here:
#   https://python-markdown.github.io/extensions/
# For completeness, the basic Markdown syntax is documented here:
#   https://daringfireball.net/projects/markdown/syntax
MARKDOWN = {
    'extensions': {
        'markdown.extensions.attr_list',
        'markdown.extensions.extra',
        'markdown.extensions.meta',
        'markdown.extensions.smarty',
        'markdown.extensions.toc',
        MarkdownInclude({'base_path': 'content'})
    },
    'output_format': 'html5'
}

# I don't feel compelled to tell the world our site was built with
# Pelican and Flex.  This relies on local changes to Flex.
ALT_CREDIT=''

# By default, the links point to the main page heading so that the top
# menu isn't seen unless you scroll or if the page happens to be
# smaller than your browser window.  Disable that.
DISABLE_URL_HASH = True

# Output our canonical URL.
REL_CANONICAL = True

# Tell the world via the JSON-LD and Open Graph types that we are a
# website and not a blog.  These rely on local changes to Flex.
OG_TYPE = 'website'
JSONLD_TYPE = 'WebPage'

# This is a simple website and not a blog so disable all the bloggy stuff
DIRECT_TEMPLATES = []
ARCHIVES_SAVE_AS = ''
ARTICLE_PATHS = []
ARTICLE_SAVE_AS = ''
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
AUTHOR_SAVE_AS = ''
CATEGORY_FEED_ATOM = None
CATEGORY_SAVE_AS = ''
DEFAULT_PAGINATION = False
DISPLAY_CATEGORIES_ON_MENU = False
DRAFT_SAVE_AS = ''
FEED_ALL_ATOM = None
INDEX_SAVE_AS = ''
TAG_SAVE_AS = ''
TRANSLATION_FEED_ATOM = None
# We don't have SOCIAL nor articles so turn on this local change to
# prevent links to font-awesome being emitted.
FONT_AWESOME_UNNEEDED = True

# The site is small, so rebuild it from scratch every time.
DELETE_OUTPUT_DIRECTORY = False
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = False

# Tell Pelican where things come from and go to.
PATH = 'content'  # Keep content separate from how to build.
PAGE_PATHS = ['pages']  # Where to look in content subdirectory for our pages.
STATIC_PATHS = ['images', 'pdfs', 'extra']  # Copy things from these to output.
OUTPUT_PATH = 'output/'  # Where to put the output.
PAGE_URL = '{slug}.html'  # Output the HTML at the root instead of in pages/
PAGE_SAVE_AS = '{slug}.html'

# The configuration of the menus is custom and somewhat hacky.

# Pages can be placed in one of three different menus of links:
#   1) at the top of the page,
#   2) on the left side of the page, or
#   3) at the bottom of the page by the copyright (via a local change).

# The menu at the top of the page is enabled with:
MAIN_MENU = True
# and the items to be put in it are defined via MENUITEMS which will
# be set by Python code that follows.

# The items in the menu at the bottom of the page are defined via
# FOOTERMENUITEMS (a local change).  Defining it also enables it.
# FOOTERMENUITEMS will also be set via the Python code that follows.

# Each page Markdown file has our own locally defined 'Menu' metadata.
# It is used for two purposes.  The first is to construct the
# MENUITEMS and FOOTERMENUITEMS lists.  The second is to define the
# order of the pages within each menu:
PAGES_SORT_ATTRIBUTE = 'menu'

# The following code examines the 'Menu' metadata of each Markdown
# page.  If it starts with 'Top', the page will be placed in the menu
# at the top of the page.  Conversely, if the 'Menu' metadata starts
# with 'Bottom', the page will be placed in the menu at the bottom of
# the page.  Otherwise, the page will be placed in the menu at the
# left side of the page.  By convention, we start the 'Menu' metadata
# with 'Side' for those pages.  Note that the pages to be placed in
# the top or bottom menus should also set the 'Status' metadata to be
# 'Hidden' to prevent the page from also appearing in the left side
# menu.  Normally that prevents the page from being crawled but a
# local change (if enabled) allows it:
CRAWL_HIDDEN = True

# We'll use the default SLUG_REGEX_SUBSTITUTIONS for generating the slug.
SLUG_REGEX_SUBSTITUTIONS = [
    (r'[^\w\s-]', ''), # remove non-alphabetical/whitespace/'-' chars
    (r'(?u)\A\s*', ''), # strip leading whitespace
    (r'(?u)\s*\Z', ''), # strip trailing whitespace
    (r'[-\s]+', '-'), # reduce multiple whitespace or '-' to single '-'
]

# Build up a list of the Markdown pages.  Each element of the list is
# a tuple containing:
#   1) the value of the 'Menu' metadata,
#   2) the value of the 'Title' metadata, and
#   3) the URL of the page (which makes assumptions about slugification)
path_path = pathlib.Path(PATH)
pages_path = path_path / 'pages'
pages_menu_info = []
for md in pages_path.glob('**/*.md'):
    title = ''
    menu = ''
    with md.open() as f:
        while True:
            line = f.readline()
            if not line or ':' not in line:
                break
            if line.lower().startswith('title:'):
                title = line[6:].strip()
            if line.lower().startswith('menu:'):
                menu = line[5:].strip()
    assert title
    if menu:
        slug = title
        for pattern, repl in SLUG_REGEX_SUBSTITUTIONS:
            slug = re.sub(pattern, repl, slug)
        slug = slug.lower()
        page_url = f'{SITEURL}/{slug}.html'
        pages_menu_info.append((menu, title, page_url))

# Now iterate through the list of Markdown pages to form MENUITEMS and
# FOOTERMENUITEMS:
MENUITEMS = []
FOOTERMENUITEMS = []
for menu, title, page_url in sorted(pages_menu_info):
    if menu.lower().startswith('top'):
        MENUITEMS.append((title, page_url))
    if menu.lower().startswith('bottom'):
        FOOTERMENUITEMS.append((title, page_url))
# Done!

# We want redirects of URLs from the old site to go to the new site
# URLs.  This is done with .htaccess files in subdirectories on the
# website as needed.  The source for these files is
# content/extra/htaccess* but we need Pelican to copy them to the
# right place in the output.  This is done via EXTRA_PATH_METADATA.
# Instead of building that manually, the following code automatically
# builds EXTRA_PATH_METADATA from the list of extra/htaccess* files.
# As an example, extra/htaccess_About will end up in About/.htaccess
# in the output.
EXTRA_PATH_METADATA = {
    'extra/google91b9f44816fd80c5.html': {
        'path': 'google91b9f44816fd80c5.html'
    }
}
extra_path = path_path / 'extra'
for hta in extra_path.glob('htaccess*'):
    rel_hta = pathlib.Path(*hta.parts[-2:])
    hta_loc = hta.name[len('htaccess'):]
    if not hta_loc:
        hta_loc = '.htaccess'
    else:
        assert hta_loc[0] == '_'
        hta_loc = hta_loc[1:] + '/.htaccess'
    EXTRA_PATH_METADATA[str(rel_hta)] = {'path': hta_loc}
