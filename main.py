from selenium import webdriver
from time import sleep
import json

start=3012
end=10000
errcount = 0
frequency = 80
def login(browser):
    browser.get("https://www.baifubao.com/user/0/login/0")
    browser.maximize_window()

    sleep(2)

    browser.find_element_by_id("TANGRAM__PSP_4__sms_btn_back").click()
    browser.find_element_by_name("userName").clear()
    browser.find_element_by_name("userName").send_keys('三淼服装')
    # browser.find_element_by_name("userName").send_keys('sep555@qq.com')
    sleep(2)
    browser.find_element_by_name("password").clear()
    browser.find_element_by_name("password").send_keys('!@sanmiao90')
    # browser.find_element_by_name("password").send_keys('Song19870919')
    sleep(5)
    browser.find_element_by_id("TANGRAM__PSP_4__submit").click()

# browser = webdriver.Firefox()
driverpath = "c:\\chromedriver_win32\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=driverpath,port=9515)
login(browser)

for phonevarint in range(start,end):
    
    for errcount in range(0,10):
        phonevar = "186"+str(phonevarint).zfill(4)+"0056"
        print("正在测试:"+phonevar)
        sleep(15)
        browser.get("https://www.baifubao.com/wireless/0/transfer/0/wap/0/start/0?username="+phonevar)
        sleep(15)
        data = browser.page_source
        data = data.replace('<html xmlns="http://www.w3.org/1999/xhtml"><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','')
        data = data.replace('</pre></body></html>','')
        dicta=json.loads(data)
        errinfo = dicta["content"]["payee_info"]["payee_err_info"]
        if(dicta["ret"]!='0'):
            print("系统出错，目前号码: "+phonevar)
        else:
            break
        
    print("检查错误："+str(errcount)+"次")
    print(errinfo)
    # print(errinfo=='对方尚未注册度小满金融，邀请对方注册完成后，即可转账。')
    if errcount == 9:
        print("系统出错次数达到 %d 次，正在退出" % errcount)
        break

    if errinfo=='对方尚未注册度小满金融，邀请对方注册完成后，即可转账。':
        print("未注册号码："+phonevar)
    
    if errinfo=='不支持给自己转账，请核对账号后重试！':
        print("找到号码："+phonevar)
        break

    # if phonevarint % 20 == 0:
    #     print("达到次数，正在等待。。。")
    #     sleep(3600)
    if phonevarint == (start + frequency):
        print("达到测试次数上限 %d，退出。。。当前号码： %s" %(frequency,phonevar))
        break

# browser.close()