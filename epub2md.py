from sys import argv
from os.path import isfile, splitext, exists
from os import mkdir
from ebooklib.epub import read_epub
from markdownify import markdownify

DRY_RUN = 1

if len(argv) <= 1:
    raise SystemExit()

filename = argv[1]

if not isfile(filename):
    raise SystemExit()

if splitext(filename)[1] != '.epub':
    raise SystemExit()

_epub = read_epub(filename)

dirname = '{} - {}'.format(
        _epub.get_metadata('DC', 'creator')[0][0],
        _epub.get_metadata('DC', 'title')[0][0])

if not exists(dirname):
    print('mkdir "{}"'.format(dirname))
    if not DRY_RUN:
        mkdir(dirname)

for xhtml in _epub.get_items_of_media_type('application/xhtml+xml'):
    chapname = splitext(xhtml.get_name())[0]
    print('write "{}/{}.md"'.format(dirname, chapname))
    if not DRY_RUN:
        with open('{}/{}.md'.format(dirname, chapname), 'w') as f:
            f.write(markdownify(xhtml.get_body_content()))
