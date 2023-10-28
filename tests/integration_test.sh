docker build . -t personal-mnemonic-medium:latest -f Dockerfile
docker volume create ankidecks

INPUT_DIR=$HOME/input/
OUTPUT_DIR=$HOME/ankidecks/integration_test

mkdir -p $INPUT_DIR
echo -e "Q. Question here\nA. Answer!" >> $HOME/input/test.md

docker run -itd \
  -v $INPUT_DIR:/input \
  -v $OUTPUT_DIR:/output \
  --restart unless-stopped \
  personal-mnemonic-medium \
  python application/main.py /input/ $OUTPUT_DIR \
  --watch \
  --no-use-anki-connect

echo "Waiting for Anki package to be created..."
echo "Waiting for 15 seconds..."
for i in {1..15} ; do
  echo "$i"
  sleep 1
done

FILE="$OUTPUT_DIR/deck.apkg"
if [ -f "$FILE" ]; then
    echo "File exists."
    
    # Get the file modification time in seconds from epoch
    FILE_TIMESTAMP=$(stat -c %Y "$FILE")

    # Get the current time in seconds from epoch
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
