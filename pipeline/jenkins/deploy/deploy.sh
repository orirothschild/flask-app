
#!/bin/bash
export IP=192.168.200.182
echo maven-project > /tmp/.auth

echo $BUILD_TAG >> /tmp/.auth 
echo $PASS >> /tmp/.auth
echo "hello"
scp /tmp/.auth jenkins@$IP:/tmp/.auth

scp ./jenkins/deploy/publish/publish.sh jenkins@$IP:/tmp/deploy.sh
ssh -t jenkins@192.168.200.182 "chmod +x /tmp/deploy.sh"

