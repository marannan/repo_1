#!/bin/sh
cd /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1
echo "syncing github for repo at /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1"
git add *
git commit -m $1
git push
