#!/bin/bash
export IP=192.168.200.182
echo maven-project > /tmp/.auth

echo $BUILD_TAG >> /tmp/.auth 
echo $PASS >> /tmp/.auth

scp /tmp/.auth jenkins@$IP:/tmp/.auth
