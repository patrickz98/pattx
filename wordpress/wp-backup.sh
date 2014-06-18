#!/bin/bash

NOW=$(date +"%Y-%m-%d")

Name="patrickz-backup.tgz"
File="/var/www/patrickz"

DB_USER="patrick"
DB_PASS="hallo6"
DB_NAME="wpdata"
DB_FILE="wpdata.$NOW.sql"

mysqldump -u$DB_USER -p$DB_PASS $DB_NAME > $DB_FILE
tar cvzf $Name $File $DB_FILE
rm $DB_FILE

Name="dana-backup.tgz"
File="/var/www/dana"

DB_USER="dana"
DB_PASS="hallo6"
DB_NAME="danawpdb"
DB_FILE="danawpdb.$NOW.sql"

mysqldump -u$DB_USER -p$DB_PASS $DB_NAME > $DB_FILE
tar cvzf $Name $File $DB_FILE
rm $DB_FILE

Name="kimz-backup.tgz"
File="/var/www/kimz"

DB_USER="kim"
DB_PASS="hallo6"
DB_NAME="kimwpdb"
DB_FILE="kimwpdb.$NOW.sql"

mysqldump -u$DB_USER -p$DB_PASS $DB_NAME > $DB_FILE
tar cvzf $Name $File $DB_FILE
rm $DB_FILE

