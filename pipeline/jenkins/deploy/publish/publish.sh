!#/bin/bash
export PASS=$(sed -n '3p' /tmp/.auth)
export TAG=$(sed -n '2p' /tmp/.auth)
export IMAGE=$(sed -n '1p' /tmp/.auth)

docker login -u orirothschild -p $PASS
cd ~/maven && docker-compose up -d

