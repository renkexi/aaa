

from selenium import webdriver


Driver=webdriver.Chrome()

Driver.get(r"C:\Users\www24\Desktop\PYTHON\autotest.html")
Driver.maximize_window()
Driver.find_element_by_xpath("//*[@id='accountID']").send_keys("dssvww")
Driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("214")
Driver.find_element_by_xpath("//*[@id='areaID']").send_keys("北京市")
Driver.find_element_by_xpath("//*[@id='sexID2']").click()
Driver.find_element_by_xpath("//*[@value='spring']").click()
Driver.find_element_by_xpath("//*[@value='Auterm']").click()
Driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"C:\Users\www24\Pictures\Saved Pictures\国旗.jpg")
