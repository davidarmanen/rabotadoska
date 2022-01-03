import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from twocaptcha import TwoCaptcha
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select


solver = TwoCaptcha('7d1d1a150db56c564f3f2856c7220cc2')
s = Service("C:/bin/chromedriver.exe")
driver = webdriver.Chrome()
email = "armanendavid@gmail.com"
headline = "Заголовок"
with open("E:/Script/Python/sites/rabotadoska/text.txt") as f:
    text = f.read()

def main():
    driver.get("https://rabotadoska.ru")
    time.sleep(2)
    button1 = driver.find_element(By.XPATH, "//body/div[@id='wrapper']/div[2]/div[1]/ul[1]/li[2]/a[1]")
    button1.click()
    time.sleep(2)
    select1 = Select(driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/form[2]/div[1]/div[3]/select[1]'))
    select1.select_by_index(1)
    time.sleep(2)
    select2 = Select(driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/form[2]/div[1]/div[3]/select[2]"))
    select2.select_by_index(1)
    time.sleep(2)
    button2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/form[2]/div[1]/div[4]/input[1]")
    button2.click()
    time.sleep(3)
    input1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[2]/form[1]/div[4]/input[1]")
    input1.send_keys(headline)
    input2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[2]/form[1]/div[5]/textarea[1]")
    input2.send_keys(text)
    input3 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[2]/form[1]/div[7]/input[1]")
    input3.send_keys(email)
    input4 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[2]/form[1]/div[8]/input[1]")
    input4.send_keys(email)
    time.sleep(3)
    img = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[2]/form[1]/div[18]/img[1]")
    with open('filename.png', 'wb') as file:
        file.write(driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[3]/div[2]/form[1]/div[18]/img[1]').screenshot_as_png)
    result = solver.normal("filename.png")
    input5 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[2]/form[1]/div[18]/input[1]")
    input5.send_keys(result["code"])
    button3 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[2]/form[1]/div[19]/button[1]")
    button3.click()
    button4 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[3]/div[1]/input[1]")
    button4.click()
    time.sleep(5)

main()
