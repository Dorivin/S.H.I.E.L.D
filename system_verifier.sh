#!bin/bash
echo "****************"
echo "Linux OS Info:"
uname -a
echo "****************"

FILE=/tmp/zip_job.py
echo "Checking if $FILE exists..."

if [ -f "$FILE" ]; then
    echo "$FILE exists."
else 
    echo "$FILE does not exist."
fi