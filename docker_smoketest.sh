set -e
docker build . -t memium:latest -f Dockerfile
docker volume create ankidecks

INPUT_DIR=$HOME/input/

mkdir -p $INPUT_DIR
echo "Creating $INPUT_DIR"
echo -e "Q. Question here\nA. Answer!" >> $INPUT_DIR/test.md

docker run -i \
  -e HOST_INPUT_DIR=$INPUT_DIR \
  -v $INPUT_DIR:/input \
  --restart unless-stopped \
  memium \
  memium \
  --input-dir /input \
  --dry-run \
  --skip-sync

echo "Smoketesting succesful!"