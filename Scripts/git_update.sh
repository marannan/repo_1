#!/bin/sh
cd /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1
echo "-----------------"
echo "syncing github at"
pwd
echo "-----------------"
git add *
git commit -m $1
git push
echo "----------"
echo "completed! "
echo "----------"
