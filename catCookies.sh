#!/bin/bash

for i in `seq $1 $2`
do
	echo -e "\n"cookies$i"\n"
	cat ./cookies/cookies$i.txt | grep -A1 cookieValue
done