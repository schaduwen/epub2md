from sys import argv, exit
from os import path, mkdir
from ebooklib import epub
from markdownify import markdownify


if len(argv) <= 1:
    exit()

filename = './{}'.format(argv[1])

if path.isfile(filename) is False:
    exit()

if path.splitext(filename)[1] != '.epub':
    exit()

dirname = path.splitext(path.basename(filename))[0]

if path.exists(dirname):
    exit()

book = epub.read_epub(filename)
xhtml = book.get_items_of_media_type('application/xhtml+xml')

mkdir(dirname)

for xhtml_obj in xhtml:
    if xhtml_obj.get_name() != 'nav.xhtml':
        chapname = path.splitext(xhtml_obj.get_name())[0]
        with open('./{}/{}.md'.format(dirname, chapname), 'w') as f:
            f.write(markdownify(
                xhtml_obj.get_content().replace(
                    b"xml version='1.0' encoding='utf-8'?",
                    b""),
                strong_em_symbol="_"))
