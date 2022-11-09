# epub2md

depends on:
- ebooklib
- markdownify

Written for epub files downloaded from https://fichub.net/, should work for other epub's provided the file structure is similar.

```
python3 epub2md.py path/to/file.epub
```
The line above, in the current working directory, creates a directory containing each story chapter as a md file. As I have yet to create some form of metadata handling, introduction.md is additionally created.
