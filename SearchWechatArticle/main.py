#coding:utf-8

from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np


chrome_driver = "driver/chromedriver.exe"
chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless') #增加无界面选项
chrome_options.add_argument('--disable-gpu') #如果不加这个选项，有时定位会出现问题

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=chrome_driver)
browser.maximize_window()
baseurl = "https://mp.weixin.qq.com/cgi-bin/loginpage?t=wxm2-login&lang=zh_CN"
browser.get(baseurl)
sleep(3)
# browser.find_element_by_name("account").send_keys("875980521@qq.com")
browser.find_element_by_name("account").send_keys("afcentry@163.com")
sleep(2)
# browser.find_element_by_name("password").send_keys("875980521@qq.com")
browser.find_element_by_name("password").send_keys("wang825624")
sleep(3)
browser.find_element_by_class_name("btn_login").send_keys(Keys.ENTER)
sleep(5)

browser.get_screenshot_as_file("qrcode.jpg")
# sourcepage = browser.page_source
# soup = BeautifulSoup(sourcepage,"lxml")
# href = "https://mp.weixin.qq.com/" + soup.find("img",attrs={"class":"weui-desktop-qrcheck__img js_qrcode"}).get("src")
# print(href)
# response = requests.get(href)
# with open("qrcode.jpg","wb") as file:
#     file.write(response.content)

lena = mpimg.imread('qrcode.jpg')  # 读取和代码处于同一目录下的 lena.png
# 此时 lena 就已经是一个 np.array 了，可以对它进行任意处理
lena.shape #(1000, 1000, 3)
plt.imshow(lena)  # 显示图片
plt.axis('off')  # 不显示坐标轴
plt.show()
# plt.close(lena)
# browser.get("https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit&action=edit&type=10&isMul=1&isNew=1&share=1&lang=zh_CN&token=1746734147&token=1746734147&lang=zh_CN")
print(browser.page_source)

sleep(8)
browser.find_element_by_class_name("weui-desktop-global__extra").find_element_by_class_name("weui-desktop-btn").send_keys(Keys.ENTER)
sleep(5)
browser.find_element_by_class_name("tab_cont_cover create-type__list jsMsgSendTab").find_element_by_class_name("create-type__item")[2].find_elements_by_class_name("create-type__link")[2].send_keys(Keys.ENTER)
# sleep(5)
# wait = ui.WebDriverWait(browser,10)
# wait.until(lambda driver: driver.find_element_by_class_name("weui-desktop-global__extra")) #weui-desktop-mass-initial
# browser.find_element_by_class_name("weui-desktop-btn").send_keys(Keys.ENTER)
print(browser.page_source)
sleep(60)
browser.quit()