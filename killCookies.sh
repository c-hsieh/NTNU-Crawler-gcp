#!/bin/bash

for i in `seq $1 $2`
do
	echo -e "\n"setCookies$i"\n"
	kill -9 `cat cookies/pidcookies$i.txt`
	rm ./cookies/pidcookies$i.txt
done