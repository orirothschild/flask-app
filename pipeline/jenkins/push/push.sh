#!/bin/bash
echo "*************************************"
echo "*******************push**************"
echo "*************************************"
IMAGE="maven-project"
echo "** logging in ***"
docker login -u orirothschild -p $PASS

echo "*** Tagging image ***"

docker tag $IMAGE:$BUILD_TAG orirothschild/$IMAGE:$BUILD_TAG

echo "****PUSHING IMAGE ******"
docker push orirothschild/$IMAGE:$BUILD_TAG

