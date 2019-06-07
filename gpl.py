#!/usr/bin/env python3

import csv
import os
import credentials as creds
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


version = 4.0

base = os.path.expanduser("~/Cisco")
glus = os.path.expanduser("~/Cisco/glus.txt")
price = os.path.expanduser("~/Cisco/price.txt")


def get_file(base):
    options = Options()
    options.headless = True
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.dir", base)
    options.set_preference("browser.download.folderList", 2)
    options.set_preference(
        "browser.helperApps.neverAsk.saveToDisk",
        "application/vnd.xara;charset=utf-8")
    browser = webdriver.Firefox(options=options)
    browser.get(
        'https://prpub.cloudapps.cisco.com/lpc/currentPL.faces?flow=nextgen'
    )
    wait = WebDriverWait(browser, 10)
    print("Logging In")
    login1 = wait.until(
        EC.visibility_of_element_located((By.ID, 'login-button')))
    login1 = browser.find_element_by_id("userInput")
    login1.send_keys(creds.userid, Keys.RETURN)
    wait = WebDriverWait(browser, 30)
    login2 = wait.until(
        EC.visibility_of_element_located((By.ID, 'kc-login')))
    login2 = browser.find_element_by_id('password')
    login2.send_keys(creds.passwd, Keys.RETURN)
    wait = WebDriverWait(browser, 30)
    print("Downloading the File")
    file_type = wait.until(
        EC.visibility_of_element_located((By.NAME, 'button1')))
    file_type = browser.find_element_by_partial_link_text(
        'Select a File Format')
    file_type.click()
    options = browser.find_element_by_partial_link_text('Ascii').click()
    submit = browser.find_element_by_id('button1')
    submit.click()
    wait = WebDriverWait(browser, 5)
    alert = browser.switch_to.alert
    alert.accept()
    sleep(100)
    for file in base:
        if os.path.isfile(base + 'glus.web.part'):
            continue
    else:
        browser.quit()


def manipulate():
    print("Grooming the File")
    dest = open(price, "wt")
    with open(glus, 'rt',)as groom:
        reader = csv.reader(groom, delimiter="|")
        writer = csv.writer(dest, delimiter="|")
        for row in reader:
            if "CORE" in row:
                writer.writerow((row[3], row[4], row[6]))
        dest.close()
        groom.close()
        os.remove(glus)


def path_exists():
    if not os.path.isdir(base):
        try:
            os.makedirs(base)
        except (SystemExit):
            raise


def main():
    path_exists()
    get_file()
    manipulate()


if __name__ == '__main__':
    main()
