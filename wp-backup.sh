#!/bin/bash
NOW=$(date +"%Y-%m-%d-%H:%M")
FILE="blechwerk.org.$NOW.tar"
BACKUP_DIR="/home/odroid/Core/dana/backup"
WWW_DIR="/var/www/"


DB_USER="patrick"
DB_PASS="hallo6"
DB_NAME="wpdata"
DB_FILE="blechwerk.org.$NOW.sql"

tar cvf $BACKUP_DIR/$FILE $WWW_DIR
mysqldump -u$DB_USER -p$DB_PASS $DB_NAME > $BACKUP_DIR/$DB_FILE

