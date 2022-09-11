from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import logInfo
#create one loginınfo than write your username and password

chrome_driver_path = "//Users/mehmetaliyildiz/Drivers/chromedriver"
browser = webdriver.Chrome(executable_path=chrome_driver_path)

browser.get("https://twitter.com/")

time.sleep(2)

giris_yap=browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span")

giris_yap.click()

time.sleep(5)

username=browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")

username.send_keys(logInfo.username)

ileri = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")

ileri.click()

time.sleep(5)

#kullanıcı_adı=browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input")
#kullanıcı_adı.send_keys(logInfo.kullanıcı_adı)

#ileri=browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/div").click

password = browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
password.send_keys(logInfo.password)

giris_butonu =browser.find_element(By.XPATH,"//*[@id='layers']/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
giris_butonu.click()

time.sleep(3)

twitterda_ara = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
twitterda_ara.click()

twitterda_ara.send_keys("#yazilimayolver")

ara_button = browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div")

ara_button.click()

time.sleep(5)
#browser.close()