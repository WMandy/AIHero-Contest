import requests
from urllib.request import urlretrieve
from selenium import webdriver
from time import sleep
import cv2
import numpy as np
import os

# 打开浏览器，最大化窗口
driver = webdriver.Chrome()
driver.maximize_window()
# 获取网页源代码
driver.get('http://www.gsxt.gov.cn/index.html')
sleep(3)
driver.find_element_by_name('searchword').click()
driver.find_element_by_name('searchword').send_keys('德化县墩华')

files = [x for x in os.listdir('D:\\wmd\\CAPTCHA_OOW\\test_images\\') if '.png' in x]
xx = int(files[-1].rstrip('.png')) + 1

# f = open('text_Chrome.txt', 'w')

for i in range(200):
    
    # 找到class name为'l-captcha'的元素，点击（出现验证码图片，出现新的源代码）
    
    if i == 0 or (i+1) % 6 == 0:
        driver.refresh()
        driver.find_element_by_name('searchword').click()
        driver.find_element_by_name('searchword').send_keys('德化县墩华')
        driver.find_element_by_id('btn_query').click()
        sleep(15)
    
    # 定位图片url
    try:
        driver.find_element_by_class_name('geetest_item_img')
    except:
        print('sleeping......')
        driver.refresh()
        driver.find_element_by_name('searchword').click()
        driver.find_element_by_name('searchword').send_keys('德化县墩华')
        driver.find_element_by_id('btn_query').click()
        sleep(30)
    try:
        driver.find_element_by_class_name('geetest_item_img')
    except:
        print('sleeping......')
        driver.refresh()
        driver.find_element_by_name('searchword').click()
        driver.find_element_by_name('searchword').send_keys('德化县墩华')
        driver.find_element_by_id('btn_query').click()
        sleep(30)
    tmp = driver.find_element_by_class_name('geetest_item_img')
    img_url = tmp.get_attribute('src')
    # print(img_url)

    # print(res)
    
    # 爬取图片
    # img_path = 'D:\\sunyiwu\\Crawler\\CAPTCHA_Chrome\\CAPTCHA.png'
    img = requests.get(img_url).content
    img = cv2.imdecode(np.fromstring(img, np.uint8), 1)
    
    cv2.imwrite('D:\\wmd\\CAPTCHA_OOW\\test_images\\' + '%06d' % (i+xx) + '.png', img[:344, :])
    cv2.imwrite('D:\\wmd\\CAPTCHA_OOW\\Words\\' + '%06d' % (i+xx) + '.png', img[344:, :])
           
    driver.find_element_by_class_name('geetest_refresh').click()
    sleep(3)
    print(i+xx+1)
# f.close()