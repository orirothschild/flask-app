#!/bin/bash

# name from ref head
JENKINS="jenkins.local:8080"

JENKINS_USER="ori"
JENKINS_USER_TOKEN="11fda108eacd598af38aaa3280b798bc10"

# nested path to job
JOB="seed-job"

## Script

JENKINS_AUTH="$JENKINS_USER:$JENKINS_USER_TOKEN"

CRUMB=$(curl --user "$JENKINS_AUTH" "$JENKINS"'/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)')

CONTAINS_ERROR=$(echo "$CRUMB" | grep "<html>" || true)

if [ -n "$CONTAINS_ERROR" ]; then
  echo "$CRUMB"
  exit 1
fi

curl -X POST \
  "$JENKINS"/job/"$JOB"/build \
  --user "$JENKINS_AUTH" \
-H "$CRUMB"

