PROJECT=$HOME"/Dropbox/Projects/Programming/Git/personal_mnemonic_medium"

$HOME/Dropbox/Projects/Programming/Git/Bear-Markdown-Export-master/update_bear_markdown.sh

cd $PROJECT

source .venv/bin/activate

# If Anki.app is not already running, launch it
if [ ! -n "$(ps -A | grep Anki)" ]; then
    open -a Anki
    sleep 3
fi

python application/main.py -r $HOME"/Library/Mobile Documents/iCloud~md~obsidian/Documents/Life Lessons/" -p "$PROJECT/Life.apkg"

# Send "y" keypress to Anki.app to start sync
osascript -e 'tell application "Anki" to activate' 

# Send the letter y as keycode to Anki.app
osascript -e 'tell application "System Events" to keystroke "y"'


