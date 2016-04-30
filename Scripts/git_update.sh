#!/bin/bash
echo "----------------------------------------------------------"
cd /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1
echo "git          : sync"
echo "directory    : $(pwd)"
echo "time         : $(date)"
echo "status       : started"
git add *
git commit -a -m "$(date)"
git push https://marannan:0x!Gorange@github.com/marannan/repo_1.git master
echo "status 	     : completed"
echo "time         : $(date)"
echo "-----------------------------------------------------------"