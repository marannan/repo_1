#!/bin/sh
echo "----------------------------------------------------------"
cd /media/ashok/My_Drive/Ashok/Google_Drive_1/
echo "google drive : sync"
echo "directory    : $(pwd)"
echo "time         : $(date)"
echo "status       : started"
grive sync
echo "status 	     : completed"
echo "time         : $(date)"
echo "-----------------------------------------------------------"
