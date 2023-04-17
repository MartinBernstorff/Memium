PROJECT="$(dirname "${0}")"

# If Anki.app is not already running, launch it
open -a Anki
echo "🧠 Updating personal mnemonic medium"
cd $PROJECT
source .venv39/bin/activate

python application/main.py -r $HOME"/Library/Mobile Documents/iCloud~md~obsidian/Documents/Life Lessons iCloud" -p "$PROJECT/Life.apkg"

# Send "y" keypress to Anki.app to start sync
osascript -e 'tell application "Anki" to activate' 
osascript -e 'tell application "System Events" to keystroke "y"'


