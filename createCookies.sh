#!/bin/bash

for i in `seq $1 $2`
do
	echo -e "\n"setCookies$i"\n"
	nohup ./getCookies_Linux.py > cookies/cookies$i.txt < /dev/null &
	echo $! > cookies/pidcookies$i.txt
done