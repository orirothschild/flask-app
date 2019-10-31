#/bin/bash
crumb=$(curl -u "ori:1234" -s 'http://jenkins.local:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)')
echo "$crumb"
curl -u "ori:1234" -H "$crumb" -X POST http://jenkins.local:8080/job/aws_backup/buildWithParameters?MYSQL_HOST=db_host&DATABASE_NAME=testdb&AWS_BUCKET_NAME=jenkins-mysql-backup-ls

