#!/bin/bash

# set up Anaconda under Google Cloud VM and transfer files on Windows
sudo apt-get update
sudo apt-get install -y --force-yes bzip2 libxml2-dev wget

wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh

bash Miniconda3-4.7.12.1-Linux-x86_64.sh

rm Miniconda3-4.7.12.1-Linux-x86_64.sh

source .bashrc
. ~/.bashrc

# install git
sudo apt install -y --force-yes git-all

# github
cd ~
git clone https://github.com/Aaron3141/NTNU-Crawler-gcp.git

# set up python enviroment
conda env create -f env.yml --yes
conda activate crawler
yes | pip install -r requirements.txt 

# set up Pytesseract
sudo apt-get install -y --force-yes tesseract-ocr
sudo apt-get install -y --force-yes libtesseract-dev

# set up selenium python
cd ~
cd NTNU-Crawler-gcp/SeleniumGCP
chmod +x install.sh && ./install.sh >> log.log
mv chromedriver $pwd\miniconda3/envs/crawler/bin/
cd ~

# run getCookie.py
cd ~
cd NTNU-Crawler-gcp
chmod +x getCookies_Linux.py catCookies.sh createCookies.sh killCookies.sh
mkdir cookies
touch personalInf.py
read -r -p 'Give me a studentID: \n' studentID
echo "studentID = \"$studentID\"" >> personalInf.py
read -r -p 'Give me a password: \n' password
echo "password = \"$password\"" >> personalInf.py


echo "DONE!!!!!!"