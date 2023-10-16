docker build . -t personal-mnemonic-medium -f Dockerfile

docker run -itd \
  -v $HOME/Library/Mobile\ Documents/iCloud~md~obsidian/Documents/Life\ Lessons\ iCloud/:/input \
  --restart unless-stopped \
  personal-mnemonic-medium \
  python application/main.py /input/ Life.apkg --watch