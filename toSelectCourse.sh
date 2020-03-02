#!/bin/bash

echo -e "\n"selectCourse"\n"
nohup ./selectCourse_Linux.py > ./select/course$1.txt < /dev/null &
echo $! > ./select/pidCourse$1.txt