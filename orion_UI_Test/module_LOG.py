from selenium import webdriver
import time
from orion_UI_Test.usedata import get_webinfo,get_userinfo,xlUserinfo,xlUserinfo
from orion_UI_Test.log_module import Loginfo,Xlloginfo
from selenium.webdriver.support.ui import WebDriverWait

# help(WebDriverWait)

url = "https://nbai.io/dashboard/#/login"
valid_username = "nbaitest1@gmail.com"  # production
valid_password = "qiang1102"  # production


def get_ele_times(driver, times, func):
    return WebDriverWait(driver, times).until(func)


def openbrowser():
    webdriver_handle = webdriver.Chrome("/Users/guoec/Downloads/chromedriver")
    return webdriver_handle


def openUrl(handle, url):
    handle.get(url)
    handle.maximize_window()


def findelement(d, arg):

    if 'text_id' in arg:
        ele_login = get_ele_times(d, 10, lambda d: d.find_element_by_id(arg['text_id']))
        ele_login.click()

    useEle = d.find_element_by_name(arg['userid'])
    pwdEle = d.find_element_by_name(arg['pwdid'])
    loginEle = d.find_element_by_id(arg['loginid'])
    # print(useEle)
    # print(pwdEle)
    # print(loginEle)

    return useEle, pwdEle, loginEle

def sendvar(eletuple,arg):
    userlist=['uname','pwd']
    i=0
    for key in userlist:
        eletuple[i].send_keys('')
        eletuple[i].clear()
        eletuple[i].send_keys(arg[key])
        i += 1
    eletuple[2].click()

def checkresult(d,err_id,arg,log):
    result = False
    time.sleep(2)
    try:
        err = d.find_element_by_id(err_id)
        # msg = 'username:%s;password:%s:error:%s'%(arg['uname'],arg['pwd'],err.text)

        print(err.text)
        log.log_write(arg['uname'],arg['pwd'],'Error','Test failed')
    except:
        # msg = 'username:%s;password:%s:pass'%(arg['uname'],arg['pwd'])
        # log.log_write(msg)
        log.log_write(arg['uname'],arg['pwd'],'Pass')

        print("Account and pwd right")
        result = True
    return result

def logout(d):
    d.find_element_by_xpath('//*[@id="m_header_topbar"]/div/ul/li[1]/a/span[2]/img').click()
    d.find_element_by_xpath('//*[@id="m_header_topbar"]/div/ul/li[1]/div/div/div[2]/div/ul/li[4]/a').click()
    d.find_element_by_xpath('//*[@id="m_login"]/div[1]/div[1]/a/img').click()

def login_test(ele_dict,user_list):
    d = openbrowser()
    # log = Loginfo()
    log=Xlloginfo()
    log.log_init('sheet1','uname','pwd','result','msg')
    openUrl(d,ele_dict['url'])
    ele_tuple = findelement(d,ele_dict)
    for arg in user_list:

        sendvar(ele_tuple,arg)
        result = checkresult(d,ele_dict['errorid'],arg,log)
        if result==True:
            logout(d)
            ele_tuple = findelement(d, ele_dict)
    d.quit()
    log.log_close()

if __name__ =='__main__':
    # user_list = get_userinfo(r'usrinfo.txt')
    ele_dict = get_webinfo(r'webinfo.txt')
    xinfo = xlUserinfo(r'userinfo.xls')
    user_list = xinfo.get_sheetinfo_by_index(0)
    login_test(ele_dict,user_list)