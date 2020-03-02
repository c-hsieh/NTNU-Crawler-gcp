#!/bin/bash

echo -e "\n"selectCourse"\n"
nohup ./selectCourse_Linux.py > ./select/course$i.txt < /dev/null &
echo $! > ./select/pidCourse$i.txt