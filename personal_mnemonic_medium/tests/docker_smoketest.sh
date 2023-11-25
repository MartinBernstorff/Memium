set -e
docker build . -t personal-mnemonic-medium:latest -f Dockerfile
docker volume create ankidecks

INPUT_DIR=$HOME/input/
HOST_OUTPUT_DIR=$HOME/ankidecks/smoketest
HOST_OUTPUT_FILE=$HOST_OUTPUT_DIR/deck.apkg
ANKICONNECT_SYNC_APKG=/output/deck.apkg

mkdir -p $INPUT_DIR
echo -e "Q. Question here\nA. Answer!" >> $HOME/input/test.md

# Delete the output file if it already exists, to ensure that we are testing the latest version
rm -f $HOST_OUTPUT_FILE

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
else
    echo "File does not exist." >&2
    exit 1
fi
