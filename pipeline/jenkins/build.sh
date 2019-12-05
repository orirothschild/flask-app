#!/bin/bash
# Copy the new jar to specified location
export BUILD_TAG=5

cp -f java-app/target/*.jar jenkins/build/
echo "***********************"
echo "*** build the image ***"
echo "***********************"

cd jenkins/build && docker-compose -f docker-compose-build.yml build --no-cache 
