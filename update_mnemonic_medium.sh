#!/bin/zsh
PROJECT="$(dirname "${0}")"
LESSONS_DIR="$HOME/Library/Mobile Documents/iCloud~md~obsidian/Documents/Life Lessons iCloud" 
RUN_EVERY_N_SECONDS=120

# Redirect stdout ( > ) into a named pipe ( >() ) running "tee"
exec > >(tee -a logs/shell_script.log)
# Redirect stderr into stdout ( 2>&1 ), then redirect stdout into a named pipe running "tee"
exec 2>&1

log() {
    # Assign the date and time stamp, in "DD:MM-HH:MM:SS" format
    TIME_STAMP=$(date +"%d/%m %H:%M:%S")
    # Assign the current user
    USER=$(whoami)
    # Write to the file *and* echo to stdout
    mkdir -p logs
    echo "$USER - $TIME_STAMP - $1"
}

while true; do
    # If Anki.app is not already running, launch it
    ANKI_COUNT=$(ps -ax | grep -c "Applications\/Anki.app")
    if (($ANKI_COUNT == 0));
    then
        log "🧠 Launching Anki"
        open -a Anki
    fi

    log "🧠 Updating personal mnemonic medium with scripts in $PROJECT"
    cd $PROJECT
    source .venv/bin/activate

    log "🧠 \"$LESSONS_DIR\""
    python application/main.py -r "$LESSONS_DIR" -p "$PROJECT/Life.apkg"

    # Send "y" keypress to Anki.app to start sync
    # osascript -e 'tell application "Anki" to activate' 
    # osascript -e 'tell application "System Events" to keystroke "y"'
    log "🧠 Finished syncing"
    sleep $RUN_EVERY_N_SECONDS
done

