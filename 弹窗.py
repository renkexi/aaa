from selenium import webdriver
import time

Driver=webdriver.Chrome()

Driver.get(r"C:\Users\www24\Desktop\PYTHON\autotest.html")
Driver.maximize_window()
Driver.find_element_by_xpath("//*[@value='submit']").click()
time.sleep(5)
Driver.switch_to.alert.dismiss()#取消accept确定