#!/bin/bash -e
##Coguration

JENKINS="http://192.168.200.65:8080"

JENKINS_USER="orirothschild"
JENKINS_USER_TOKEN="1193b8617462894da4de8cc1a3a96d3657"

# nested path to job
JOB="unit-tests"
cardNumber="4580458045804580"	
cardCvv="123"
cardId="311321590"
creditCardExpirey="0421"
## Script

JENKINS_AUTH="$JENKINS_USER:$JENKINS_USER_TOKEN"

CRUMB=$(curl --user "$JENKINS_AUTH" "$JENKINS"'/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)')

CONTAINS_ERROR=$(echo "$CRUMB" | grep "<html>" || true)

if [ -n "$CONTAINS_ERROR" ]; then
  echo "$CRUMB"
  exit 1
fi

curl -X POST \
  "$JENKINS"/job/"$JOB"/buildWithParameters?delay=0sec \
  --user "$JENKINS_AUTH" \
-H "$CRUMB"

