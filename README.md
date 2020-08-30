* ### [set up Anaconda under Google Cloud VM and transfer files on Windows](https://medium.com/google-cloud/set-up-anaconda-under-google-cloud-vm-on-windows-f71fc1064bd7)

```sh
sudo apt-get update
sudo apt-get install -y --force-yes bzip2 libxml2-dev wget

wget https://repo.anaconda.com/miniconda/Miniconda3-4.7.12.1-Linux-x86_64.sh

bash Miniconda3-4.7.12.1-Linux-x86_64.sh

rm Miniconda3-4.7.12.1-Linux-x86_64.sh

source .bashrc
. ~/.bashrc
```
* ### install git
```sh
sudo apt install -y --force-yes git-all
```

* ### [github](https://github.com/Aaron3141/NTNU-Crawler-gcp.git)
```sh
git clone https://github.com/Aaron3141/NTNU-Crawler-gcp.git
```
* ### set up python enviroment
```sh
conda env create -f env.yml --yes
conda activate crawler
yes | pip install -r requirements.txt 
```

* ### [set up selenium python](https://github.com/garywu/google-compute-engine-selenium)

```sh
# wget https://raw.githubusercontent.com/garywu/gae-selenium/master/install.sh && chmod +x install.sh && ./install.sh &&  ./start_headless.sh && ./demo.py
chmod +x install.sh && ./install.sh >> log.log

mv chromedriver /home/[name]/miniconda3/envs/crawler/bin/
```
* ### [set up Pytesseract](https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)

```sh
sudo apt-get install -y --force-yes tesseract-ocr
sudo apt-get install -y --force-yes libtesseract-dev
```
* ### run getCookie.py
```sh
touch personalInf.py
echo "studentID = \"\"" >> personalInf.py
echo "password = \"\"" >> personalInf.py

```

```sh
chmod +x getCookies_Linux.py catCookies.sh createCookies.sh killCookies.sh
mkdir cookies
./createCookies.sh [arg1] [arg2]
./catCookies.sh [arg1] [arg2]
./killCookies.sh [arg1] [arg2]

# nohup python getCookies_Linux.py&

```
* ### run selectCourse_Linux.py
```sh
chmod +x selectCourse_Linux.py toSelectCourse.sh
./selectCourse_Linux.sh [arg1] 

```

* ### kill all
```sh
kill -9 -1
```
* ### PID & Kill
```sh
ps ax| grep python
kill -9 [PID]
```
<!-- ps ufx
ps aux | grep getCookies.py 
ps -la -->


