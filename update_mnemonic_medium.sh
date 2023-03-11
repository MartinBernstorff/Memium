PROJECT="$(dirname "${0}")"

# If Anki.app is not already running, launch it
open -a Anki
echo "🧠 Updating personal mnemonic medium"
cd $PROJECT
source .venv/bin/activate

python application/main.py -r $HOME"/Documents/Life Lessons/" -p "$PROJECT/Life.apkg"

# Send "y" keypress to Anki.app to start sync
osascript -e 'tell application "Anki" to activate' 
osascript -e 'tell application "System Events" to keystroke "y"'


