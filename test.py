import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import pandas as pd
import json
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium")
driver = webdriver.Chrome(options=chrome_options)
s = Service("C:/bin/chromedriver.exe")

def main():
    driver.get("https://proxy6.net")
    with open("cookies.json", "r") as f:
        cookies = f.read()
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://proxy6.net")

main()
