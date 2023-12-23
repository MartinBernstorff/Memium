set -e
docker build . -t personal-mnemonic-medium:latest -f Dockerfile
docker volume create ankidecks

INPUT_DIR=$HOME/input/
APKG_OUTPUT_DIR=/output/
HOST_APKG_DIR=$HOME/ankidecks/smoketest

mkdir -p $INPUT_DIR
echo -e "Q. Question here\nA. Answer!" >> $HOME/input/test.md

# Delete the output file if it already exists, to ensure that we are testing the latest version
rm -f $HOST_OUTPUT_FILE

docker run -i \
  -e HOST_INPUT_DIR=$INPUT_DIR \
  -v $INPUT_DIR:/input \
  -v $HOST_APKG_DIR:/output \
  --restart unless-stopped \
  personal-mnemonic-medium \
  personal_mnemonic_medium \ # Run the cli
  --input-dir /input/ \
  --dry-run \
  --skip-sync

echo "Smoketesting succesful!"