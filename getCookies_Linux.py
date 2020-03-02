#!/home/genius861030/miniconda3/envs/crawler/bin/python -u

import personalInf
from threading import Thread
import time
import string
import random
import requests
import urllib

from selenium import webdriver
from PIL import Image

import IPython.display as Imm

# try:
#     from PIL import Image
# except ImportError:
#     import Image
import pytesseract

import shutil

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException

import os
import sys

success = False


def getReq(cookieValue):
    hhGet = {
        "Cookie": "JSESSIONID={}".format(cookieValue)
    }
    urlGetUserCourse = "http://cos1.ntnu.edu.tw/AasEnrollStudent/StfseldListCtrl"
    dataGetUserCourse = {
        "action": "showGrid",
        "_dc": "1579631355794",
        "page": "1",
        "start": "0",
        "limit": "999999",
        "group": "[{\"property\":\"v_totalCredit\",\"direction\":\"ASC\"}]",
        "sort": "[{\"property\":\"v_totalCredit\",\"direction\":\"ASC\"}]"
    }
    urlGetUserCourse = urlGetUserCourse + "?" + \
        urllib.parse.urlencode(dataGetUserCourse)
    UserCourse = requests.get(urlGetUserCourse, headers=hhGet)
    return UserCourse.text


q = None
cookieValue = None


def check():
    ti = 0
    TT = 0
    while True:
        time.sleep(1)

        # print("ti: ", ti)
        if cookieValue != None:

            if ti > 600:
                try:
                    g = getReq(cookieValue)
                    # print('\n',g)
                    if '非選課期間' in g:
                        f = open("log.txt", "a")
                        f.writelines(str(TT)+' 非選課期間 '+"\n")
                        f.close()
                        print('\nGot ERROR. 非選課期間')
                        print("\nTime: ", TT, end="")
                    else:
                        print("\nSuccess")
                except:
                    f = open("log.txt", "a")
                    f.writelines(str(TT)+"\n")
                    f.close()
                    print('\nGot ERROR.')
                    print("\nTime: ", TT, end="")
                try:
                    driver.execute_script("countSecond = 3000")
                    print('\n\ncookieValue: \n', cookieValue)
                except:
                    print("\nexecute_script")
                #print("\nSet countSecond value = 3000 \nPress \"q\" to exit: ")
                ti = 1
            TT += 1
            ti += 1
            # print("\nTime: ", TT, end="")
            # time.sleep(2)
            # driver.save_screenshot('test.png')
            # print(driver.get_log('browser'))
            if q == "q":
                return

        else:
            print("Loading")


def untilClick(id1, id2):
    while True:
        time.sleep(0.5)
        try:
            driver.find_element_by_id(id1).click()
            return
        except:
            print("wait!! ", id1, " !!")
        try:
            driver.find_element_by_id(id2).click()
            return
        except:
            print("wait!! ", id2, " !!")


def untilClickByLinkText(text):
    while True:
        time.sleep(0.5)
        try:
            driver.find_element_by_link_text(text).click()
            return
        except:
            print("wait!! ", id, " !!")


t = Thread(target=check)
t.start()
filenName = ''.join(random.choice(string.ascii_uppercase +
                                  string.digits) for _ in range(5))
while success != True:
    # driver = webdriver.Chrome()

    # chromedriverPath  = shutil.which("chromedriver")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("window-size=1200x600")
    driver = webdriver.Chrome(
        "/home/genius861030/miniconda3/envs/crawler/bin/chromedriver", options=options)
    # print("chromedriverPath", chromedriverPath)
    driver.get(
        "http://cos1.ntnu.edu.tw/AasEnrollStudent/LoginCheckCtrl?language=TW")

    driver.save_screenshot(filenName+'capture.png')
    vfImg = driver.find_element_by_id("imageBoxCmp")

    left = vfImg.location['x']
    right = left + vfImg.size['width']
    top = vfImg.location['y']
    bottom = top + vfImg.size['height']
    # left = vfImg.location['x']+895
    # right = left + vfImg.size['width']+50
    # top = vfImg.location['y']+215
    # bottom = top + vfImg.size['height']+20

    img = Image.open(filenName+'capture.png')
    img = img.crop((left, top, right, bottom))
    img.save(filenName+'vfImg.png', 'png')
    os.remove(filenName+'capture.png')

    code = pytesseract.image_to_string(Image.open(filenName+'vfImg.png'))
    code = code.lower().translate({ord(i): None for i in '\n '})
    os.remove(filenName+'vfImg.png')
    print("code:  ", code)
    if len(code) != 4 or code.isalpha() != True:
        print("Verification code format does not match !")
        driver.close()
        continue
#     code = code.lower().translate({ord(i): None for i in '\n '})
    # print(code)

    elem_user = driver.find_element_by_id("userid-inputEl")
    elem_user.send_keys(personalInf.studentID)
    elem_pwd = driver.find_element_by_name("password")
    elem_pwd.send_keys(personalInf.password)
    elem_vf = driver.find_element_by_id("validateCode-inputEl")
    elem_vf.send_keys(code)

    try:
        driver.find_element_by_id("button-1016-btnWrap").click()
    except:
        # print("Loading too much time!")
        print("err")
        driver.close()
        continue

    delay = 10  # seconds
    try:
        # try:
        fastrack1005 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'button-1005-btnWrap')))
        fastrack1005.click()
        # except:
        # print("wowo")
        fastrack = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'button-1017-btnWrap')))
        fastrack.click()
        cookieValue = str(driver.get_cookies()[0]["value"])
        print('cookieValue: \n', cookieValue)
        if cookieValue != None:
            # break
            # driver.switch_to.frame('stfseldListDo')
            while True:
                time.sleep(0.5)
                try:
                    driver.switch_to.frame('stfseldListDo')
                    break
                except:
                    print("!!")
            untilClick('query', 'add')
            time.sleep(1)
            driver.switch_to.parent_frame()
            # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'query')))
        while True:
            # q = input("Press \"q\" to exit: ")
            q = "x"

            if q == "q":
                success = True

                # driver.close()
                break

#         driver.close()
    except TimeoutException:
        print("Loading too much time!")
        driver.close()
        print("Reloading Page")
        continue
    except UnexpectedAlertPresentException as err:
        # print("Loading took too much time!")
        # print(type(err))    # the exception instance
        # print("aa", err.args)     # arguments stored in .args
        # print("bb", err.args)
        print("code: ", code)
        print(err)
        driver.close()
        print("Reloading Page")
        continue
    #except:
    #    print("Error")
    #    driver.close()
    #    print("Reloading Page")
    #    continue

try:
    # t.raise_exception()

    t.join()
    driver.close()
    print("\nClosing browser!!\n")
    # sys.exit()

except:
    print("Close browser!!")
