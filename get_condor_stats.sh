#!/bin/bash

# run the script as /bin/bash script.sh myfile(no path be in the same folder)

#example on how to get the file
#scp -i <key> <serveruser>@<server>:<file> <destination>

dt=$(date '+%Y-%m-%d_%H%M%S')
echo current time is "${dt}"
echo file being processed is "${1}"
echo
cp ~/condor_stats/${1} ~/condor_stats/${1}_backup
sed -i -e 's|/mnt/data/||g' -e 's|/job-\S*||g' ${1}
#awk -F '\s' '{print $2}' ${1} | sort | uniq -c | sort -nr 
#obscured usernames of people working at cyverse
awk  '( $2 != "rosysnake" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) {print $2}' ${1} | sort | uniq -c | sort -nr >> stat_users_"${dt}".txt
UNIQUE_USERS=`awk  '( $2 != "rosysnake" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) {print $2}' ${1} | sort | uniq -c | sort -nr | wc -l`
TOTAL_JOBS=`awk  '{sum += $1} END {print sum}' stat_users_"${dt}".txt`
echo there are "${UNIQUE_USERS}" unique users at $(date '+%d/%m/%Y')
echo total jobs run by these users: "${TOTAL_JOBS}"
echo saved user statistics in stat_user_"${dt}".txt
echo
awk  '( $2 != "rosysnake" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) {print $3}' ${1} | sort | uniq -c | sort -nr >> stat_applications_"${dt}".txt
APPLICATIONS=`awk  '( $2 != "rosysnake" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) && ( $2 != "" ) {print $3}' ${1} | sort | uniq -c | sort -nr | wc -l`
TOTAL_JOBS2=`awk '{sum += $1} END {print sum}' stat_applications_"${dt}".txt`
echo approximately \(as counting docker images and not applications\) the number of run applications is "${APPLICATIONS}"
echo confirming number of run job is "${TOTAL_JOBS2}"
echo saved application statistics in stat_applications_"${dt}".txt
