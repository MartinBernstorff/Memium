docker build . -t personal-mnemonic-medium -f Dockerfile

docker volume create ankidecks

docker run -itd \
  -v $HOME/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/Life\ Lessons\ iCloud/:/input \
  -v $HOME/ankidecks:/output \
  --restart unless-stopped \
  personal-mnemonic-medium \
  python application/main.py /input/ $HOME/ankidecks --watch