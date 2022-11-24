from sys import argv
from os import path, mkdir
from ebooklib import epub
from markdownify import markdownify


if len(argv) <= 1:
    raise SystemExit()

filename = argv[1]

if path.isfile(filename) is False:
    raise SystemExit()

if path.splitext(filename)[1] != '.epub':
    raise SystemExit()

_epub = epub.read_epub(filename)
xhtmls = _epub.get_items_of_media_type('application/xhtml+xml')

dirname = path.splitext(path.basename(filename))[0]

if path.exists(dirname) is False:
    mkdir(dirname)

for xhtml in xhtmls:
    chapname = path.splitext(xhtml.get_name())[0]
    if chapname != 'nav':
        with open('./{}/{}.md'.format(dirname, chapname), 'w') as f:
            f.write(markdownify(xhtml.get_body_content()))
