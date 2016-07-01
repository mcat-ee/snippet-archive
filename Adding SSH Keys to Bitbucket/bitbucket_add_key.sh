#!/bin/bash

BBUSER=$1
BBPASS=$2

mkdir ~/.ssh
cd ~/.ssh
ssh-keygen -t rsa -f worker_rsa -N '' && cat ./worker_rsa.pub | while read key; do curl --user "$BBUSER:$BBPASS" --data-urlencode "key=$key" -X POST https://bitbucket.org/api/1.0/users/$BBUSER/ssh-keys -v ; echo $key; done

chmod 400 ./worker_rsa
chmod 400 ./worker_rsa.pub

ssh-add ./worker_rsa
ssh-keyscan bitbucket.org >> known_hosts
