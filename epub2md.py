from sys import argv
from os import path, mkdir
from configparser import ConfigParser
from ebooklib import epub
from bs4 import BeautifulSoup
from markdownify import markdownify

SECTION_NAME = 'METADATA'
EXCLUDE = ['introduction.xhtml', 'nav.xhtml']

if len(argv) <= 1:
    raise SystemExit()

filename = argv[1]

if path.isfile(filename) is False:
    raise SystemExit()

if path.splitext(filename)[1] != '.epub':
    raise SystemExit()

_epub = epub.read_epub(filename)
html = _epub.get_item_with_href('introduction.xhtml').get_body_content()

ini = ConfigParser()
ini.add_section(SECTION_NAME)
for i, tag in enumerate(BeautifulSoup(html, 'html.parser')):
    if i == 0:
        booktitle = tag.text
        ini.set(SECTION_NAME, 'title', booktitle)
    elif i == 2:
        bookauthor = tag.text.replace('By: ', '')
        ini.set(SECTION_NAME, 'author', bookauthor)

dirname = '{} - {}'.format(bookauthor, booktitle)

if path.exists(dirname) is False:
    mkdir(dirname)

with open('{}/metadata.ini'.format(dirname), 'w') as f:
    ini.write(f)

xhtmls = _epub.get_items_of_media_type('application/xhtml+xml')
for xhtml in xhtmls:
    filename = xhtml.get_name()
    if filename not in EXCLUDE:
        chapname = path.splitext(filename)[0]
        with open('{}/{}.md'.format(dirname, chapname), 'w') as f:
            f.write(markdownify(xhtml.get_body_content()))
