from selenium import webdriver
import time
from orion_UI_Test.usedata import get_webinfo, get_userinfo

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

def checkresult(d,text):
    try:
        err = d.find_element_by_id(text)
        print(err.text)
    except:
        print("Account and pwd right")
def login_test(ele_dict,user_list):
    d = openbrowser()
    openUrl(d,ele_dict['url'])
    ele_tuple = findelement(d,ele_dict)
    for arg in user_list:

        sendvar(ele_tuple,arg)
        checkresult(d,ele_dict['errorid'])

if __name__ =='__main__':
    user_list = get_userinfo(r'usrinfo.txt')
    ele_dict = get_webinfo(r'webinfo.txt')
    login_test(ele_dict,user_list)