# emoji_scraper

A simple piece of python code that extracts all unique emojis on a webpage and saves them into a json file. Meant to work on https://www.unicode.org/emoji/charts/full-emoji-list.html

Flag emojis comprise two unique characters, so all letter emojis are removed from the list, and all possible two letter combinations of letter emojis are added to it to come up with a complete emoji list. Take note of this if attempting to use the code on a different webpage.

Alternative ways of getting a list of all emojis include using emoji.UNICODE_EMOJI from the [emoji](https://github.com/alexandrevicenzi/emojis) library, but I found that it captures #, numbers and various other characters I don't consider emojis, and was not suitable for my purposes. That was how this mini 'project' was born.

## Requirements

* Python 3

## Installation

python has to be downloaded and installed. Atom was used as text editor.

* [python 3.8.1](https://www.python.org/downloads/)
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
pattern = '|'.join(emojis)
```

> I get UnicodeEncodeError: 'charmap' codec can't encode character...

python is not running on utf-8 encoding on your computer. Use the following code to fix the error:

```
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
```

## Current status and issues

### Status

This is the only version until I have free time and decide to add more features.

1. Adding code that automatically scrapes the website instead of needing manual copy and paste.
2. Making it runnable from command line.

### Known issues

1. The approach to extracting emojis brute forces all possible two letter combinations of letter emojis in order to capture flag emojis. However, it also meant that non-existant letter combinations are added to the list.

## License

MIT License - see [LICENSE.md](LICENSE.md).
