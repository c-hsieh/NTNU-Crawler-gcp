#!/bin/bash

RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color
# printf "I ${RED}love${NC} Stack Overflow\n"
# echo -e "I ${YELLOW}love${NC} Stack Overflow\n"

echo -e "${YELLOW}Set up Miniconda${NC}\n"
# set up Anaconda under Google Cloud VM and transfer files on Windows
sudo apt-get update
sudo apt-get install -y --force-yes bzip2 libxml2-dev wget

wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh

# bash Miniconda3-4.7.12.1-Linux-x86_64.sh
bash ~/Miniconda3-4.7.12.1-Linux-x86_64.sh -b -p $HOME/miniconda

rm Miniconda3-4.7.12.1-Linux-x86_64.sh

source .bashrc
. ~/.bashrc

echo -e "${YELLOW}Install git${NC}\n"
# install git
sudo apt install -y --force-yes git-all

echo -e "${YELLOW}Git clone${NC}\n"
# github
cd ~
git clone https://github.com/Aaron3141/NTNU-Crawler-gcp.git

echo -e "${YELLOW}Set up python enviroment${NC}\n"
# set up python enviroment
cd ~
cd NTNU-Crawler-gcp
conda env create -f env.yml --yes
conda activate crawler
yes | pip install -r requirements.txt 

echo -e "${YELLOW}Set up Pytesseract${NC}\n"
# set up Pytesseract
sudo apt-get install -y --force-yes tesseract-ocr
sudo apt-get install -y --force-yes libtesseract-dev

echo -e "${YELLOW}Set up selenium python${NC}\n"
# set up selenium python
cd ~
cd NTNU-Crawler-gcp/SeleniumGCP
chmod +x install.sh && ./install.sh >> log.log
cd ~
cd selenium
mv chromedriver $pwd\miniconda3/envs/crawler/bin/
cd ~

echo -e "${YELLOW}Set uppppp${NC}\n"
# run getCookie.py
cd ~
cd NTNU-Crawler-gcp
chmod +x getCookies_Linux.py catCookies.sh createCookies.sh killCookies.sh
mkdir cookies
touch personalInf.py
read -r -p 'Give me a studentID: \n' studentID
echo -e "studentID = \"$studentID\"" >> personalInf.py
read -r -p 'Give me a password: \n' password
echo -e "password = \"$password\"" >> personalInf.py

echo -e "${YELLOW}DONE!!!!!!${NC}\n"