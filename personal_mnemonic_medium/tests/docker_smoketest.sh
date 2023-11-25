set -e
docker build . -t personal-mnemonic-medium:latest -f Dockerfile
docker volume create ankidecks

INPUT_DIR=$HOME/input/
HOST_OUTPUT_DIR=$HOME/ankidecks/smoketest
HOST_OUTPUT_FILE=$HOST_OUTPUT_DIR/deck.apkg
ANKICONNECT_SYNC_APKG=/output/deck.apkg

mkdir -p $INPUT_DIR
echo -e "Q. Question here\nA. Answer!" >> $HOME/input/test.md

docker run -i \
  -v $INPUT_DIR:/input \
  -v $HOST_OUTPUT_DIR:/output \
  --restart unless-stopped \
  personal-mnemonic-medium \
  python personal_mnemonic_medium/presentation/cli.py \
  /input/ \
  $ANKICONNECT_SYNC_APKG \
  $HOST_OUTPUT_DIR \
  --no-watch \
  --no-use-anki-connect

echo "Checking if file exists at $HOST_OUTPUT_FILE"

if [ -f "$HOST_OUTPUT_FILE" ]; then
    echo "File exists."
    
    FILE_TIMESTAMP=$(stat -c %Y "$HOST_OUTPUT_FILE")
    CURRENT_TIMESTAMP=$(date +%s)

    # Calculate the age of the file by subtracting file's timestamp from current timestamp
    FILE_AGE=$(($CURRENT_TIMESTAMP - $FILE_TIMESTAMP))

    # Check if file age is less than 1 minute (60 seconds)
    if [ $FILE_AGE -lt 60 ]; then
        echo "File age is less than 1 minute."
    else
        echo "File age is more than 1 minute." >&2
        exit 1
    fi
else
    echo "File does not exist." >&2
    exit 1
fi
