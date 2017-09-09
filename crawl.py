# -*- coding: utf-8 -*-
"""
Created on Sat Sep 02 18:52:33 2017

@author: zchenack
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

dates = []
Stri = "20170"
Mon = [1,3,5,7,8]
for i in range(3,9):
    if i in Mon:
        N = 31
    else:
        N = 30
    for j in range(1,N+1):
        if j <10:
            tmpS = '0'+str(j)
        else:
            tmpS = str(j)
        dates.append(Stri+str(i)+tmpS)

driver = webdriver.Chrome()
driver.get("http://stockhtm.finance.qq.com/fund/jzzx/index.htm")
#assert "Python" in driver.title
elem = driver.find_element_by_name("textfield")

for dat in dates:
    #print dat
    elem.clear()
    elem.send_keys(dat)
    elem1 = driver.find_element_by_name("Submit01")
    action1 = ActionChains(driver).move_to_element(elem1)
    action1.click(elem1)
    action1.perform()
    elem2 = driver.find_element_by_name("Submit02")
    action2 = ActionChains(driver).move_to_element(elem2)
    action2.click(elem2)
    action2.perform()

#elem.send_keys(Keys.RETURN)
#print driver.page_source
#driver.get("http://stockhtm.finance.qq.com/fund/jzzx/index.htm")
