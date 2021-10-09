from selenium import webdriver
import time

Driver=webdriver.Chrome()

Driver.get("http://www.jd.com")
Driver.maximize_window()
Driver.find_element_by_xpath("//*[@id='key']").send_keys("华为P50 Pro")
time.sleep(2)
Driver.find_element_by_xpath("//*[@class='button']").click()

time.sleep(2)

Driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img").click()




time.sleep(5)
Driver.quit()