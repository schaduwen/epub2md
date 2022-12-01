# epub2md

Converts xhtml files within an epub to md. Originally written for epub's downloaded from https://fichub.net.

depends on:
- Ebooklib
- markdownify

```
python3 epub2md.py path/to/file.epub
```

The line above, in the current working directory, creates a directory containing md files.

options:
- DRY_RUN : epub2md does everything apart from actually creating the directory and files.

future goals (unsure):
- rename the md files produced
- ignore navigation xhtml
