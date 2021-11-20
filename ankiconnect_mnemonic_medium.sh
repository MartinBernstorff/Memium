#!/bin/bash
path=$HOME"/Dropbox/Projects/Programming/Git/personal_mnemonic_medium"

$HOME/Dropbox/Projects/Programming/Git/Bear-Markdown-Export-master/update_bear_markdown.sh 

cd $path

python3 personal_mnemonic_medium/primary.py -r $HOME"/Library/Mobile Documents/iCloud~md~obsidian/Documents/Life Lessons/" -p "Life.apkg"
# sleep 1

# $HOME/Dropbox/Projects/Programming/Git/Bear-Markdown-Export-master/update_bear_markdown.sh