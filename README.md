# emoji_scraper

A simple piece of python code that extracts all emojis on a webpage and saves it into a json file. Meant to work on https://www.unicode.org/emoji/charts/full-emoji-list.html

## Installation

python has to be downloaded and installed. Atom was used as text editor.

* [python 3.8.1 Windows x86-64](https://www.python.org/downloads/)
* [atom 1.40.1](https://atom.io/)

## Usage

Run emoji_scraper.py using the script module in atom. You need to paste the webpage into the "emoji_webpage" variable in the file before running it.

emojis.json is the result. It contains a list of emojis. You may just download the file if you are not concerned in any new emoji updates.

## Current status

This is the only version until I have free time to add more features.

1. Adding code that automatically scrapes the website instead of needing manual
2. Making it runnable from command line.

### Atom packages used:

* Hydrogen
* atom-ide-debugger-python
* linter-flake8
* python-autopep8
* python-debugger

### General packages:

* atom-beautify
* busy-signal
* file-icons
* intentions
* minimap
* open_in_cmd
* project-manager
* script

## License

MIT License - see [LICENSE.md](LICENSE.md).
