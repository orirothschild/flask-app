#/bin/bash

MASSAGE=$1

git add . &&\
git commit -am "$MASSAGE" && \
git push && \
git push github
