#!/usr/bin/env python
# -*- coding: utf-8 -*- #

""" Pelican configuration file """

from __future__ import unicode_literals
from collections import namedtuple
import datetime
import os
import pathlib
import re
import shutil

#saa from markdown_include.include import MarkdownInclude

# The Pelican settings are documented here:
#   https://docs.getpelican.com/en/stable/settings.html
# and the Flex theme's settings are documented here:
#   https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings

# Pelican general site settings
# Depending on the scope of changes, you may want to change "westlanetv.org"
# in the SITEURL to wherever the staging site is so links point within the
# staging site.
SITEURL = 'https://mann-website.pages.dev'
SITENAME = 'Ronald G. Mann Building LLC'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# The Flex theme can accommodate our non-blog site well and is MIT license
THEME = 'Flex'

# Flex general site settings
SITETITLE = SITENAME
SITESUBTITLE = 'Specializing in complex site builds'
SITEDESCRIPTION = \
    "Information about Ronald G. Mann Building LLC."
AUTHOR = 'Ronald G. Mann Building LLC'
COPYRIGHT_NAME = AUTHOR
FIRST_YEAR = '2024'
CURRENT_YEAR = str(datetime.datetime.today().year)
if CURRENT_YEAR == FIRST_YEAR:
    COPYRIGHT_YEAR = CURRENT_YEAR
else:
    COPYRIGHT_YEAR = f'{FIRST_YEAR}-{CURRENT_YEAR}'
ROBOTS = 'index, follow'
FAVICON = SITEURL + '/images/favicon.ico'
SITELOGO = SITEURL + '/images/mnronaldgmannbuilding.png'
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
 # saa       MarkdownInclude({'base_path': 'content'})
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
STATIC_PATHS = ['images']  # Copy things from these to output.
OUTPUT_PATH = 'output/'  # Where to put the output.
PAGE_URL = '{slug}.html'  # Output the HTML at the root instead of in pages/
PAGE_SAVE_AS = '{slug}.html'

# The configuration of the menus is custom and somewhat hacky.

# Pages can be placed in one of three different menus of links:
#   1) at the top of the page,
#   2) on the left side of the page, or
#   3) at the bottom of the page by the copyright (via a local change).

# The menu at the top of the page is enabled with:
# MAIN_MENU = True
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
    TITLE = ''
    MENU = ''
    with md.open() as f:
        while True:
            line = f.readline()
            if not line or ':' not in line:
                break
            if line.lower().startswith('title:'):
                TITLE = line[6:].strip()
            if line.lower().startswith('menu:'):
                MENU = line[5:].strip()
    assert TITLE
    if MENU:
        slug = TITLE
        for pattern, repl in SLUG_REGEX_SUBSTITUTIONS:
            slug = re.sub(pattern, repl, slug)
        slug = slug.lower()
        page_url = f'{SITEURL}/{slug}.html'
        pages_menu_info.append((MENU, TITLE, page_url))

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

# OurHomes.md is built automatically from the paths to images
ImageGroup = namedtuple('ImageGroup', ['subdirectory', 'description'])
IMAGE_GROUPS = (
    ImageGroup('Current', 'Home Construction In Progress'),
    ImageGroup('Sale', 'Completed Homes Available to Buy'),
    ImageGroup('Vacant', 'Vacant Land Ready for Your Design'),
    ImageGroup('Previous', 'Previous Home Builds for Other Satisfied Clients')
)
OURHOME_TEMPLATE = 'content/pages/OurHomes.template'
OURHOME_MD = 'content/pages/OurHomes.md'
shutil.copyfile(OURHOME_TEMPLATE, OURHOME_MD)
images_path = path_path / 'images'
properties_path = pages_path / 'Properties'
shutil.rmtree(properties_path, ignore_errors=True)
os.makedirs(properties_path)
with open(OURHOME_MD, 'a', encoding='ascii') as ourhome_md:
    for subdirectory, description in IMAGE_GROUPS:
        print(f'\n### {description}', file=ourhome_md)
        print('| Location | Address | Lot Size| Additional Information | | |',
              file=ourhome_md)
        print('| :--- | :--- | :---| :--- | :---: | ---- |', file=ourhome_md)
        dir_path = images_path / subdirectory
        for property_dir in sorted(dir_path.glob('*')):
            property_attrs = property_dir.name.split('^')
            num_property_attrs = len(property_attrs)
            assert 4 <= num_property_attrs <= 5
            address, location, lot_size, info = property_attrs[:4]
            if num_property_attrs == 5:
                listing_url = (f'[Listing link](https://tinyurl.com/'
                               f'{property_attrs[4]}) |')
            else:
                listing_url = ''
            property_md = properties_path / (address + '.md')
            property_link = property_md.relative_to(pages_path)

            FIRST_IMG_NAME = FIRST_IMG_PATH = None
            with open(property_md, 'w', encoding='ascii') as prop_file:
                print(f'Title: {address}\nStatus: Hidden\n', file=prop_file)
                for img in sorted(property_dir.glob('*')):
                    img_name = img.name
                    img_path = f'{{static}}/{img.relative_to(path_path)}'
                    if not FIRST_IMG_NAME:
                        FIRST_IMG_PATH = img_path
                        FIRST_IMG_NAME = img_name
                    print(f'![{img_name}]({img_path})\n', file=prop_file)

            print(f'| [{location}]({{filename}}{property_link}) '
                  f'| [{address}]({{filename}}{property_link}) '
                  f'| [{lot_size}]({{filename}}{property_link}) '
                  f'| [{info}]({{filename}}{property_link}) '

                  f'| <div style="width:100px"> [![{FIRST_IMG_NAME}]'
                  f'({FIRST_IMG_PATH})]({{filename}}{property_link}) </div> '
                  f'| {listing_url} |',
                  file=ourhome_md)
