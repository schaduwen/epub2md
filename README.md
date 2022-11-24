# epub2md

Written for epub files downloaded from https://fichub.net

depends on:
- ebooklib
- beautifulsoup4
- markdownify

```
python3 epub2md.py path/to/file.epub
```

The line above, in the current working directory, creates a directory containing each story chapter as a md file. A file containing information about the story, metadata.ini, is additionally created.

fichub supported sites:
- SpaceBattles, SufficientVelocity, QuestionableQuesting (XenForo)
- FanFiction.net, FictionPress
- Archive Of Our Own
- Harry Potter Fanfic Archive
- Sink Into Your Eyes
- AdultFanfiction.org
- Worm, Ward
