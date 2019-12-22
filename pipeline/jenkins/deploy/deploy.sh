
#!/bin/bash
export IP=192.168.200.182
export PASS=978645312Or
export BUILD_TAG=10
echo maven-project > /tmp/.auth

echo $BUILD_TAG >> /tmp/.auth 
echo $PASS >> /tmp/.auth
scp /tmp/.auth jenkins@$IP:/tmp/.auth
scp jenkins/deploy/publish.sh jenkins@$IP:/tmp/publish.sh
echo hello
ssh -t jenkins@$IP "echo 1234 | sudo -S /tmp/publish.sh"

