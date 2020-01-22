# emoji_scraper

A simple piece of python code that extracts all unique emojis on a webpage and saves them into a json file. Meant to work on https://www.unicode.org/emoji/charts/full-emoji-list.html

## Requirements

* Python 3

## Installation

python has to be downloaded and installed. Atom was used as text editor.

* [python 3.8.1 Windows x86-64](https://www.python.org/downloads/)
* [atom 1.40.1](https://atom.io/)

### Atom packages used:

* script

## Usage

Run emoji_scraper.py using the script module in atom. You need to paste the webpage into the "emoji_webpage" variable in the file before running it.

emojis.json is the result. It contains a list of emojis. You may just download the file if you are not concerned in any new emoji updates.

### FAQ

> How do I use a list of emojis?

This code was written to in order to get a regex pattern that can match all emojis. To get such a pattern, use:

```
pattern = f'[{"".join(emojis)}]'
```

> I get UnicodeEncodeError: 'charmap' codec can't encode character...

Python is not running on utf-8 encoding on your computer. Use the following code to fix the error:

```
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
```

## Current status

This is the only version until I have free time and decide to add more features.

1. Adding code that automatically scrapes the website instead of needing manual copy and paste.
2. Making it runnable from command line.

## License

MIT License - see [LICENSE.md](LICENSE.md).
