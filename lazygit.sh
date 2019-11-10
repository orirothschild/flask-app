#/bin/bash

MASSAGE=$1

echo 1234 | sudo -S command
sudo -u ori git add . &&\
git commit -am "$MASSAGE" && \
git push && \
git push github
