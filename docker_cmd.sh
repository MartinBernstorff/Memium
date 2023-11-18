docker build . -t personal-mnemonic-medium:latest -f Dockerfile

docker volume create ankidecks

docker run -itd \
  -v /Users/Shared/life-lessons/docs/life-lessons:/input \
  -v $HOME/ankidecks:/output \
  --restart unless-stopped \
  personal-mnemonic-medium \
  python personal_mnemonic_medium/cli.py /input/ $HOME/ankidecks --watch --use-anki-connect