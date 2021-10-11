from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
Driver=webdriver.Chrome()

Driver.get("http://www.jd.com")
Driver.maximize_window()
Driver.find_element_by_xpath("//*[@id='key']").send_keys("华为P50 Pro")
time.sleep(2)
Driver.find_element_by_xpath("//*[@class='button']").click()

time.sleep(2)

Driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[1]/div/div[1]/a/img").click()

data=Driver.window_handles
Driver.switch_to.window(data[1])

Driver.find_element_by_xpath("//*[@id='InitCartUrl']").click()

Driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]/a").click()

Driver.find_element_by_xpath("//*[@id='loginname']").send_keys("17631406990")
Driver.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("sfdjf")
Driver.find_element_by_xpath("//*[@id='loginsubmit']").click()

ac = ActionChains(Driver)
ele = Driver.find_element_by_xpath("//*[@id='JDJRV-wrap-loginsubmit']/div/div/div/div[2]/div[3]")

ac.click_and_hold(ele).move_by_offset(108,0).perform()

ac.release()

time.sleep(2)
Driver.quit()