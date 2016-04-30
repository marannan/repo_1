#!/bin/bash
. ~/.keychain/`/bin/hostname`-sh
echo "----------------------------------------------------------"
cd /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1
echo "git          : sync"
echo "directory    : $(pwd)"
echo "time         : $(date)"
echo "status       : started"
git add *
git commit -a -m "$(date)"
git push origin master
echo "status 	     : completed"
echo "time         : $(date)"
echo "-----------------------------------------------------------"