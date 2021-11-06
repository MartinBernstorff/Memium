#!/bin/bash
path=$HOME"/Dropbox/Projects/Programming/Git/personal_mnemonic_medium"

$HOME/Dropbox/Projects/Programming/Git/Bear-Markdown-Export-master/update_bear_markdown.sh

/Library/Frameworks/Python.framework/Versions/3.7/bin/python3 $path/main.py -r $HOME"/Library/Mobile Documents/iCloud~md~obsidian/Documents/Life Lessons/" -p "$path/Life.apkg"

open -a "Anki" "$path/Life.apkg"
sleep 1

$HOME/Dropbox/Projects/Programming/Git/Bear-Markdown-Export-master/update_bear_markdown.sh