#!/bin/bash

NOW=$(date +"%Y-%m-%d")

Name="kimz-backup.tgz"
File="/var/www/kimz"

DB_USER="kim"
DB_PASS="hallo6"
DB_NAME="kimzdb"
DB_FILE="kimzdb.$NOW.sql"

mysqldump -u$DB_USER -p$DB_PASS $DB_NAME > $DB_FILE
tar czf $Name $File $DB_FILE
rm $DB_FILE
