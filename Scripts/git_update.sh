#!/bin/sh
echo "----------------------------------------------------------" >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
cd /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1 >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
echo "git          : sync" >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
echo "directory    : $(pwd)" >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
echo "time         : $(date)" >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
echo "status       : started" >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
git add * >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
git commit -a -m "$(date)" >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
git push master repo_1 >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
echo "status 	   : completed" >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
echo "time         : $(date)" >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log
echo "-----------------------------------------------------------" >> /media/ashok/My_Drive/Ashok/Google_Drive_2/Docs/Github/repo_1/Scripts/Logs/git_sync.log