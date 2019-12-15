#!/bin/bash
# Copy the new jar to specified location

cp -f java-app/target/*.jar jenkins/build/
echo "***********************"
echo "*** build the image ***"
echo "***********************"

cd jenkins/build && docker-compose -f docker-compose-build.yml build --no-cache 
