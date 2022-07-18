PROJECT=$HOME"/Dropbox/Projects/Programming/Git/personal_mnemonic_medium"

$HOME/Dropbox/Projects/Programming/Git/Bear-Markdown-Export-master/update_bear_markdown.sh

cd $PROJECT

source .venv/bin/activate

python application/main.py -r $HOME"/Library/Mobile Documents/iCloud~md~obsidian/Documents/Life Lessons/" -p "$PROJECT/Life.apkg"