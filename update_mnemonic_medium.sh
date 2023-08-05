PROJECT="$(dirname "${0}")"
LESSONS_DIR="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Life Lessons iCloud" 
RUN_EVERY_N_SECONDS=120

while true; do
    # If Anki.app is not already running, launch it
    ANKI_COUNT=$(ps -ax | grep -c "Applications\/Anki.app")
    if (($ANKI_COUNT == 0));
    then
        echo "🧠 Launching Anki"
        open -a Anki
    fi

    echo "🧠 Updating personal mnemonic medium with scripts in $PROJECT"
    cd $PROJECT
    source .venv39/bin/activate

    echo "🧠 \"$LESSONS_DIR\""
    python application/main.py -r "$LESSONS_DIR" -p "$PROJECT/Life.apkg"

    # Send "y" keypress to Anki.app to start sync
    # osascript -e 'tell application "Anki" to activate' 
    # osascript -e 'tell application "System Events" to keystroke "y"'
    echo "🧠 Finished syncing"
    sleep $RUN_EVERY_N_SECONDS
done

