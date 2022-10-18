from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from worker import sleep
from GlobalVar import *
from pythonping import ping
from ReportLog import *
from RouterSupportTable import *
import os
import subprocess
import time
import threading
from AutoBoxControl import ConnectAutoBox, AcControl
from Txt_To_Excel import TXTFile_To_ExcelFile

def BrowserPause():
    goal = 1
    while (goal):
        AP_Info.driver.refresh()
        sleep(60)
  
       
def GetDeviceID():
    TestLoopBoxUpdate('0' +'\n')
    deviceID = os.popen('adb devices').read()
    print(deviceID)
    LogTextBoxUpdate(deviceID + '\n')
    return


def GetDeviceBrand():
    device = os.popen('adb shell getprop ro.product.brand').read()
    print('Device Brand: ', device)
    LogTextBoxUpdate("Device Brand: " + device + '\n')
    return


def GetDeviceName():
    deviceName = os.popen('adb shell getprop ro.product.model').read()
    print('Device Name: ', deviceName)
    LogTextBoxUpdate("Device Name: " + deviceName + '\n')
    return


def GetDeviceVersion():
    platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
    print('Android Version: ', platformVersion)
    LogTextBoxUpdate("Android Version: " + platformVersion + '\n')
    return


def AP_Login(ID, PW):
    # Open browser
    ProgrameControl.Browser_Type = BrowserInfo.comboBrowser.get()
    Browser_Type = BrowserInfo.comboBrowser.get()
    if ProgrameControl.Browser_Type == "Chrome":
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "none"
        AP_Info.driver = webdriver.Chrome()
    elif ProgrameControl.Browser_Type == "Firefox":
        desired_capabilities = DesiredCapabilities.FIREFOX
        desired_capabilities["pageLoadStrategy"] = "none"        
        AP_Info.driver = webdriver.Firefox()

    LogTextBoxUpdate("You open browser is " + Browser_Type + '\n')
    # Input address
    print('Router ID: ' + ID, 'Router Password: ' + PW, sep='\n')
    AP_Webaddress = EthernetInfo.AP_Webaddress.get()
    AP_Info.driver.get(AP_Webaddress)
    sleep(10)
    # Login password
    context = AP_Info.driver.find_element_by_id("admin_Password")
    context.send_keys(PW)
    sleep(2)
    # Login
    commit = AP_Info.driver.find_element_by_id("logIn_btn").click()
    sleep(10)
    return


def AP_WiFiEnter():
    # Settings
    AP_Info.driver.find_element_by_xpath("//div[@id='routerInfo_circle']/img").click()
    sleep(2)
    # Wireless
    AP_Info.driver.find_element_by_xpath("//div[@id='router_right']/div[4]/div/a").click()
    sleep(10)


def AP_24GSettings():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[1]/span")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[1]/span").click()
    sleep(3)


def AP_5GSettings():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[1]/span")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("//span[@onclick='showAdv(\"5\")']").click()
    sleep(3)


def AP_24GWPA():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/a[1]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/ul/li[8]/a").click()
    sleep(3)


def AP_24GWPA2():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/a[1]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/ul/li[7]/a").click()
    sleep(3)


def AP_24GWPA3():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/a[1]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[1]/td/div/div/ul/li[5]/a").click()
    sleep(2)
    # ok
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[6]/div/table/tbody/tr[2]/td/button[1]").click()
    sleep(3)


def AP_5GWPA():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # Security Mode-WPA
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/a[1]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/ul/li[8]/a").click()
    sleep(3)


def AP_5GWPA2():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # Security Mode-WPA2
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/a[1]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/ul/li[7]/a").click()
    sleep(3)


def AP_5GWPA3():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # Security Mode-WPA3
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/a[1]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[1]/td/div/div/ul/li[5]/a").click()
    sleep(2)
    # ok
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[6]/div/table/tbody/tr[2]/td/button[1]").click()
    sleep(3)


def AP_24G80211n():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[2]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # 802.11 Mode_only n
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[2]/td/div/div/a[1]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[2]/td/div/div/ul/li[3]/a").click()
    sleep(3)


def AP_24G80211gn():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[2]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # 802.11 Mode_g/n
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[2]/td/div/div/a[1]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[2]/td/div/div/ul/li[2]/a").click()
    sleep(3)


def AP_24G80211bgn():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[2]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[2]/td/div/div/a[1]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[2]/td/div/div/ul/li[1]/a").click()
    sleep(3)


def AP_5G80211n():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # 802.11 Mode_only n
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/a[1]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/ul/li[7]/a").click()
    sleep(3) 


def AP_5G80211a():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # 802.11 Mode_only a
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/a[1]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/ul/li[6]/a").click()
    sleep(3)


def AP_5G80211ac():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # 802.11 Mode_only ac
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/a[1]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/ul/li[5]/a").click()
    sleep(3)


def AP_5G80211ax():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/a[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # 802.11 Mode_a/n/ac/ax
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/a[1]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[2]/td/div/div/ul/li[1]/a").click()
    sleep(3)

def AP_24GAuto():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[1]/a").click()
    sleep(3)

def AP_24GCH1():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[2]/a").click()
    sleep(3)

def AP_24GCH2():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[3]/a").click()
    sleep(3)
    
def AP_24GCH3():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[4]/a").click()
    sleep(3)

def AP_24GCH4():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[5]/a").click()
    sleep(3)

def AP_24GCH5():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[6]/a").click()
    sleep(3)

def AP_24GCH6():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[7]/a").click()
    sleep(3)

def AP_24GCH7():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[8]/a").click()
    sleep(3)

def AP_24GCH8():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[9]/a").click()
    sleep(3)

def AP_24GCH9():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[10]/a").click()
    sleep(3)

def AP_24GCH10():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[11]/a").click()
    sleep(3)

def AP_24GCH11():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[12]/a").click()
    sleep(3)

def AP_5GAuto():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[1]/a").click()
    sleep(3)

def AP_5GCH36():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[2]/a").click()
    sleep(3)

def AP_5GCH40():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[3]/a").click()
    sleep(3)

def AP_5GCH44():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[4]/a").click()
    sleep(3)

def AP_5GCH48():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[5]/a").click()
    sleep(3)

def AP_5GCH149():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[6]/a").click()
    sleep(3)

def AP_5GCH153():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[7]/a").click()
    sleep(3)

def AP_5GCH157():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[8]/a").click()
    sleep(3)

def AP_5GCH161():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[9]/a").click()
    sleep(3)

def AP_5GCH165():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/a[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[5]/div[2]/table/tbody/tr[3]/td/div/div/ul/li[10]/a").click()
    sleep(3)


def AP_24GWPASSIDConnect():
    # Web move to Up
    js = "var q=document.documentElement.scrollTop=0"
    AP_Info.driver.execute_script(js)
    sleep(2)
    SSIDFrame24 = WifiInfo.SSIDFrame24.get()
    PWFrame24 = WifiInfo.PWFrame24.get()
    #save
    AP_Info.driver.find_element_by_id("Save_btn").click()
    sleep(35)
    AP_Info.driver.find_element_by_id("popalert_ok").click()
    sleep(5)
    # SSID connect
    SSIDclear = os.popen('adb shell pm clear com.steinwurf.adbjoinwifi')
    sleep(5)
    SSIDconnect = os.popen(
        'adb shell am start -n com.steinwurf.adbjoinwifi/com.steinwurf.adbjoinwifi.MainActivity -e ssid ' + SSIDFrame24 + ' -e password_type WPA -e password ' + PWFrame24)
    sleep(5)
    # Home key
    keyevent = os.popen('adb shell input keyevent 3')
    sleep(10)


def AP_5GWPASSIDConnect():
    # Web move to Up
    js = "var q=document.documentElement.scrollTop=0"
    AP_Info.driver.execute_script(js)
    sleep(2)
    SSIDFrame5 = WifiInfo.SSIDFrame5.get()
    PWFrame5 = WifiInfo.PWFrame5.get()
    #save
    AP_Info.driver.find_element_by_id("Save_btn").click()
    sleep(35)
    AP_Info.driver.find_element_by_id("popalert_ok").click()
    sleep(5)
    # SSID connect
    SSIDclear = os.popen('adb shell pm clear com.steinwurf.adbjoinwifi')
    sleep(5)
    SSIDconnect = os.popen(
        'adb shell am start -n com.steinwurf.adbjoinwifi/com.steinwurf.adbjoinwifi.MainActivity -e ssid ' + SSIDFrame5 + ' -e password_type WPA -e password ' + PWFrame5)
    sleep(5)
    # Home key
    keyevent = os.popen('adb shell input keyevent 3')
    sleep(10)


def AP_WPA3SSIDConnect():
    # Web move to Up
    js = "var q=document.documentElement.scrollTop=0"
    AP_Info.driver.execute_script(js)
    sleep(2)
    # save
    AP_Info.driver.find_element_by_id("Save_btn").click()
    sleep(35)
    AP_Info.driver.find_element_by_id("popalert_ok").click()
    sleep(5)


def WifiTriggerOnOff():
    LogTextBoxUpdate("TV Wifi Trigger Off/On Test" + '\n')
    # WiFi off/on
    wifiDisable = os.popen('adb shell svc wifi disable')
    print("WiFi Disable")
    LogTextBoxUpdate("TV WiFi Disable" + '\n')
    sleep(5)
    wifiDisable = os.popen('adb shell svc wifi enable')
    print("WiFi Enable")
    LogTextBoxUpdate("TV WiFi Enable" + '\n')
    sleep(15)


def DCTriggerOnOff():
    LogTextBoxUpdate("TV DC Trigger Off/On Test" + '\n')
    # Power key - turn off
    keyevent = os.popen('adb shell input keyevent 26')
    print("DC Off")
    LogTextBoxUpdate("DC Off" + '\n')
    sleep(10)
    # Power key - turn on
    keyevent = os.popen('adb shell input keyevent 26')
    print("DC On")
    LogTextBoxUpdate("DC On" + '\n')
    sleep(15)


def ACTriggerOnOff():
    LogTextBoxUpdate("TV AC Trigger Off/On Test" + '\n')
    sleep(2)
    AcControl('ac1', 'off')
    sleep(2)
    AcControl('ac2', 'off')
    sleep(8)
    print("Device reboot.... wait for device turn on")
    AcControl('ac1', 'on')
    sleep(2)
    AcControl('ac2', 'on')
    LogTextBoxUpdate("Device reboot.... wait for device turn on" + '\n')
    sleep(30)
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[1]/span")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(30)
    # 2.4g disable
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/table/tbody/tr[2]/td/label/span[2]").click()
    sleep(30)
    # 2.4g enable
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/table/tbody/tr[2]/td/label/span").click()
    sleep(20)
    keyevent = os.popen('adb shell input keyevent 3')
    sleep(10)


def APTriggerOnOff():
    LogTextBoxUpdate("AP Wifi Trigger Off/On Test" + '\n')
    keyevent = os.popen('adb shell input keyevent 3')
    sleep(3)
    LogTextBoxUpdate("AP WiFi Disable" + '\n')
    # Web move to 2.4g setting
    #target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[1]/span")
    #AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(3)
    # 2.4g disable
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/table/tbody/tr[2]/td/label/span[2]").click()
    sleep(2)
    # Web move to 5g setting
    target = AP_Info.driver.find_element_by_xpath("//span[@onclick='showAdv(\"5\")']")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # 5g diable
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/table/tbody/tr[2]/td/label/span[2]").click()
    sleep(2)
    # Save
    js = "var q=document.documentElement.scrollTop=0"
    AP_Info.driver.execute_script(js)
    sleep(2)
    AP_Info.driver.find_element_by_id("Save_btn").click()
    sleep(35)
    AP_Info.driver.find_element_by_id("popalert_ok").click()
    sleep(5)

    # Web move to 2.4g setting
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[1]/div[4]/div[3]/div[4]/div[1]/span")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # 2.4g enable
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[4]/table/tbody/tr[2]/td/label/span").click()
    sleep(2)
    # Web move to 5g setting
    target = AP_Info.driver.find_element_by_xpath("//span[@onclick='showAdv(\"5\")']")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # 5g enable
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[1]/div[4]/div[3]/div[5]/table/tbody/tr[2]/td/label/span").click()
    sleep(2)
    # Save
    js = "var q=document.documentElement.scrollTop=0"
    AP_Info.driver.execute_script(js)
    sleep(2)
    AP_Info.driver.find_element_by_id("Save_btn").click()
    sleep(35)
    AP_Info.driver.find_element_by_id("popalert_ok").click()
    sleep(15)

def ConnectionTest():
    sleep(15)

def Pingip():
    sleep(1)

WifiEventList = [
    ["0001_2.4G_WPA_802.11n_-_Auto_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_Auto_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0002_2.4G_WPA_802.11n_-_Auto_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_Auto_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0003_2.4G_WPA_802.11n_-_Auto_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_Auto_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0004_2.4G_WPA_802.11n_-_Auto_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_Auto_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0005_2.4G_WPA_802.11n_-_Auto_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_Auto_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],     
    ["0006_2.4G_WPA_802.11n_-_CH1_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH1_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0007_2.4G_WPA_802.11n_-_CH1_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH1_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0008_2.4G_WPA_802.11n_-_CH1_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH1_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0009_2.4G_WPA_802.11n_-_CH1_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH1_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0010_2.4G_WPA_802.11n_-_CH1_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH1_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0011_2.4G_WPA_802.11n_-_CH2_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH2_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0012_2.4G_WPA_802.11n_-_CH2_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH2_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0013_2.4G_WPA_802.11n_-_CH2_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH2_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0014_2.4G_WPA_802.11n_-_CH2_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH2_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0015_2.4G_WPA_802.11n_-_CH2_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH2_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0016_2.4G_WPA_802.11n_-_CH3_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH3_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0017_2.4G_WPA_802.11n_-_CH3_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH3_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0018_2.4G_WPA_802.11n_-_CH3_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH3_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0019_2.4G_WPA_802.11n_-_CH3_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH3_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0020_2.4G_WPA_802.11n_-_CH3_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH3_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0021_2.4G_WPA_802.11n_-_CH4_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH4_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0022_2.4G_WPA_802.11n_-_CH4_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH4_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0023_2.4G_WPA_802.11n_-_CH4_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH4_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0024_2.4G_WPA_802.11n_-_CH4_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH4_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0025_2.4G_WPA_802.11n_-_CH4_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH4_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0026_2.4G_WPA_802.11n_-_CH5_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH5_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0027_2.4G_WPA_802.11n_-_CH5_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH5_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0028_2.4G_WPA_802.11n_-_CH5_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH5_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0029_2.4G_WPA_802.11n_-_CH5_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH5_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0030_2.4G_WPA_802.11n_-_CH5_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH5_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0031_2.4G_WPA_802.11n_-_CH6_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH6_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0032_2.4G_WPA_802.11n_-_CH6_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH6_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0033_2.4G_WPA_802.11n_-_CH6_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH6_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0034_2.4G_WPA_802.11n_-_CH6_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH6_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0035_2.4G_WPA_802.11n_-_CH6_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH6_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0036_2.4G_WPA_802.11n_-_CH7_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH7_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0037_2.4G_WPA_802.11n_-_CH7_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH7_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0038_2.4G_WPA_802.11n_-_CH7_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH7_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0039_2.4G_WPA_802.11n_-_CH7_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH7_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0040_2.4G_WPA_802.11n_-_CH7_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH7_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0041_2.4G_WPA_802.11n_-_CH8_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH8_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0042_2.4G_WPA_802.11n_-_CH8_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH8_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0043_2.4G_WPA_802.11n_-_CH8_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH8_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0044_2.4G_WPA_802.11n_-_CH8_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH8_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0045_2.4G_WPA_802.11n_-_CH8_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH8_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0046_2.4G_WPA_802.11n_-_CH9_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH9_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0047_2.4G_WPA_802.11n_-_CH9_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH9_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0048_2.4G_WPA_802.11n_-_CH9_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH9_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0049_2.4G_WPA_802.11n_-_CH9_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH9_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0050_2.4G_WPA_802.11n_-_CH9_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH9_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0051_2.4G_WPA_802.11n_-_CH10_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH10_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0052_2.4G_WPA_802.11n_-_CH10_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH10_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0053_2.4G_WPA_802.11n_-_CH10_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH10_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0054_2.4G_WPA_802.11n_-_CH10_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH10_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0055_2.4G_WPA_802.11n_-_CH10_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH10_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0056_2.4G_WPA_802.11n_-_CH11_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_CH11_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0057_2.4G_WPA_802.11n_-_CH11_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH11_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0058_2.4G_WPA_802.11n_-_CH11_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_CH11_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0059_2.4G_WPA_802.11n_-_CH11_AP_Off/On_", "2.4G_WPA_2.4G-802.11n_CH11_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0060_2.4G_WPA_802.11n_-_CH11_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11n_CH11_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211n, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0061_2.4G_WPA_802.11gn_-_Auto_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_Auto_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0062_2.4G_WPA_802.11gn_-_Auto_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_Auto_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0063_2.4G_WPA_802.11gn_-_Auto_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_Auto_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0064_2.4G_WPA_802.11gn_-_Auto_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_Auto_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0065_2.4G_WPA_802.11gn_-_Auto_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_Auto_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0066_2.4G_WPA_802.11gn_-_CH1_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH1_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0067_2.4G_WPA_802.11gn_-_CH1_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH1_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0068_2.4G_WPA_802.11gn_-_CH1_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH1_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0069_2.4G_WPA_802.11gn_-_CH1_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH1_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0070_2.4G_WPA_802.11gn_-_CH1_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH1_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0071_2.4G_WPA_802.11gn_-_CH2_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH2_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0072_2.4G_WPA_802.11gn_-_CH2_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH2_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0073_2.4G_WPA_802.11gn_-_CH2_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH2_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0074_2.4G_WPA_802.11gn_-_CH2_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH2_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0075_2.4G_WPA_802.11gn_-_CH2_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH2_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0076_2.4G_WPA_802.11gn_-_CH3_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH3_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0077_2.4G_WPA_802.11gn_-_CH3_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH3_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0078_2.4G_WPA_802.11gn_-_CH3_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH3_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0079_2.4G_WPA_802.11gn_-_CH3_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH3_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0080_2.4G_WPA_802.11gn_-_CH3_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH3_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0081_2.4G_WPA_802.11gn_-_CH4_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH4_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0082_2.4G_WPA_802.11gn_-_CH4_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH4_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0083_2.4G_WPA_802.11gn_-_CH4_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH4_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0084_2.4G_WPA_802.11gn_-_CH4_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH4_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0085_2.4G_WPA_802.11gn_-_CH4_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH4_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0086_2.4G_WPA_802.11gn_-_CH5_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH5_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0087_2.4G_WPA_802.11gn_-_CH5_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH5_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0088_2.4G_WPA_802.11gn_-_CH5_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH5_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0089_2.4G_WPA_802.11gn_-_CH5_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH5_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0090_2.4G_WPA_802.11gn_-_CH5_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH5_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0091_2.4G_WPA_802.11gn_-_CH6_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH6_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0092_2.4G_WPA_802.11gn_-_CH6_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH6_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0093_2.4G_WPA_802.11gn_-_CH6_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH6_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0094_2.4G_WPA_802.11gn_-_CH6_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH6_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0095_2.4G_WPA_802.11gn_-_CH6_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH6_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0096_2.4G_WPA_802.11gn_-_CH7_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH7_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0097_2.4G_WPA_802.11gn_-_CH7_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH7_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0098_2.4G_WPA_802.11gn_-_CH7_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH7_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0099_2.4G_WPA_802.11gn_-_CH7_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH7_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0100_2.4G_WPA_802.11gn_-_CH7_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH7_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0101_2.4G_WPA_802.11gn_-_CH8_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH8_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0102_2.4G_WPA_802.11gn_-_CH8_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH8_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0103_2.4G_WPA_802.11gn_-_CH8_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH8_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0104_2.4G_WPA_802.11gn_-_CH8_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH8_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0105_2.4G_WPA_802.11gn_-_CH8_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH8_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0106_2.4G_WPA_802.11gn_-_CH9_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH9_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0107_2.4G_WPA_802.11gn_-_CH9_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH9_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0108_2.4G_WPA_802.11gn_-_CH9_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH9_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0109_2.4G_WPA_802.11gn_-_CH9_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH9_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0110_2.4G_WPA_802.11gn_-_CH9_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH9_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0111_2.4G_WPA_802.11gn_-_CH10_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH10_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0112_2.4G_WPA_802.11gn_-_CH10_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH10_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0113_2.4G_WPA_802.11gn_-_CH10_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH10_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0114_2.4G_WPA_802.11gn_-_CH10_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH10_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0115_2.4G_WPA_802.11gn_-_CH10_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH10_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0116_2.4G_WPA_802.11gn_-_CH11_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH11_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0117_2.4G_WPA_802.11gn_-_CH11_DC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH11_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0118_2.4G_WPA_802.11gn_-_CH11_AC_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH11_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0119_2.4G_WPA_802.11gn_-_CH11_AP_Off/On_", "2.4G_WPA_2.4G-802.11gn_CH11_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0120_2.4G_WPA_802.11gn_-_CH11_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11gn_CH11_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0121_2.4G_WPA_802.11bgn_-_Auto_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_Auto_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0122_2.4G_WPA_802.11bgn_-_Auto_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_Auto_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0123_2.4G_WPA_802.11bgn_-_Auto_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_Auto_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0124_2.4G_WPA_802.11bgn_-_Auto_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_Auto_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0125_2.4G_WPA_802.11bgn_-_Auto_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_Auto_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0126_2.4G_WPA_802.11bgn_-_CH1_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH1_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0127_2.4G_WPA_802.11bgn_-_CH1_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH1_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0128_2.4G_WPA_802.11bgn_-_CH1_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH1_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0129_2.4G_WPA_802.11bgn_-_CH1_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH1_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0130_2.4G_WPA_802.11bgn_-_CH1_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH1_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0131_2.4G_WPA_802.11bgn_-_CH2_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH2_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0132_2.4G_WPA_802.11bgn_-_CH2_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH2_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0133_2.4G_WPA_802.11bgn_-_CH2_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH2_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0134_2.4G_WPA_802.11bgn_-_CH2_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH2_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0135_2.4G_WPA_802.11bgn_-_CH2_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH2_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0136_2.4G_WPA_802.11bgn_-_CH3_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH3_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0137_2.4G_WPA_802.11bgn_-_CH3_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH3_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0138_2.4G_WPA_802.11bgn_-_CH3_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH3_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0139_2.4G_WPA_802.11bgn_-_CH3_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH3_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0140_2.4G_WPA_802.11bgn_-_CH3_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH3_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0141_2.4G_WPA_802.11bgn_-_CH4_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH4_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0142_2.4G_WPA_802.11bgn_-_CH4_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH4_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0143_2.4G_WPA_802.11bgn_-_CH4_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH4_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0144_2.4G_WPA_802.11bgn_-_CH4_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH4_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0145_2.4G_WPA_802.11bgn_-_CH4_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH4_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0146_2.4G_WPA_802.11bgn_-_CH5_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH5_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0147_2.4G_WPA_802.11bgn_-_CH5_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH5_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0148_2.4G_WPA_802.11bgn_-_CH5_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH5_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0149_2.4G_WPA_802.11bgn_-_CH5_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH5_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0150_2.4G_WPA_802.11bgn_-_CH5_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH5_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0151_2.4G_WPA_802.11bgn_-_CH6_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH6_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0152_2.4G_WPA_802.11bgn_-_CH6_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH6_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0153_2.4G_WPA_802.11bgn_-_CH6_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH6_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0154_2.4G_WPA_802.11bgn_-_CH6_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH6_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0155_2.4G_WPA_802.11bgn_-_CH6_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH6_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0156_2.4G_WPA_802.11bgn_-_CH7_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH7_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0157_2.4G_WPA_802.11bgn_-_CH7_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH7_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0158_2.4G_WPA_802.11bgn_-_CH7_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH7_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0159_2.4G_WPA_802.11bgn_-_CH7_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH7_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0160_2.4G_WPA_802.11bgn_-_CH7_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH7_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0161_2.4G_WPA_802.11bgn_-_CH8_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH8_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0162_2.4G_WPA_802.11bgn_-_CH8_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH8_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0163_2.4G_WPA_802.11bgn_-_CH8_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH8_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0164_2.4G_WPA_802.11bgn_-_CH8_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH8_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0165_2.4G_WPA_802.11bgn_-_CH8_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH8_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0166_2.4G_WPA_802.11bgn_-_CH9_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH9_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0167_2.4G_WPA_802.11bgn_-_CH9_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH9_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0168_2.4G_WPA_802.11bgn_-_CH9_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH9_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0169_2.4G_WPA_802.11bgn_-_CH9_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH9_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0170_2.4G_WPA_802.11bgn_-_CH9_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH9_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0171_2.4G_WPA_802.11bgn_-_CH10_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH10_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0172_2.4G_WPA_802.11bgn_-_CH10_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH10_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0173_2.4G_WPA_802.11bgn_-_CH10_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH10_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0174_2.4G_WPA_802.11bgn_-_CH10_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH10_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0175_2.4G_WPA_802.11bgn_-_CH10_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH10_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0176_2.4G_WPA_802.11bgn_-_CH11_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH11_WifiTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0177_2.4G_WPA_802.11bgn_-_CH11_DC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH11_DCTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0178_2.4G_WPA_802.11bgn_-_CH11_AC_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH11_ACTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0179_2.4G_WPA_802.11bgn_-_CH11_AP_Off/On_", "2.4G_WPA_2.4G-802.11bgn_CH11_APTriggerOnOff", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0180_2.4G_WPA_802.11bgn_-_CH11_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11bgn_CH11_ConnectionTest", 
     AP_24GSettings, AP_24GWPA, AP_24G80211bgn, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0181_2.4G_WPA2_802.11n_-_Auto_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_Auto_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0182_2.4G_WPA2_802.11n_-_Auto_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_Auto_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0183_2.4G_WPA2_802.11n_-_Auto_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_Auto_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0184_2.4G_WPA2_802.11n_-_Auto_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_Auto_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0185_2.4G_WPA2_802.11n_-_Auto_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_Auto_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0186_2.4G_WPA2_802.11n_-_CH1_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH1_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0187_2.4G_WPA2_802.11n_-_CH1_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH1_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0188_2.4G_WPA2_802.11n_-_CH1_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH1_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0189_2.4G_WPA2_802.11n_-_CH1_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH1_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0190_2.4G_WPA2_802.11n_-_CH1_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH1_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0191_2.4G_WPA2_802.11n_-_CH2_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH2_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0192_2.4G_WPA2_802.11n_-_CH2_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH2_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0193_2.4G_WPA2_802.11n_-_CH2_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH2_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0194_2.4G_WPA2_802.11n_-_CH2_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH2_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0195_2.4G_WPA2_802.11n_-_CH2_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH2_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0196_2.4G_WPA2_802.11n_-_CH3_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH3_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0197_2.4G_WPA2_802.11n_-_CH3_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH3_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0198_2.4G_WPA2_802.11n_-_CH3_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH3_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0199_2.4G_WPA2_802.11n_-_CH3_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH3_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0200_2.4G_WPA2_802.11n_-_CH3_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH3_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0201_2.4G_WPA2_802.11n_-_CH4_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH4_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0202_2.4G_WPA2_802.11n_-_CH4_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH4_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0203_2.4G_WPA2_802.11n_-_CH4_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH4_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0204_2.4G_WPA2_802.11n_-_CH4_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH4_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0205_2.4G_WPA2_802.11n_-_CH4_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH4_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0206_2.4G_WPA2_802.11n_-_CH5_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH5_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0207_2.4G_WPA2_802.11n_-_CH5_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH5_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0208_2.4G_WPA2_802.11n_-_CH5_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH5_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0209_2.4G_WPA2_802.11n_-_CH5_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH5_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0210_2.4G_WPA2_802.11n_-_CH5_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH5_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0211_2.4G_WPA2_802.11n_-_CH6_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH6_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0212_2.4G_WPA2_802.11n_-_CH6_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH6_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0213_2.4G_WPA2_802.11n_-_CH6_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH6_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0214_2.4G_WPA2_802.11n_-_CH6_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH6_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0215_2.4G_WPA2_802.11n_-_CH6_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH6_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0216_2.4G_WPA2_802.11n_-_CH7_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH7_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0217_2.4G_WPA2_802.11n_-_CH7_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH7_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0218_2.4G_WPA2_802.11n_-_CH7_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH7_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0219_2.4G_WPA2_802.11n_-_CH7_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH7_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0220_2.4G_WPA2_802.11n_-_CH7_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH7_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0221_2.4G_WPA2_802.11n_-_CH8_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH8_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0222_2.4G_WPA2_802.11n_-_CH8_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH8_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0223_2.4G_WPA2_802.11n_-_CH8_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH8_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0224_2.4G_WPA2_802.11n_-_CH8_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH8_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0225_2.4G_WPA2_802.11n_-_CH8_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH8_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0226_2.4G_WPA2_802.11n_-_CH9_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH9_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0227_2.4G_WPA2_802.11n_-_CH9_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH9_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0228_2.4G_WPA2_802.11n_-_CH9_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH9_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0229_2.4G_WPA2_802.11n_-_CH9_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH9_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0230_2.4G_WPA2_802.11n_-_CH9_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH9_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0231_2.4G_WPA2_802.11n_-_CH10_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH10_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0232_2.4G_WPA2_802.11n_-_CH10_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH10_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0233_2.4G_WPA2_802.11n_-_CH10_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH10_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0234_2.4G_WPA2_802.11n_-_CH10_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH10_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0235_2.4G_WPA2_802.11n_-_CH10_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH10_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0236_2.4G_WPA2_802.11n_-_CH11_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH11_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0237_2.4G_WPA2_802.11n_-_CH11_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH11_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0238_2.4G_WPA2_802.11n_-_CH11_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH11_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0239_2.4G_WPA2_802.11n_-_CH11_AP_Off/On_", "2.4G_WPA2_2.4G-802.11n_CH11_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0240_2.4G_WPA2_802.11n_-_CH11_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11n_CH11_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211n, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0241_2.4G_WPA2_802.11gn_-_Auto_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_Auto_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0242_2.4G_WPA2_802.11gn_-_Auto_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_Auto_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0243_2.4G_WPA2_802.11gn_-_Auto_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_Auto_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0244_2.4G_WPA2_802.11gn_-_Auto_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_Auto_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0245_2.4G_WPA2_802.11gn_-_Auto_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_Auto_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0246_2.4G_WPA2_802.11gn_-_CH1_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH1_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0247_2.4G_WPA2_802.11gn_-_CH1_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH1_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0248_2.4G_WPA2_802.11gn_-_CH1_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH1_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0249_2.4G_WPA2_802.11gn_-_CH1_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH1_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0250_2.4G_WPA2_802.11gn_-_CH1_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH1_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0251_2.4G_WPA2_802.11gn_-_CH2_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH2_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0252_2.4G_WPA2_802.11gn_-_CH2_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH2_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0253_2.4G_WPA2_802.11gn_-_CH2_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH2_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0254_2.4G_WPA2_802.11gn_-_CH2_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH2_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0255_2.4G_WPA2_802.11gn_-_CH2_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH2_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0256_2.4G_WPA2_802.11gn_-_CH3_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH3_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0257_2.4G_WPA2_802.11gn_-_CH3_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH3_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0258_2.4G_WPA2_802.11gn_-_CH3_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH3_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0259_2.4G_WPA2_802.11gn_-_CH3_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH3_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0260_2.4G_WPA2_802.11gn_-_CH3_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH3_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0261_2.4G_WPA2_802.11gn_-_CH4_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH4_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0262_2.4G_WPA2_802.11gn_-_CH4_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH4_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0263_2.4G_WPA2_802.11gn_-_CH4_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH4_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0264_2.4G_WPA2_802.11gn_-_CH4_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH4_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0265_2.4G_WPA2_802.11gn_-_CH4_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH4_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0266_2.4G_WPA2_802.11gn_-_CH5_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH5_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0267_2.4G_WPA2_802.11gn_-_CH5_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH5_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0268_2.4G_WPA2_802.11gn_-_CH5_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH5_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0269_2.4G_WPA2_802.11gn_-_CH5_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH5_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0270_2.4G_WPA2_802.11gn_-_CH5_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH5_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0271_2.4G_WPA2_802.11gn_-_CH6_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH6_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0272_2.4G_WPA2_802.11gn_-_CH6_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH6_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0273_2.4G_WPA2_802.11gn_-_CH6_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH6_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0274_2.4G_WPA2_802.11gn_-_CH6_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH6_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0275_2.4G_WPA2_802.11gn_-_CH6_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH6_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0276_2.4G_WPA2_802.11gn_-_CH7_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH7_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0277_2.4G_WPA2_802.11gn_-_CH7_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH7_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0278_2.4G_WPA2_802.11gn_-_CH7_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH7_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0279_2.4G_WPA2_802.11gn_-_CH7_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH7_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0280_2.4G_WPA2_802.11gn_-_CH7_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH7_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0281_2.4G_WPA2_802.11gn_-_CH8_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH8_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0282_2.4G_WPA2_802.11gn_-_CH8_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH8_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0283_2.4G_WPA2_802.11gn_-_CH8_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH8_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0284_2.4G_WPA2_802.11gn_-_CH8_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH8_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0285_2.4G_WPA2_802.11gn_-_CH8_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH8_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0286_2.4G_WPA2_802.11gn_-_CH9_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH9_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0287_2.4G_WPA2_802.11gn_-_CH9_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH9_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0288_2.4G_WPA2_802.11gn_-_CH9_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH9_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0289_2.4G_WPA2_802.11gn_-_CH9_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH9_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0290_2.4G_WPA2_802.11gn_-_CH9_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH9_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0291_2.4G_WPA2_802.11gn_-_CH10_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH10_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0292_2.4G_WPA2_802.11gn_-_CH10_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH10_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0293_2.4G_WPA2_802.11gn_-_CH10_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH10_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0294_2.4G_WPA2_802.11gn_-_CH10_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH10_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0295_2.4G_WPA2_802.11gn_-_CH10_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH10_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0296_2.4G_WPA2_802.11gn_-_CH11_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH11_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0297_2.4G_WPA2_802.11gn_-_CH11_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH11_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0298_2.4G_WPA2_802.11gn_-_CH11_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH11_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0299_2.4G_WPA2_802.11gn_-_CH11_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH11_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0300_2.4G_WPA2_802.11gn_-_CH11_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH11_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0301_2.4G_WPA2_802.11bgn_-_Auto_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_Auto_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0302_2.4G_WPA2_802.11bgn_-_Auto_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_Auto_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0303_2.4G_WPA2_802.11bgn_-_Auto_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_Auto_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0304_2.4G_WPA2_802.11bgn_-_Auto_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_Auto_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0305_2.4G_WPA2_802.11bgn_-_Auto_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_Auto_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0306_2.4G_WPA2_802.11bgn_-_CH1_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH1_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0307_2.4G_WPA2_802.11bgn_-_CH1_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH1_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0308_2.4G_WPA2_802.11bgn_-_CH1_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH1_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0309_2.4G_WPA2_802.11bgn_-_CH1_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH1_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0310_2.4G_WPA2_802.11bgn_-_CH1_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH1_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0311_2.4G_WPA2_802.11bgn_-_CH2_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH2_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0312_2.4G_WPA2_802.11bgn_-_CH2_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH2_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0313_2.4G_WPA2_802.11bgn_-_CH2_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH2_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0314_2.4G_WPA2_802.11bgn_-_CH2_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH2_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0315_2.4G_WPA2_802.11bgn_-_CH2_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH2_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0316_2.4G_WPA2_802.11bgn_-_CH3_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH3_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0317_2.4G_WPA2_802.11bgn_-_CH3_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH3_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0318_2.4G_WPA2_802.11bgn_-_CH3_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH3_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0319_2.4G_WPA2_802.11bgn_-_CH3_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH3_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0320_2.4G_WPA2_802.11bgn_-_CH3_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH3_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0321_2.4G_WPA2_802.11bgn_-_CH4_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH4_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0322_2.4G_WPA2_802.11bgn_-_CH4_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH4_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0323_2.4G_WPA2_802.11bgn_-_CH4_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH4_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0324_2.4G_WPA2_802.11bgn_-_CH4_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH4_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0325_2.4G_WPA2_802.11bgn_-_CH4_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH4_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0326_2.4G_WPA2_802.11bgn_-_CH5_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH5_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0327_2.4G_WPA2_802.11bgn_-_CH5_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH5_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0328_2.4G_WPA2_802.11bgn_-_CH5_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH5_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0329_2.4G_WPA2_802.11bgn_-_CH5_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH5_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0330_2.4G_WPA2_802.11bgn_-_CH5_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH5_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0331_2.4G_WPA2_802.11bgn_-_CH6_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH6_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0332_2.4G_WPA2_802.11bgn_-_CH6_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH6_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0333_2.4G_WPA2_802.11bgn_-_CH6_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH6_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0334_2.4G_WPA2_802.11bgn_-_CH6_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH6_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0335_2.4G_WPA2_802.11bgn_-_CH6_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH6_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0336_2.4G_WPA2_802.11bgn_-_CH7_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH7_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0337_2.4G_WPA2_802.11bgn_-_CH7_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH7_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0338_2.4G_WPA2_802.11bgn_-_CH7_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH7_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0339_2.4G_WPA2_802.11bgn_-_CH7_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH7_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0340_2.4G_WPA2_802.11bgn_-_CH7_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH7_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0341_2.4G_WPA2_802.11bgn_-_CH8_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH8_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0342_2.4G_WPA2_802.11bgn_-_CH8_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH8_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0343_2.4G_WPA2_802.11bgn_-_CH8_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH8_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0344_2.4G_WPA2_802.11bgn_-_CH8_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH8_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0345_2.4G_WPA2_802.11bgn_-_CH8_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH8_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0346_2.4G_WPA2_802.11bgn_-_CH9_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH9_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0347_2.4G_WPA2_802.11bgn_-_CH9_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH9_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0348_2.4G_WPA2_802.11bgn_-_CH9_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH9_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0349_2.4G_WPA2_802.11bgn_-_CH9_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH9_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0350_2.4G_WPA2_802.11bgn_-_CH9_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH9_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0351_2.4G_WPA2_802.11bgn_-_CH10_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH10_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0352_2.4G_WPA2_802.11bgn_-_CH10_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH10_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0353_2.4G_WPA2_802.11bgn_-_CH10_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH10_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0354_2.4G_WPA2_802.11bgn_-_CH10_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH10_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0355_2.4G_WPA2_802.11bgn_-_CH10_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH10_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0356_2.4G_WPA2_802.11bgn_-_CH11_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH11_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0357_2.4G_WPA2_802.11bgn_-_CH11_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH11_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0358_2.4G_WPA2_802.11bgn_-_CH11_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH11_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0359_2.4G_WPA2_802.11bgn_-_CH11_AP_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_CH11_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0360_2.4G_WPA2_802.11bgn_-_CH11_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11bgn_CH11_ConnectionTest",
     AP_24GSettings, AP_24GWPA2, AP_24G80211bgn, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["0361_2.4G_WPA3_802.11n_-_Auto_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_Auto_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GAuto, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0362_2.4G_WPA3_802.11n_-_Auto_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_Auto_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GAuto, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0363_2.4G_WPA3_802.11n_-_Auto_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_Auto_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GAuto, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0364_2.4G_WPA3_802.11n_-_Auto_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_Auto_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GAuto, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0365_2.4G_WPA3_802.11n_-_Auto_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_Auto_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GAuto, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0366_2.4G_WPA3_802.11n_-_CH1_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH1_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH1, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0367_2.4G_WPA3_802.11n_-_CH1_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH1_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH1, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0368_2.4G_WPA3_802.11n_-_CH1_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH1_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH1, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0369_2.4G_WPA3_802.11n_-_CH1_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH1_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH1, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0370_2.4G_WPA3_802.11n_-_CH1_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH1_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH1, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0371_2.4G_WPA3_802.11n_-_CH2_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH2_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH2, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0372_2.4G_WPA3_802.11n_-_CH2_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH2_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH2, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0373_2.4G_WPA3_802.11n_-_CH2_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH2_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH2, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0374_2.4G_WPA3_802.11n_-_CH2_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH2_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH2, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0375_2.4G_WPA3_802.11n_-_CH2_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH2_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH2, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0376_2.4G_WPA3_802.11n_-_CH3_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH3_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH3, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0377_2.4G_WPA3_802.11n_-_CH3_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH3_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH3, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0378_2.4G_WPA3_802.11n_-_CH3_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH3_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH3, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0379_2.4G_WPA3_802.11n_-_CH3_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH3_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH3, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0380_2.4G_WPA3_802.11n_-_CH3_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH3_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH3, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0381_2.4G_WPA3_802.11n_-_CH4_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH4_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH4, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0382_2.4G_WPA3_802.11n_-_CH4_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH4_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH4, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0383_2.4G_WPA3_802.11n_-_CH4_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH4_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH4, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0384_2.4G_WPA3_802.11n_-_CH4_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH4_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH4, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0385_2.4G_WPA3_802.11n_-_CH4_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH4_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH4, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0386_2.4G_WPA3_802.11n_-_CH5_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH5_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH5, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0387_2.4G_WPA3_802.11n_-_CH5_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH5_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH5, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0388_2.4G_WPA3_802.11n_-_CH5_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH5_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH5, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0389_2.4G_WPA3_802.11n_-_CH5_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH5_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH5, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0390_2.4G_WPA3_802.11n_-_CH5_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH5_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH5, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0391_2.4G_WPA3_802.11n_-_CH6_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH6_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH6, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0392_2.4G_WPA3_802.11n_-_CH6_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH6_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH6, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0393_2.4G_WPA3_802.11n_-_CH6_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH6_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH6, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0394_2.4G_WPA3_802.11n_-_CH6_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH6_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH6, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0395_2.4G_WPA3_802.11n_-_CH6_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH6_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH6, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0396_2.4G_WPA3_802.11n_-_CH7_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH7_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH7, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0397_2.4G_WPA3_802.11n_-_CH7_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH7_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH7, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0398_2.4G_WPA3_802.11n_-_CH7_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH7_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH7, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0399_2.4G_WPA3_802.11n_-_CH7_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH7_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH7, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0400_2.4G_WPA3_802.11n_-_CH7_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH7_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH7, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0401_2.4G_WPA3_802.11n_-_CH8_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH8_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH8, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0402_2.4G_WPA3_802.11n_-_CH8_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH8_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH8, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0403_2.4G_WPA3_802.11n_-_CH8_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH8_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH8, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0404_2.4G_WPA3_802.11n_-_CH8_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH8_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH8, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0405_2.4G_WPA3_802.11n_-_CH8_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH8_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH8, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0406_2.4G_WPA3_802.11n_-_CH9_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH9_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH9, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0407_2.4G_WPA3_802.11n_-_CH9_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH9_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH9, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0408_2.4G_WPA3_802.11n_-_CH9_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH9_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH9, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0409_2.4G_WPA3_802.11n_-_CH9_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH9_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH9, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0410_2.4G_WPA3_802.11n_-_CH9_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH9_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH9, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0411_2.4G_WPA3_802.11n_-_CH10_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH10_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH10, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0412_2.4G_WPA3_802.11n_-_CH10_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH10_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH10, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0413_2.4G_WPA3_802.11n_-_CH10_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH10_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH10, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0414_2.4G_WPA3_802.11n_-_CH10_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH10_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH10, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0415_2.4G_WPA3_802.11n_-_CH10_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH10_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH10, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0416_2.4G_WPA3_802.11n_-_CH11_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH11_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH11, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0417_2.4G_WPA3_802.11n_-_CH11_DC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH11_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH11, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0418_2.4G_WPA3_802.11n_-_CH11_AC_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH11_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH11, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0419_2.4G_WPA3_802.11n_-_CH11_AP_Off/On_", "2.4G_WPA3_2.4G-802.11n_CH11_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH11, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0420_2.4G_WPA3_802.11n_-_CH11_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11n_CH11_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211n, AP_24GCH11, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0421_2.4G_WPA3_802.11gn_-_Auto_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_Auto_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GAuto, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0422_2.4G_WPA3_802.11gn_-_Auto_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_Auto_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GAuto, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0423_2.4G_WPA3_802.11gn_-_Auto_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_Auto_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GAuto, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0424_2.4G_WPA3_802.11gn_-_Auto_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_Auto_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GAuto, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0425_2.4G_WPA3_802.11gn_-_Auto_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_Auto_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GAuto, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0426_2.4G_WPA3_802.11gn_-_CH1_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH1_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH1, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0427_2.4G_WPA3_802.11gn_-_CH1_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH1_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH1, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0428_2.4G_WPA3_802.11gn_-_CH1_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH1_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH1, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0429_2.4G_WPA3_802.11gn_-_CH1_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH1_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH1, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0430_2.4G_WPA3_802.11gn_-_CH1_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH1_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH1, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0431_2.4G_WPA3_802.11gn_-_CH2_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH2_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH2, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0432_2.4G_WPA3_802.11gn_-_CH2_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH2_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH2, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0433_2.4G_WPA3_802.11gn_-_CH2_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH2_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH2, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0434_2.4G_WPA3_802.11gn_-_CH2_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH2_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH2, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0435_2.4G_WPA3_802.11gn_-_CH2_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH2_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH2, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0436_2.4G_WPA3_802.11gn_-_CH3_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH3_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH3, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0437_2.4G_WPA3_802.11gn_-_CH3_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH3_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH3, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0438_2.4G_WPA3_802.11gn_-_CH3_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH3_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH3, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0439_2.4G_WPA3_802.11gn_-_CH3_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH3_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH3, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0440_2.4G_WPA3_802.11gn_-_CH3_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH3_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH3, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0441_2.4G_WPA3_802.11gn_-_CH4_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH4_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH4, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0442_2.4G_WPA3_802.11gn_-_CH4_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH4_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH4, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0443_2.4G_WPA3_802.11gn_-_CH4_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH4_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH4, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0444_2.4G_WPA3_802.11gn_-_CH4_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH4_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH4, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0445_2.4G_WPA3_802.11gn_-_CH4_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH4_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH4, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0446_2.4G_WPA3_802.11gn_-_CH5_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH5_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH5, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0447_2.4G_WPA3_802.11gn_-_CH5_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH5_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH5, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0448_2.4G_WPA3_802.11gn_-_CH5_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH5_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH5, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0449_2.4G_WPA3_802.11gn_-_CH5_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH5_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH5, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0450_2.4G_WPA3_802.11gn_-_CH5_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH5_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH5, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0451_2.4G_WPA3_802.11gn_-_CH6_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH6_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH6, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0452_2.4G_WPA3_802.11gn_-_CH6_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH6_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH6, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0453_2.4G_WPA3_802.11gn_-_CH6_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH6_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH6, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0454_2.4G_WPA3_802.11gn_-_CH6_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH6_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH6, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0455_2.4G_WPA3_802.11gn_-_CH6_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH6_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH6, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0456_2.4G_WPA3_802.11gn_-_CH7_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH7_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH7, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0457_2.4G_WPA3_802.11gn_-_CH7_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH7_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH7, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0458_2.4G_WPA3_802.11gn_-_CH7_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH7_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH7, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0459_2.4G_WPA3_802.11gn_-_CH7_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH7_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH7, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0460_2.4G_WPA3_802.11gn_-_CH7_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH7_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH7, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0461_2.4G_WPA3_802.11gn_-_CH8_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH8_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH8, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0462_2.4G_WPA3_802.11gn_-_CH8_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH8_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH8, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0463_2.4G_WPA3_802.11gn_-_CH8_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH8_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH8, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0464_2.4G_WPA3_802.11gn_-_CH8_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH8_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH8, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0465_2.4G_WPA3_802.11gn_-_CH8_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH8_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH8, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0466_2.4G_WPA3_802.11gn_-_CH9_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH9_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH9, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0467_2.4G_WPA3_802.11gn_-_CH9_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH9_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH9, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0468_2.4G_WPA3_802.11gn_-_CH9_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH9_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH9, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0469_2.4G_WPA3_802.11gn_-_CH9_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH9_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH9, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0470_2.4G_WPA3_802.11gn_-_CH9_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH9_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH9, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0471_2.4G_WPA3_802.11gn_-_CH10_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH10_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH10, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0472_2.4G_WPA3_802.11gn_-_CH10_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH10_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH10, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0473_2.4G_WPA3_802.11gn_-_CH10_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH10_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH10, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0474_2.4G_WPA3_802.11gn_-_CH10_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH10_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH10, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0475_2.4G_WPA3_802.11gn_-_CH10_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH10_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH10, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0476_2.4G_WPA3_802.11gn_-_CH11_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH11_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH11, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0477_2.4G_WPA3_802.11gn_-_CH11_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH11_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH11, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0478_2.4G_WPA3_802.11gn_-_CH11_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH11_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH11, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0479_2.4G_WPA3_802.11gn_-_CH11_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH11_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH11, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0480_2.4G_WPA3_802.11gn_-_CH11_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH11_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211gn, AP_24GCH11, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0481_2.4G_WPA3_802.11bgn_-_Auto_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_Auto_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GAuto, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0482_2.4G_WPA3_802.11bgn_-_Auto_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_Auto_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GAuto, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0483_2.4G_WPA3_802.11bgn_-_Auto_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_Auto_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GAuto, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0484_2.4G_WPA3_802.11bgn_-_Auto_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_Auto_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GAuto, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0485_2.4G_WPA3_802.11bgn_-_Auto_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_Auto_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GAuto, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0486_2.4G_WPA3_802.11bgn_-_CH1_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH1_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH1, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0487_2.4G_WPA3_802.11bgn_-_CH1_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH1_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH1, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0488_2.4G_WPA3_802.11bgn_-_CH1_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH1_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH1, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0489_2.4G_WPA3_802.11bgn_-_CH1_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH1_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH1, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0490_2.4G_WPA3_802.11bgn_-_CH1_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH1_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH1, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0491_2.4G_WPA3_802.11bgn_-_CH2_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH2_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH2, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0492_2.4G_WPA3_802.11bgn_-_CH2_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH2_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH2, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0493_2.4G_WPA3_802.11bgn_-_CH2_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH2_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH2, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0494_2.4G_WPA3_802.11bgn_-_CH2_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH2_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH2, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0495_2.4G_WPA3_802.11bgn_-_CH2_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH2_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH2, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0496_2.4G_WPA3_802.11bgn_-_CH3_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH3_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH3, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0497_2.4G_WPA3_802.11bgn_-_CH3_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH3_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH3, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0498_2.4G_WPA3_802.11bgn_-_CH3_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH3_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH3, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0499_2.4G_WPA3_802.11bgn_-_CH3_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH3_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH3, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0500_2.4G_WPA3_802.11bgn_-_CH3_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH3_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH3, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0501_2.4G_WPA3_802.11bgn_-_CH4_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH4_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH4, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0502_2.4G_WPA3_802.11bgn_-_CH4_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH4_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH4, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0503_2.4G_WPA3_802.11bgn_-_CH4_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH4_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH4, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0504_2.4G_WPA3_802.11bgn_-_CH4_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH4_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH4, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0505_2.4G_WPA3_802.11bgn_-_CH4_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH4_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH4, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0506_2.4G_WPA3_802.11bgn_-_CH5_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH5_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH5, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0507_2.4G_WPA3_802.11bgn_-_CH5_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH5_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH5, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0508_2.4G_WPA3_802.11bgn_-_CH5_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH5_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH5, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0509_2.4G_WPA3_802.11bgn_-_CH5_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH5_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH5, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0510_2.4G_WPA3_802.11bgn_-_CH5_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH5_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH5, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0511_2.4G_WPA3_802.11bgn_-_CH6_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH6_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH6, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0512_2.4G_WPA3_802.11bgn_-_CH6_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH6_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH6, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0513_2.4G_WPA3_802.11bgn_-_CH6_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH6_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH6, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0514_2.4G_WPA3_802.11bgn_-_CH6_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH6_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH6, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0515_2.4G_WPA3_802.11bgn_-_CH6_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH6_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH6, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0516_2.4G_WPA3_802.11bgn_-_CH7_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH7_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH7, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0517_2.4G_WPA3_802.11bgn_-_CH7_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH7_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH7, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0518_2.4G_WPA3_802.11bgn_-_CH7_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH7_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH7, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0519_2.4G_WPA3_802.11bgn_-_CH7_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH7_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH7, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0520_2.4G_WPA3_802.11bgn_-_CH7_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH7_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH7, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0521_2.4G_WPA3_802.11bgn_-_CH8_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH8_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH8, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0522_2.4G_WPA3_802.11bgn_-_CH8_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH8_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH8, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0523_2.4G_WPA3_802.11bgn_-_CH8_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH8_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH8, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0524_2.4G_WPA3_802.11bgn_-_CH8_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH8_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH8, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0525_2.4G_WPA3_802.11bgn_-_CH8_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH8_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH8, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0526_2.4G_WPA3_802.11bgn_-_CH9_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH9_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH9, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0527_2.4G_WPA3_802.11bgn_-_CH9_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH9_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH9, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0528_2.4G_WPA3_802.11bgn_-_CH9_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH9_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH9, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0529_2.4G_WPA3_802.11bgn_-_CH9_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH9_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH9, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0530_2.4G_WPA3_802.11bgn_-_CH9_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH9_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH9, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0531_2.4G_WPA3_802.11bgn_-_CH10_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH10_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH10, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0532_2.4G_WPA3_802.11bgn_-_CH10_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH10_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH10, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0533_2.4G_WPA3_802.11bgn_-_CH10_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH10_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH10, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0534_2.4G_WPA3_802.11bgn_-_CH10_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH10_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH10, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0535_2.4G_WPA3_802.11bgn_-_CH10_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH10_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH10, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0536_2.4G_WPA3_802.11bgn_-_CH11_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH11_WifiTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH11, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0537_2.4G_WPA3_802.11bgn_-_CH11_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH11_DCTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH11, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0538_2.4G_WPA3_802.11bgn_-_CH11_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH11_ACTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH11, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0539_2.4G_WPA3_802.11bgn_-_CH11_AP_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_CH11_APTriggerOnOff",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH11, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0540_2.4G_WPA3_802.11bgn_-_CH11_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11bgn_CH11_ConnectionTest",
     AP_24GSettings, AP_24GWPA3, AP_24G80211bgn, AP_24GCH11, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0541_5G_WPA_802.11n_-_Auto_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0542_5G_WPA_802.11n_-_Auto_DC_Off/On_", "5G_WPA_5G-802.11n_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0543_5G_WPA_802.11n_-_Auto_AC_Off/On_", "5G_WPA_5G-802.11n_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0544_5G_WPA_802.11n_-_Auto_AP_Off/On_", "5G_WPA_5G-802.11n_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0545_5G_WPA_802.11n_-_Auto_IP_ConnectionTest_", "5G_WPA_5G-802.11n_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0546_5G_WPA_802.11n_-_CH36_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0547_5G_WPA_802.11n_-_CH36_DC_Off/On_", "5G_WPA_5G-802.11n_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0548_5G_WPA_802.11n_-_CH36_AC_Off/On_", "5G_WPA_5G-802.11n_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0549_5G_WPA_802.11n_-_CH36_AP_Off/On_", "5G_WPA_5G-802.11n_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0550_5G_WPA_802.11n_-_CH36_IP_ConnectionTest_", "5G_WPA_5G-802.11n_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0551_5G_WPA_802.11n_-_CH40_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0552_5G_WPA_802.11n_-_CH40_DC_Off/On_", "5G_WPA_5G-802.11n_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0553_5G_WPA_802.11n_-_CH40_AC_Off/On_", "5G_WPA_5G-802.11n_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0554_5G_WPA_802.11n_-_CH40_AP_Off/On_", "5G_WPA_5G-802.11n_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0555_5G_WPA_802.11n_-_CH40_IP_ConnectionTest_", "5G_WPA_5G-802.11n_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0556_5G_WPA_802.11n_-_CH44_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0557_5G_WPA_802.11n_-_CH44_DC_Off/On_", "5G_WPA_5G-802.11n_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0558_5G_WPA_802.11n_-_CH44_AC_Off/On_", "5G_WPA_5G-802.11n_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0559_5G_WPA_802.11n_-_CH44_AP_Off/On_", "5G_WPA_5G-802.11n_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0560_5G_WPA_802.11n_-_CH44_IP_ConnectionTest_", "5G_WPA_5G-802.11n_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0561_5G_WPA_802.11n_-_CH48_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0562_5G_WPA_802.11n_-_CH48_DC_Off/On_", "5G_WPA_5G-802.11n_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0563_5G_WPA_802.11n_-_CH48_AC_Off/On_", "5G_WPA_5G-802.11n_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0564_5G_WPA_802.11n_-_CH48_AP_Off/On_", "5G_WPA_5G-802.11n_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0565_5G_WPA_802.11n_-_CH48_IP_ConnectionTest_", "5G_WPA_5G-802.11n_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0566_5G_WPA_802.11n_-_CH149_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0567_5G_WPA_802.11n_-_CH149_DC_Off/On_", "5G_WPA_5G-802.11n_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0568_5G_WPA_802.11n_-_CH149_AC_Off/On_", "5G_WPA_5G-802.11n_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0569_5G_WPA_802.11n_-_CH149_AP_Off/On_", "5G_WPA_5G-802.11n_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0570_5G_WPA_802.11n_-_CH149_IP_ConnectionTest_", "5G_WPA_5G-802.11n_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0571_5G_WPA_802.11n_-_CH153_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0572_5G_WPA_802.11n_-_CH153_DC_Off/On_", "5G_WPA_5G-802.11n_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0573_5G_WPA_802.11n_-_CH153_AC_Off/On_", "5G_WPA_5G-802.11n_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0574_5G_WPA_802.11n_-_CH153_AP_Off/On_", "5G_WPA_5G-802.11n_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0575_5G_WPA_802.11n_-_CH153_IP_ConnectionTest_", "5G_WPA_5G-802.11n_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0576_5G_WPA_802.11n_-_CH157_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0577_5G_WPA_802.11n_-_CH157_DC_Off/On_", "5G_WPA_5G-802.11n_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0578_5G_WPA_802.11n_-_CH157_AC_Off/On_", "5G_WPA_5G-802.11n_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0579_5G_WPA_802.11n_-_CH157_AP_Off/On_", "5G_WPA_5G-802.11n_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0580_5G_WPA_802.11n_-_CH157_IP_ConnectionTest_", "5G_WPA_5G-802.11n_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0581_5G_WPA_802.11n_-_CH161_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0582_5G_WPA_802.11n_-_CH161_DC_Off/On_", "5G_WPA_5G-802.11n_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0583_5G_WPA_802.11n_-_CH161_AC_Off/On_", "5G_WPA_5G-802.11n_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0584_5G_WPA_802.11n_-_CH161_AP_Off/On_", "5G_WPA_5G-802.11n_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0585_5G_WPA_802.11n_-_CH161_IP_ConnectionTest_", "5G_WPA_5G-802.11n_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0586_5G_WPA_802.11n_-_CH165_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH165, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0587_5G_WPA_802.11n_-_CH165_DC_Off/On_", "5G_WPA_5G-802.11n_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH165, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0588_5G_WPA_802.11n_-_CH165_AC_Off/On_", "5G_WPA_5G-802.11n_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH165, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0589_5G_WPA_802.11n_-_CH165_AP_Off/On_", "5G_WPA_5G-802.11n_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH165, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0590_5G_WPA_802.11n_-_CH165_IP_ConnectionTest_", "5G_WPA_5G-802.11n_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211n, AP_5GCH165, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0591_5G_WPA_802.11a_-_Auto_TV Wifi_Off/On_", "5G_WPA_5G-802.11a_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0592_5G_WPA_802.11a_-_Auto_DC_Off/On_", "5G_WPA_5G-802.11a_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0593_5G_WPA_802.11a_-_Auto_AC_Off/On_", "5G_WPA_5G-802.11a_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0594_5G_WPA_802.11a_-_Auto_AP_Off/On_", "5G_WPA_5G-802.11a_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0595_5G_WPA_802.11a_-_Auto_IP_ConnectionTest_", "5G_WPA_5G-802.11a_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0596_5G_WPA_802.11a_-_CH36_TV Wifi_Off/On_", "5G_WPA_5G-802.11a_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0597_5G_WPA_802.11a_-_CH36_DC_Off/On_", "5G_WPA_5G-802.11a_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0598_5G_WPA_802.11a_-_CH36_AC_Off/On_", "5G_WPA_5G-802.11a_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0599_5G_WPA_802.11a_-_CH36_AP_Off/On_", "5G_WPA_5G-802.11a_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0600_5G_WPA_802.11a_-_CH36_IP_ConnectionTest_", "5G_WPA_5G-802.11a_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0601_5G_WPA_802.11a_-_CH40_TV Wifi_Off/On_", "5G_WPA_5G-802.11a_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0602_5G_WPA_802.11a_-_CH40_DC_Off/On_", "5G_WPA_5G-802.11a_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0603_5G_WPA_802.11a_-_CH40_AC_Off/On_", "5G_WPA_5G-802.11a_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0604_5G_WPA_802.11a_-_CH40_AP_Off/On_", "5G_WPA_5G-802.11a_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0605_5G_WPA_802.11a_-_CH40_IP_ConnectionTest_", "5G_WPA_5G-802.11a_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0606_5G_WPA_802.11a_-_CH44_TV Wifi_Off/On_", "5G_WPA_5G-802.11a_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0607_5G_WPA_802.11a_-_CH44_DC_Off/On_", "5G_WPA_5G-802.11a_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0608_5G_WPA_802.11a_-_CH44_AC_Off/On_", "5G_WPA_5G-802.11a_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0609_5G_WPA_802.11a_-_CH44_AP_Off/On_", "5G_WPA_5G-802.11a_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0610_5G_WPA_802.11a_-_CH44_IP_ConnectionTest_", "5G_WPA_5G-802.11a_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0611_5G_WPA_802.11a_-_CH48_TV Wifi_Off/On_", "5G_WPA_5G-802.11a_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0612_5G_WPA_802.11a_-_CH48_DC_Off/On_", "5G_WPA_5G-802.11a_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0613_5G_WPA_802.11a_-_CH48_AC_Off/On_", "5G_WPA_5G-802.11a_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0614_5G_WPA_802.11a_-_CH48_AP_Off/On_", "5G_WPA_5G-802.11a_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0615_5G_WPA_802.11a_-_CH48_IP_ConnectionTest_", "5G_WPA_5G-802.11a_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0616_5G_WPA_802.11a_-_CH149_TV Wifi_Off/On_", "5G_WPA_5G-802.11a_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0617_5G_WPA_802.11a_-_CH149_DC_Off/On_", "5G_WPA_5G-802.11a_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0618_5G_WPA_802.11a_-_CH149_AC_Off/On_", "5G_WPA_5G-802.11a_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0619_5G_WPA_802.11a_-_CH149_AP_Off/On_", "5G_WPA_5G-802.11a_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0620_5G_WPA_802.11a_-_CH149_IP_ConnectionTest_", "5G_WPA_5G-802.11a_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0621_5G_WPA_802.11a_-_CH153_TV Wifi_Off/On_", "5G_WPA_5G-802.11a_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0622_5G_WPA_802.11a_-_CH153_DC_Off/On_", "5G_WPA_5G-802.11a_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0623_5G_WPA_802.11a_-_CH153_AC_Off/On_", "5G_WPA_5G-802.11a_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0624_5G_WPA_802.11a_-_CH153_AP_Off/On_", "5G_WPA_5G-802.11a_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0625_5G_WPA_802.11a_-_CH153_IP_ConnectionTest_", "5G_WPA_5G-802.11a_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0626_5G_WPA_802.11a_-_CH157_TV Wifi_Off/On_", "5G_WPA_5G-802.11a_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0627_5G_WPA_802.11a_-_CH157_DC_Off/On_", "5G_WPA_5G-802.11a_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0628_5G_WPA_802.11a_-_CH157_AC_Off/On_", "5G_WPA_5G-802.11a_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0629_5G_WPA_802.11a_-_CH157_AP_Off/On_", "5G_WPA_5G-802.11a_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0630_5G_WPA_802.11a_-_CH157_IP_ConnectionTest_", "5G_WPA_5G-802.11a_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0631_5G_WPA_802.11a_-_CH161_TV Wifi_Off/On_", "5G_WPA_5G-802.11a_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0632_5G_WPA_802.11a_-_CH161_DC_Off/On_", "5G_WPA_5G-802.11a_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0633_5G_WPA_802.11a_-_CH161_AC_Off/On_", "5G_WPA_5G-802.11a_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0634_5G_WPA_802.11a_-_CH161_AP_Off/On_", "5G_WPA_5G-802.11a_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0635_5G_WPA_802.11a_-_CH161_IP_ConnectionTest_", "5G_WPA_5G-802.11a_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0636_5G_WPA_802.11a_-_CH165_TV Wifi_Off/On_", "5G_WPA_5G-802.11a_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH165, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0637_5G_WPA_802.11a_-_CH165_DC_Off/On_", "5G_WPA_5G-802.11a_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH165, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0638_5G_WPA_802.11a_-_CH165_AC_Off/On_", "5G_WPA_5G-802.11a_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH165, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0639_5G_WPA_802.11a_-_CH165_AP_Off/On_", "5G_WPA_5G-802.11a_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH165, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0640_5G_WPA_802.11a_-_CH165_IP_ConnectionTest_", "5G_WPA_5G-802.11a_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211a, AP_5GCH165, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0641_5G_WPA_802.11ac_-_Auto_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0642_5G_WPA_802.11ac_-_Auto_DC_Off/On_", "5G_WPA_5G-802.11ac_Auto_DCTriggerOnOff",    
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0643_5G_WPA_802.11ac_-_Auto_AC_Off/On_", "5G_WPA_5G-802.11ac_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0644_5G_WPA_802.11ac_-_Auto_AP_Off/On_", "5G_WPA_5G-802.11ac_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0645_5G_WPA_802.11ac_-_Auto_IP_ConnectionTest_", "5G_WPA_5G-802.11ac_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0646_5G_WPA_802.11ac_-_CH36_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0647_5G_WPA_802.11ac_-_CH36_DC_Off/On_", "5G_WPA_5G-802.11ac_CH36_DCTriggerOnOff",    
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0648_5G_WPA_802.11ac_-_CH36_AC_Off/On_", "5G_WPA_5G-802.11ac_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0649_5G_WPA_802.11ac_-_CH36_AP_Off/On_", "5G_WPA_5G-802.11ac_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0650_5G_WPA_802.11ac_-_CH36_IP_ConnectionTest_", "5G_WPA_5G-802.11ac_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0651_5G_WPA_802.11ac_-_CH40_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0652_5G_WPA_802.11ac_-_CH40_DC_Off/On_", "5G_WPA_5G-802.11ac_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0653_5G_WPA_802.11ac_-_CH40_AC_Off/On_", "5G_WPA_5G-802.11ac_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0654_5G_WPA_802.11ac_-_CH40_AP_Off/On_", "5G_WPA_5G-802.11ac_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0655_5G_WPA_802.11ac_-_CH40_IP_ConnectionTest_", "5G_WPA_5G-802.11ac_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0656_5G_WPA_802.11ac_-_CH44_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0657_5G_WPA_802.11ac_-_CH44_DC_Off/On_", "5G_WPA_5G-802.11ac_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0658_5G_WPA_802.11ac_-_CH44_AC_Off/On_", "5G_WPA_5G-802.11ac_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0659_5G_WPA_802.11ac_-_CH44_AP_Off/On_", "5G_WPA_5G-802.11ac_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0660_5G_WPA_802.11ac_-_CH44_IP_ConnectionTest_", "5G_WPA_5G-802.11ac_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0661_5G_WPA_802.11ac_-_CH48_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0662_5G_WPA_802.11ac_-_CH48_DC_Off/On_", "5G_WPA_5G-802.11ac_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0663_5G_WPA_802.11ac_-_CH48_AC_Off/On_", "5G_WPA_5G-802.11ac_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0664_5G_WPA_802.11ac_-_CH48_AP_Off/On_", "5G_WPA_5G-802.11ac_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0665_5G_WPA_802.11ac_-_CH48_IP_ConnectionTest_", "5G_WPA_5G-802.11ac_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0666_5G_WPA_802.11ac_-_CH149_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0667_5G_WPA_802.11ac_-_CH149_DC_Off/On_", "5G_WPA_5G-802.11ac_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0668_5G_WPA_802.11ac_-_CH149_AC_Off/On_", "5G_WPA_5G-802.11ac_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0669_5G_WPA_802.11ac_-_CH149_AP_Off/On_", "5G_WPA_5G-802.11ac_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0670_5G_WPA_802.11ac_-_CH149_IP_ConnectionTest_", "5G_WPA_5G-802.11ac_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0671_5G_WPA_802.11ac_-_CH153_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0672_5G_WPA_802.11ac_-_CH153_DC_Off/On_", "5G_WPA_5G-802.11ac_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0673_5G_WPA_802.11ac_-_CH153_AC_Off/On_", "5G_WPA_5G-802.11ac_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0674_5G_WPA_802.11ac_-_CH153_AP_Off/On_", "5G_WPA_5G-802.11ac_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0675_5G_WPA_802.11ac_-_CH153_IP_ConnectionTest_", "5G_WPA_5G-802.11ac_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0676_5G_WPA_802.11ac_-_CH157_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0677_5G_WPA_802.11ac_-_CH157_DC_Off/On_", "5G_WPA_5G-802.11ac_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0678_5G_WPA_802.11ac_-_CH157_AC_Off/On_", "5G_WPA_5G-802.11ac_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0679_5G_WPA_802.11ac_-_CH157_AP_Off/On_", "5G_WPA_5G-802.11ac_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0680_5G_WPA_802.11ac_-_CH157_IP_ConnectionTest_", "5G_WPA_5G-802.11ac_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0681_5G_WPA_802.11ac_-_CH161_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0682_5G_WPA_802.11ac_-_CH161_DC_Off/On_", "5G_WPA_5G-802.11ac_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0683_5G_WPA_802.11ac_-_CH161_AC_Off/On_", "5G_WPA_5G-802.11ac_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0684_5G_WPA_802.11ac_-_CH161_AP_Off/On_", "5G_WPA_5G-802.11ac_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0685_5G_WPA_802.11ac_-_CH161_IP_ConnectionTest_", "5G_WPA_5G-802.11ac_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0686_5G_WPA_802.11ac_-_CH165_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH165, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0687_5G_WPA_802.11ac_-_CH165_DC_Off/On_", "5G_WPA_5G-802.11ac_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH165, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0688_5G_WPA_802.11ac_-_CH165_AC_Off/On_", "5G_WPA_5G-802.11ac_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH165, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0689_5G_WPA_802.11ac_-_CH165_AP_Off/On_", "5G_WPA_5G-802.11ac_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH165, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0690_5G_WPA_802.11ac_-_CH165_IP_ConnectionTest_", "5G_WPA_5G-802.11ac_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ac, AP_5GCH165, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0691_5G_WPA_802.11ax_-_Auto_TV Wifi_Off/On_", "5G_WPA_5G-802.11ax_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0692_5G_WPA_802.11ax_-_Auto_DC_Off/On_", "5G_WPA_5G-802.11ax_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0693_5G_WPA_802.11ax_-_Auto_AC_Off/On_", "5G_WPA_5G-802.11ax_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0694_5G_WPA_802.11ax_-_Auto_AP_Off/On_", "5G_WPA_5G-802.11ax_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0695_5G_WPA_802.11ax_-_Auto_IP_ConnectionTest_", "5G_WPA_5G-802.11ax_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0696_5G_WPA_802.11ax_-_CH36_TV Wifi_Off/On_", "5G_WPA_5G-802.11ax_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0697_5G_WPA_802.11ax_-_CH36_DC_Off/On_", "5G_WPA_5G-802.11ax_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0698_5G_WPA_802.11ax_-_CH36_AC_Off/On_", "5G_WPA_5G-802.11ax_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0699_5G_WPA_802.11ax_-_CH36_AP_Off/On_", "5G_WPA_5G-802.11ax_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0700_5G_WPA_802.11ax_-_CH36_IP_ConnectionTest_", "5G_WPA_5G-802.11ax_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0701_5G_WPA_802.11ax_-_CH40_TV Wifi_Off/On_", "5G_WPA_5G-802.11ax_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0702_5G_WPA_802.11ax_-_CH40_DC_Off/On_", "5G_WPA_5G-802.11ax_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0703_5G_WPA_802.11ax_-_CH40_AC_Off/On_", "5G_WPA_5G-802.11ax_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0704_5G_WPA_802.11ax_-_CH40_AP_Off/On_", "5G_WPA_5G-802.11ax_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0705_5G_WPA_802.11ax_-_CH40_IP_ConnectionTest_", "5G_WPA_5G-802.11ax_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0706_5G_WPA_802.11ax_-_CH44_TV Wifi_Off/On_", "5G_WPA_5G-802.11ax_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0707_5G_WPA_802.11ax_-_CH44_DC_Off/On_", "5G_WPA_5G-802.11ax_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0708_5G_WPA_802.11ax_-_CH44_AC_Off/On_", "5G_WPA_5G-802.11ax_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0709_5G_WPA_802.11ax_-_CH44_AP_Off/On_", "5G_WPA_5G-802.11ax_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0710_5G_WPA_802.11ax_-_CH44_IP_ConnectionTest_", "5G_WPA_5G-802.11ax_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0711_5G_WPA_802.11ax_-_CH48_TV Wifi_Off/On_", "5G_WPA_5G-802.11ax_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0712_5G_WPA_802.11ax_-_CH48_DC_Off/On_", "5G_WPA_5G-802.11ax_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0713_5G_WPA_802.11ax_-_CH48_AC_Off/On_", "5G_WPA_5G-802.11ax_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0714_5G_WPA_802.11ax_-_CH48_AP_Off/On_", "5G_WPA_5G-802.11ax_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0715_5G_WPA_802.11ax_-_CH48_IP_ConnectionTest_", "5G_WPA_5G-802.11ax_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0716_5G_WPA_802.11ax_-_CH149_TV Wifi_Off/On_", "5G_WPA_5G-802.11ax_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0717_5G_WPA_802.11ax_-_CH149_DC_Off/On_", "5G_WPA_5G-802.11ax_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0718_5G_WPA_802.11ax_-_CH149_AC_Off/On_", "5G_WPA_5G-802.11ax_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0719_5G_WPA_802.11ax_-_CH149_AP_Off/On_", "5G_WPA_5G-802.11ax_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0720_5G_WPA_802.11ax_-_CH149_IP_ConnectionTest_", "5G_WPA_5G-802.11ax_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0721_5G_WPA_802.11ax_-_CH153_TV Wifi_Off/On_", "5G_WPA_5G-802.11ax_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0722_5G_WPA_802.11ax_-_CH153_DC_Off/On_", "5G_WPA_5G-802.11ax_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0723_5G_WPA_802.11ax_-_CH153_AC_Off/On_", "5G_WPA_5G-802.11ax_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0724_5G_WPA_802.11ax_-_CH153_AP_Off/On_", "5G_WPA_5G-802.11ax_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0725_5G_WPA_802.11ax_-_CH153_IP_ConnectionTest_", "5G_WPA_5G-802.11ax_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0726_5G_WPA_802.11ax_-_CH157_TV Wifi_Off/On_", "5G_WPA_5G-802.11ax_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0727_5G_WPA_802.11ax_-_CH157_DC_Off/On_", "5G_WPA_5G-802.11ax_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0728_5G_WPA_802.11ax_-_CH157_AC_Off/On_", "5G_WPA_5G-802.11ax_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0729_5G_WPA_802.11ax_-_CH157_AP_Off/On_", "5G_WPA_5G-802.11ax_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0730_5G_WPA_802.11ax_-_CH157_IP_ConnectionTest_", "5G_WPA_5G-802.11ax_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0731_5G_WPA_802.11ax_-_CH161_TV Wifi_Off/On_", "5G_WPA_5G-802.11ax_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0732_5G_WPA_802.11ax_-_CH161_DC_Off/On_", "5G_WPA_5G-802.11ax_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0733_5G_WPA_802.11ax_-_CH161_AC_Off/On_", "5G_WPA_5G-802.11ax_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0734_5G_WPA_802.11ax_-_CH161_AP_Off/On_", "5G_WPA_5G-802.11ax_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0735_5G_WPA_802.11ax_-_CH161_IP_ConnectionTest_", "5G_WPA_5G-802.11ax_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0736_5G_WPA_802.11ax_-_CH165_TV Wifi_Off/On_", "5G_WPA_5G-802.11ax_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH165, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0737_5G_WPA_802.11ax_-_CH165_DC_Off/On_", "5G_WPA_5G-802.11ax_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH165, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0738_5G_WPA_802.11ax_-_CH165_AC_Off/On_", "5G_WPA_5G-802.11ax_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH165, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0739_5G_WPA_802.11ax_-_CH165_AP_Off/On_", "5G_WPA_5G-802.11ax_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH165, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0740_5G_WPA_802.11ax_-_CH165_IP_ConnectionTest_", "5G_WPA_5G-802.11ax_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA, AP_5G80211ax, AP_5GCH165, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0741_5G_WPA2_802.11n_-_Auto_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0742_5G_WPA2_802.11n_-_Auto_DC_Off/On_", "5G_WPA2_5G-802.11n_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0743_5G_WPA2_802.11n_-_Auto_AC_Off/On_", "5G_WPA2_5G-802.11n_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0744_5G_WPA2_802.11n_-_Auto_AP_Off/On_", "5G_WPA2_5G-802.11n_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0745_5G_WPA2_802.11n_-_Auto_IP_ConnectionTest_", "5G_WPA2_5G-802.11n_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0746_5G_WPA2_802.11n_-_CH36_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0747_5G_WPA2_802.11n_-_CH36_DC_Off/On_", "5G_WPA2_5G-802.11n_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0748_5G_WPA2_802.11n_-_CH36_AC_Off/On_", "5G_WPA2_5G-802.11n_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0749_5G_WPA2_802.11n_-_CH36_AP_Off/On_", "5G_WPA2_5G-802.11n_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0750_5G_WPA2_802.11n_-_CH36_IP_ConnectionTest_", "5G_WPA2_5G-802.11n_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0751_5G_WPA2_802.11n_-_CH40_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0752_5G_WPA2_802.11n_-_CH40_DC_Off/On_", "5G_WPA2_5G-802.11n_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0753_5G_WPA2_802.11n_-_CH40_AC_Off/On_", "5G_WPA2_5G-802.11n_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0754_5G_WPA2_802.11n_-_CH40_AP_Off/On_", "5G_WPA2_5G-802.11n_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0755_5G_WPA2_802.11n_-_CH40_IP_ConnectionTest_", "5G_WPA2_5G-802.11n_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0756_5G_WPA2_802.11n_-_CH44_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0757_5G_WPA2_802.11n_-_CH44_DC_Off/On_", "5G_WPA2_5G-802.11n_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0758_5G_WPA2_802.11n_-_CH44_AC_Off/On_", "5G_WPA2_5G-802.11n_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0759_5G_WPA2_802.11n_-_CH44_AP_Off/On_", "5G_WPA2_5G-802.11n_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0760_5G_WPA2_802.11n_-_CH44_IP_ConnectionTest_", "5G_WPA2_5G-802.11n_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0761_5G_WPA2_802.11n_-_CH48_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0762_5G_WPA2_802.11n_-_CH48_DC_Off/On_", "5G_WPA2_5G-802.11n_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0763_5G_WPA2_802.11n_-_CH48_AC_Off/On_", "5G_WPA2_5G-802.11n_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0764_5G_WPA2_802.11n_-_CH48_AP_Off/On_", "5G_WPA2_5G-802.11n_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0765_5G_WPA2_802.11n_-_CH48_IP_ConnectionTest_", "5G_WPA2_5G-802.11n_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0766_5G_WPA2_802.11n_-_CH149_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0767_5G_WPA2_802.11n_-_CH149_DC_Off/On_", "5G_WPA2_5G-802.11n_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0768_5G_WPA2_802.11n_-_CH149_AC_Off/On_", "5G_WPA2_5G-802.11n_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0769_5G_WPA2_802.11n_-_CH149_AP_Off/On_", "5G_WPA2_5G-802.11n_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0770_5G_WPA2_802.11n_-_CH149_IP_ConnectionTest_", "5G_WPA2_5G-802.11n_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0771_5G_WPA2_802.11n_-_CH153_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0772_5G_WPA2_802.11n_-_CH153_DC_Off/On_", "5G_WPA2_5G-802.11n_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0773_5G_WPA2_802.11n_-_CH153_AC_Off/On_", "5G_WPA2_5G-802.11n_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0774_5G_WPA2_802.11n_-_CH153_AP_Off/On_", "5G_WPA2_5G-802.11n_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0775_5G_WPA2_802.11n_-_CH153_IP_ConnectionTest_", "5G_WPA2_5G-802.11n_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0776_5G_WPA2_802.11n_-_CH157_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0777_5G_WPA2_802.11n_-_CH157_DC_Off/On_", "5G_WPA2_5G-802.11n_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0778_5G_WPA2_802.11n_-_CH157_AC_Off/On_", "5G_WPA2_5G-802.11n_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0779_5G_WPA2_802.11n_-_CH157_AP_Off/On_", "5G_WPA2_5G-802.11n_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0780_5G_WPA2_802.11n_-_CH157_IP_ConnectionTest_", "5G_WPA2_5G-802.11n_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0781_5G_WPA2_802.11n_-_CH161_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0782_5G_WPA2_802.11n_-_CH161_DC_Off/On_", "5G_WPA2_5G-802.11n_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0783_5G_WPA2_802.11n_-_CH161_AC_Off/On_", "5G_WPA2_5G-802.11n_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0784_5G_WPA2_802.11n_-_CH161_AP_Off/On_", "5G_WPA2_5G-802.11n_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0785_5G_WPA2_802.11n_-_CH161_IP_ConnectionTest_", "5G_WPA2_5G-802.11n_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0786_5G_WPA2_802.11n_-_CH165_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH165, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0787_5G_WPA2_802.11n_-_CH165_DC_Off/On_", "5G_WPA2_5G-802.11n_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH165, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0788_5G_WPA2_802.11n_-_CH165_AC_Off/On_", "5G_WPA2_5G-802.11n_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH165, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0789_5G_WPA2_802.11n_-_CH165_AP_Off/On_", "5G_WPA2_5G-802.11n_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH165, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0790_5G_WPA2_802.11n_-_CH165_IP_ConnectionTest_", "5G_WPA2_5G-802.11n_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211n, AP_5GCH165, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0791_5G_WPA2_802.11a_-_Auto_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0792_5G_WPA2_802.11a_-_Auto_DC_Off/On_", "5G_WPA2_5G-802.11a_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0793_5G_WPA2_802.11a_-_Auto_AC_Off/On_", "5G_WPA2_5G-802.11a_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0794_5G_WPA2_802.11a_-_Auto_AP_Off/On_", "5G_WPA2_5G-802.11a_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0795_5G_WPA2_802.11a_-_Auto_IP_ConnectionTest_", "5G_WPA2_5G-802.11a_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0796_5G_WPA2_802.11a_-_CH36_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0797_5G_WPA2_802.11a_-_CH36_DC_Off/On_", "5G_WPA2_5G-802.11a_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0798_5G_WPA2_802.11a_-_CH36_AC_Off/On_", "5G_WPA2_5G-802.11a_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0799_5G_WPA2_802.11a_-_CH36_AP_Off/On_", "5G_WPA2_5G-802.11a_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0800_5G_WPA2_802.11a_-_CH36_IP_ConnectionTest_", "5G_WPA2_5G-802.11a_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0801_5G_WPA2_802.11a_-_CH40_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0802_5G_WPA2_802.11a_-_CH40_DC_Off/On_", "5G_WPA2_5G-802.11a_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0803_5G_WPA2_802.11a_-_CH40_AC_Off/On_", "5G_WPA2_5G-802.11a_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0804_5G_WPA2_802.11a_-_CH40_AP_Off/On_", "5G_WPA2_5G-802.11a_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0805_5G_WPA2_802.11a_-_CH40_IP_ConnectionTest_", "5G_WPA2_5G-802.11a_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0806_5G_WPA2_802.11a_-_CH44_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0807_5G_WPA2_802.11a_-_CH44_DC_Off/On_", "5G_WPA2_5G-802.11a_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0808_5G_WPA2_802.11a_-_CH44_AC_Off/On_", "5G_WPA2_5G-802.11a_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0809_5G_WPA2_802.11a_-_CH44_AP_Off/On_", "5G_WPA2_5G-802.11a_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0810_5G_WPA2_802.11a_-_CH44_IP_ConnectionTest_", "5G_WPA2_5G-802.11a_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0811_5G_WPA2_802.11a_-_CH48_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0812_5G_WPA2_802.11a_-_CH48_DC_Off/On_", "5G_WPA2_5G-802.11a_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0813_5G_WPA2_802.11a_-_CH48_AC_Off/On_", "5G_WPA2_5G-802.11a_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0814_5G_WPA2_802.11a_-_CH48_AP_Off/On_", "5G_WPA2_5G-802.11a_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0815_5G_WPA2_802.11a_-_CH48_IP_ConnectionTest_", "5G_WPA2_5G-802.11a_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0816_5G_WPA2_802.11a_-_CH149_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0817_5G_WPA2_802.11a_-_CH149_DC_Off/On_", "5G_WPA2_5G-802.11a_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0818_5G_WPA2_802.11a_-_CH149_AC_Off/On_", "5G_WPA2_5G-802.11a_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0819_5G_WPA2_802.11a_-_CH149_AP_Off/On_", "5G_WPA2_5G-802.11a_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0820_5G_WPA2_802.11a_-_CH149_IP_ConnectionTest_", "5G_WPA2_5G-802.11a_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0821_5G_WPA2_802.11a_-_CH153_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0822_5G_WPA2_802.11a_-_CH153_DC_Off/On_", "5G_WPA2_5G-802.11a_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0823_5G_WPA2_802.11a_-_CH153_AC_Off/On_", "5G_WPA2_5G-802.11a_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0824_5G_WPA2_802.11a_-_CH153_AP_Off/On_", "5G_WPA2_5G-802.11a_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0825_5G_WPA2_802.11a_-_CH153_IP_ConnectionTest_", "5G_WPA2_5G-802.11a_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0826_5G_WPA2_802.11a_-_CH157_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0827_5G_WPA2_802.11a_-_CH157_DC_Off/On_", "5G_WPA2_5G-802.11a_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0828_5G_WPA2_802.11a_-_CH157_AC_Off/On_", "5G_WPA2_5G-802.11a_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0829_5G_WPA2_802.11a_-_CH157_AP_Off/On_", "5G_WPA2_5G-802.11a_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0830_5G_WPA2_802.11a_-_CH157_IP_ConnectionTest_", "5G_WPA2_5G-802.11a_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0831_5G_WPA2_802.11a_-_CH161_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0832_5G_WPA2_802.11a_-_CH161_DC_Off/On_", "5G_WPA2_5G-802.11a_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0833_5G_WPA2_802.11a_-_CH161_AC_Off/On_", "5G_WPA2_5G-802.11a_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0834_5G_WPA2_802.11a_-_CH161_AP_Off/On_", "5G_WPA2_5G-802.11a_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0835_5G_WPA2_802.11a_-_CH161_IP_ConnectionTest_", "5G_WPA2_5G-802.11a_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0836_5G_WPA2_802.11a_-_CH165_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH165, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0837_5G_WPA2_802.11a_-_CH165_DC_Off/On_", "5G_WPA2_5G-802.11a_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH165, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0838_5G_WPA2_802.11a_-_CH165_AC_Off/On_", "5G_WPA2_5G-802.11a_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH165, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0839_5G_WPA2_802.11a_-_CH165_AP_Off/On_", "5G_WPA2_5G-802.11a_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH165, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0840_5G_WPA2_802.11a_-_CH165_IP_ConnectionTest_", "5G_WPA2_5G-802.11a_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211a, AP_5GCH165, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0841_5G_WPA2_802.11ac_-_Auto_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0842_5G_WPA2_802.11ac_-_Auto_DC_Off/On_", "5G_WPA2_5G-802.11ac_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0843_5G_WPA2_802.11ac_-_Auto_AC_Off/On_", "5G_WPA2_5G-802.11ac_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0844_5G_WPA2_802.11ac_-_Auto_AP_Off/On_", "5G_WPA2_5G-802.11ac_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0845_5G_WPA2_802.11ac_-_Auto_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0846_5G_WPA2_802.11ac_-_CH36_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0847_5G_WPA2_802.11ac_-_CH36_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0848_5G_WPA2_802.11ac_-_CH36_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0849_5G_WPA2_802.11ac_-_CH36_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0850_5G_WPA2_802.11ac_-_CH36_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0851_5G_WPA2_802.11ac_-_CH40_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0852_5G_WPA2_802.11ac_-_CH40_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0853_5G_WPA2_802.11ac_-_CH40_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0854_5G_WPA2_802.11ac_-_CH40_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0855_5G_WPA2_802.11ac_-_CH40_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0856_5G_WPA2_802.11ac_-_CH44_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0857_5G_WPA2_802.11ac_-_CH44_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0858_5G_WPA2_802.11ac_-_CH44_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0859_5G_WPA2_802.11ac_-_CH44_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0860_5G_WPA2_802.11ac_-_CH44_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0861_5G_WPA2_802.11ac_-_CH48_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0862_5G_WPA2_802.11ac_-_CH48_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0863_5G_WPA2_802.11ac_-_CH48_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0864_5G_WPA2_802.11ac_-_CH48_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0865_5G_WPA2_802.11ac_-_CH48_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0866_5G_WPA2_802.11ac_-_CH149_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0867_5G_WPA2_802.11ac_-_CH149_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0868_5G_WPA2_802.11ac_-_CH149_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0869_5G_WPA2_802.11ac_-_CH149_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0870_5G_WPA2_802.11ac_-_CH149_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0871_5G_WPA2_802.11ac_-_CH153_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0872_5G_WPA2_802.11ac_-_CH153_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0873_5G_WPA2_802.11ac_-_CH153_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0874_5G_WPA2_802.11ac_-_CH153_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0875_5G_WPA2_802.11ac_-_CH153_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0876_5G_WPA2_802.11ac_-_CH157_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0877_5G_WPA2_802.11ac_-_CH157_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0878_5G_WPA2_802.11ac_-_CH157_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0879_5G_WPA2_802.11ac_-_CH157_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0880_5G_WPA2_802.11ac_-_CH157_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0881_5G_WPA2_802.11ac_-_CH161_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0882_5G_WPA2_802.11ac_-_CH161_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0883_5G_WPA2_802.11ac_-_CH161_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0884_5G_WPA2_802.11ac_-_CH161_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0885_5G_WPA2_802.11ac_-_CH161_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0886_5G_WPA2_802.11ac_-_CH165_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH165, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0887_5G_WPA2_802.11ac_-_CH165_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH165, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0888_5G_WPA2_802.11ac_-_CH165_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH165, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0889_5G_WPA2_802.11ac_-_CH165_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH165, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0890_5G_WPA2_802.11ac_-_CH165_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ac, AP_5GCH165, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0891_5G_WPA2_802.11ax_-_Auto_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0892_5G_WPA2_802.11ax_-_Auto_DC_Off/On_", "5G_WPA2_5G-802.11ax_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0893_5G_WPA2_802.11ax_-_Auto_AC_Off/On_", "5G_WPA2_5G-802.11ax_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0894_5G_WPA2_802.11ax_-_Auto_AP_Off/On_", "5G_WPA2_5G-802.11ax_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0895_5G_WPA2_802.11ax_-_Auto_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0896_5G_WPA2_802.11ax_-_CH36_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0897_5G_WPA2_802.11ax_-_CH36_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0898_5G_WPA2_802.11ax_-_CH36_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0899_5G_WPA2_802.11ax_-_CH36_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0900_5G_WPA2_802.11ax_-_CH36_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0901_5G_WPA2_802.11ax_-_CH40_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0902_5G_WPA2_802.11ax_-_CH40_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0903_5G_WPA2_802.11ax_-_CH40_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0904_5G_WPA2_802.11ax_-_CH40_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0905_5G_WPA2_802.11ax_-_CH40_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0906_5G_WPA2_802.11ax_-_CH44_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0907_5G_WPA2_802.11ax_-_CH44_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0908_5G_WPA2_802.11ax_-_CH44_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0909_5G_WPA2_802.11ax_-_CH44_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0910_5G_WPA2_802.11ax_-_CH44_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0911_5G_WPA2_802.11ax_-_CH48_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0912_5G_WPA2_802.11ax_-_CH48_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0913_5G_WPA2_802.11ax_-_CH48_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0914_5G_WPA2_802.11ax_-_CH48_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0915_5G_WPA2_802.11ax_-_CH48_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0916_5G_WPA2_802.11ax_-_CH149_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0917_5G_WPA2_802.11ax_-_CH149_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0918_5G_WPA2_802.11ax_-_CH149_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0919_5G_WPA2_802.11ax_-_CH149_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0920_5G_WPA2_802.11ax_-_CH149_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0921_5G_WPA2_802.11ax_-_CH153_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0922_5G_WPA2_802.11ax_-_CH153_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0923_5G_WPA2_802.11ax_-_CH153_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0924_5G_WPA2_802.11ax_-_CH153_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0925_5G_WPA2_802.11ax_-_CH153_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0926_5G_WPA2_802.11ax_-_CH157_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0927_5G_WPA2_802.11ax_-_CH157_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0928_5G_WPA2_802.11ax_-_CH157_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0929_5G_WPA2_802.11ax_-_CH157_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0930_5G_WPA2_802.11ax_-_CH157_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0931_5G_WPA2_802.11ax_-_CH161_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0932_5G_WPA2_802.11ax_-_CH161_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0933_5G_WPA2_802.11ax_-_CH161_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0934_5G_WPA2_802.11ax_-_CH161_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0935_5G_WPA2_802.11ax_-_CH161_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0936_5G_WPA2_802.11ax_-_CH165_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH165, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["0937_5G_WPA2_802.11ax_-_CH165_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH165, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["0938_5G_WPA2_802.11ax_-_CH165_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH165, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["0939_5G_WPA2_802.11ax_-_CH165_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH165, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["0940_5G_WPA2_802.11ax_-_CH165_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA2, AP_5G80211ax, AP_5GCH165, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["0941_5G_WPA3_802.11n_-_Auto_TV Wifi_Off/On_", "5G_WPA3_5G-802.11n_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GAuto, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0942_5G_WPA3_802.11n_-_Auto_DC_Off/On_", "5G_WPA3_5G-802.11n_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GAuto, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0943_5G_WPA3_802.11n_-_Auto_AC_Off/On_", "5G_WPA3_5G-802.11n_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GAuto, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0944_5G_WPA3_802.11n_-_Auto_AP_Off/On_", "5G_WPA3_5G-802.11n_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GAuto, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0945_5G_WPA3_802.11n_-_Auto_IP_ConnectionTest_", "5G_WPA3_5G-802.11n_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GAuto, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0946_5G_WPA3_802.11n_-_CH36_TV Wifi_Off/On_", "5G_WPA3_5G-802.11n_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH36, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0947_5G_WPA3_802.11n_-_CH36_DC_Off/On_", "5G_WPA3_5G-802.11n_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH36, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0948_5G_WPA3_802.11n_-_CH36_AC_Off/On_", "5G_WPA3_5G-802.11n_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH36, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0949_5G_WPA3_802.11n_-_CH36_AP_Off/On_", "5G_WPA3_5G-802.11n_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH36, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0950_5G_WPA3_802.11n_-_CH36_IP_ConnectionTest_", "5G_WPA3_5G-802.11n_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH36, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0951_5G_WPA3_802.11n_-_CH40_TV Wifi_Off/On_", "5G_WPA3_5G-802.11n_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH40, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0952_5G_WPA3_802.11n_-_CH40_DC_Off/On_", "5G_WPA3_5G-802.11n_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH40, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0953_5G_WPA3_802.11n_-_CH40_AC_Off/On_", "5G_WPA3_5G-802.11n_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH40, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0954_5G_WPA3_802.11n_-_CH40_AP_Off/On_", "5G_WPA3_5G-802.11n_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH40, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0955_5G_WPA3_802.11n_-_CH40_IP_ConnectionTest_", "5G_WPA3_5G-802.11n_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH40, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0956_5G_WPA3_802.11n_-_CH44_TV Wifi_Off/On_", "5G_WPA3_5G-802.11n_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH44, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0957_5G_WPA3_802.11n_-_CH44_DC_Off/On_", "5G_WPA3_5G-802.11n_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH44, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0958_5G_WPA3_802.11n_-_CH44_AC_Off/On_", "5G_WPA3_5G-802.11n_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH44, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0959_5G_WPA3_802.11n_-_CH44_AP_Off/On_", "5G_WPA3_5G-802.11n_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH44, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0960_5G_WPA3_802.11n_-_CH44_IP_ConnectionTest_", "5G_WPA3_5G-802.11n_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH44, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0961_5G_WPA3_802.11n_-_CH48_TV Wifi_Off/On_", "5G_WPA3_5G-802.11n_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH48, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0962_5G_WPA3_802.11n_-_CH48_DC_Off/On_", "5G_WPA3_5G-802.11n_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH48, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0963_5G_WPA3_802.11n_-_CH48_AC_Off/On_", "5G_WPA3_5G-802.11n_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH48, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0964_5G_WPA3_802.11n_-_CH48_AP_Off/On_", "5G_WPA3_5G-802.11n_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH48, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0965_5G_WPA3_802.11n_-_CH48_IP_ConnectionTest_", "5G_WPA3_5G-802.11n_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH48, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0966_5G_WPA3_802.11n_-_CH149_TV Wifi_Off/On_", "5G_WPA3_5G-802.11n_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH149, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0967_5G_WPA3_802.11n_-_CH149_DC_Off/On_", "5G_WPA3_5G-802.11n_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH149, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0968_5G_WPA3_802.11n_-_CH149_AC_Off/On_", "5G_WPA3_5G-802.11n_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH149, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0969_5G_WPA3_802.11n_-_CH149_AP_Off/On_", "5G_WPA3_5G-802.11n_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH149, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0970_5G_WPA3_802.11n_-_CH149_IP_ConnectionTest_", "5G_WPA3_5G-802.11n_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH149, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0971_5G_WPA3_802.11n_-_CH153_TV Wifi_Off/On_", "5G_WPA3_5G-802.11n_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH153, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0972_5G_WPA3_802.11n_-_CH153_DC_Off/On_", "5G_WPA3_5G-802.11n_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH153, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0973_5G_WPA3_802.11n_-_CH153_AC_Off/On_", "5G_WPA3_5G-802.11n_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH153, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0974_5G_WPA3_802.11n_-_CH153_AP_Off/On_", "5G_WPA3_5G-802.11n_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH153, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0975_5G_WPA3_802.11n_-_CH153_IP_ConnectionTest_", "5G_WPA3_5G-802.11n_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH153, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0976_5G_WPA3_802.11n_-_CH157_TV Wifi_Off/On_", "5G_WPA3_5G-802.11n_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH157, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0977_5G_WPA3_802.11n_-_CH157_DC_Off/On_", "5G_WPA3_5G-802.11n_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH157, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0978_5G_WPA3_802.11n_-_CH157_AC_Off/On_", "5G_WPA3_5G-802.11n_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH157, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0979_5G_WPA3_802.11n_-_CH157_AP_Off/On_", "5G_WPA3_5G-802.11n_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH157, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0980_5G_WPA3_802.11n_-_CH157_IP_ConnectionTest_", "5G_WPA3_5G-802.11n_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH157, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0981_5G_WPA3_802.11n_-_CH161_TV Wifi_Off/On_", "5G_WPA3_5G-802.11n_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH161, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0982_5G_WPA3_802.11n_-_CH161_DC_Off/On_", "5G_WPA3_5G-802.11n_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH161, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0983_5G_WPA3_802.11n_-_CH161_AC_Off/On_", "5G_WPA3_5G-802.11n_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH161, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0984_5G_WPA3_802.11n_-_CH161_AP_Off/On_", "5G_WPA3_5G-802.11n_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH161, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0985_5G_WPA3_802.11n_-_CH161_IP_ConnectionTest_", "5G_WPA3_5G-802.11n_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH161, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0986_5G_WPA3_802.11n_-_CH165_TV Wifi_Off/On_", "5G_WPA3_5G-802.11n_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH165, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0987_5G_WPA3_802.11n_-_CH165_DC_Off/On_", "5G_WPA3_5G-802.11n_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH165, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0988_5G_WPA3_802.11n_-_CH165_AC_Off/On_", "5G_WPA3_5G-802.11n_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH165, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0989_5G_WPA3_802.11n_-_CH165_AP_Off/On_", "5G_WPA3_5G-802.11n_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH165, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0990_5G_WPA3_802.11n_-_CH165_IP_ConnectionTest_", "5G_WPA3_5G-802.11n_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211n, AP_5GCH165, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0991_5G_WPA3_802.11a_-_Auto_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GAuto, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0992_5G_WPA3_802.11a_-_Auto_DC_Off/On_", "5G_WPA3_5G-802.11a_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GAuto, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0993_5G_WPA3_802.11a_-_Auto_AC_Off/On_", "5G_WPA3_5G-802.11a_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GAuto, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0994_5G_WPA3_802.11a_-_Auto_AP_Off/On_", "5G_WPA3_5G-802.11a_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GAuto, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["0995_5G_WPA3_802.11a_-_Auto_IP_ConnectionTest_", "5G_WPA3_5G-802.11a_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GAuto, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["0996_5G_WPA3_802.11a_-_CH36_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH36, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["0997_5G_WPA3_802.11a_-_CH36_DC_Off/On_", "5G_WPA3_5G-802.11a_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH36, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["0998_5G_WPA3_802.11a_-_CH36_AC_Off/On_", "5G_WPA3_5G-802.11a_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH36, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["0999_5G_WPA3_802.11a_-_CH36_AP_Off/On_", "5G_WPA3_5G-802.11a_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH36, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1000_5G_WPA3_802.11a_-_CH36_IP_ConnectionTest_", "5G_WPA3_5G-802.11a_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH36, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1001_5G_WPA3_802.11a_-_CH40_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH40, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1002_5G_WPA3_802.11a_-_CH40_DC_Off/On_", "5G_WPA3_5G-802.11a_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH40, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1003_5G_WPA3_802.11a_-_CH40_AC_Off/On_", "5G_WPA3_5G-802.11a_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH40, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1004_5G_WPA3_802.11a_-_CH40_AP_Off/On_", "5G_WPA3_5G-802.11a_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH40, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1005_5G_WPA3_802.11a_-_CH40_IP_ConnectionTest_", "5G_WPA3_5G-802.11a_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH40, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1006_5G_WPA3_802.11a_-_CH44_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH44, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1007_5G_WPA3_802.11a_-_CH44_DC_Off/On_", "5G_WPA3_5G-802.11a_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH44, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1008_5G_WPA3_802.11a_-_CH44_AC_Off/On_", "5G_WPA3_5G-802.11a_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH44, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1009_5G_WPA3_802.11a_-_CH44_AP_Off/On_", "5G_WPA3_5G-802.11a_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH44, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1010_5G_WPA3_802.11a_-_CH44_IP_ConnectionTest_", "5G_WPA3_5G-802.11a_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH44, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1011_5G_WPA3_802.11a_-_CH48_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH48, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1012_5G_WPA3_802.11a_-_CH48_DC_Off/On_", "5G_WPA3_5G-802.11a_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH48, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1013_5G_WPA3_802.11a_-_CH48_AC_Off/On_", "5G_WPA3_5G-802.11a_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH48, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1014_5G_WPA3_802.11a_-_CH48_AP_Off/On_", "5G_WPA3_5G-802.11a_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH48, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1015_5G_WPA3_802.11a_-_CH48_IP_ConnectionTest_", "5G_WPA3_5G-802.11a_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH48, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1016_5G_WPA3_802.11a_-_CH149_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH149, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1017_5G_WPA3_802.11a_-_CH149_DC_Off/On_", "5G_WPA3_5G-802.11a_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH149, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1018_5G_WPA3_802.11a_-_CH149_AC_Off/On_", "5G_WPA3_5G-802.11a_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH149, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1019_5G_WPA3_802.11a_-_CH149_AP_Off/On_", "5G_WPA3_5G-802.11a_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH149, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1020_5G_WPA3_802.11a_-_CH149_IP_ConnectionTest_", "5G_WPA3_5G-802.11a_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH149, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1021_5G_WPA3_802.11a_-_CH153_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH153, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1022_5G_WPA3_802.11a_-_CH153_DC_Off/On_", "5G_WPA3_5G-802.11a_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH153, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1023_5G_WPA3_802.11a_-_CH153_AC_Off/On_", "5G_WPA3_5G-802.11a_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH153, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1024_5G_WPA3_802.11a_-_CH153_AP_Off/On_", "5G_WPA3_5G-802.11a_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH153, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1025_5G_WPA3_802.11a_-_CH153_IP_ConnectionTest_", "5G_WPA3_5G-802.11a_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH153, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1026_5G_WPA3_802.11a_-_CH157_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH157, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1027_5G_WPA3_802.11a_-_CH157_DC_Off/On_", "5G_WPA3_5G-802.11a_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH157, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1028_5G_WPA3_802.11a_-_CH157_AC_Off/On_", "5G_WPA3_5G-802.11a_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH157, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1029_5G_WPA3_802.11a_-_CH157_AP_Off/On_", "5G_WPA3_5G-802.11a_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH157, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1030_5G_WPA3_802.11a_-_CH157_IP_ConnectionTest_", "5G_WPA3_5G-802.11a_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH157, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1031_5G_WPA3_802.11a_-_CH161_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH161, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1032_5G_WPA3_802.11a_-_CH161_DC_Off/On_", "5G_WPA3_5G-802.11a_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH161, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1033_5G_WPA3_802.11a_-_CH161_AC_Off/On_", "5G_WPA3_5G-802.11a_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH161, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1034_5G_WPA3_802.11a_-_CH161_AP_Off/On_", "5G_WPA3_5G-802.11a_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH161, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1035_5G_WPA3_802.11a_-_CH161_IP_ConnectionTest_", "5G_WPA3_5G-802.11a_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH161, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1036_5G_WPA3_802.11a_-_CH165_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH165, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1037_5G_WPA3_802.11a_-_CH165_DC_Off/On_", "5G_WPA3_5G-802.11a_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH165, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1038_5G_WPA3_802.11a_-_CH165_AC_Off/On_", "5G_WPA3_5G-802.11a_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH165, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1039_5G_WPA3_802.11a_-_CH165_AP_Off/On_", "5G_WPA3_5G-802.11a_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH165, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1040_5G_WPA3_802.11a_-_CH165_IP_ConnectionTest_", "5G_WPA3_5G-802.11a_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211a, AP_5GCH165, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1041_5G_WPA3_802.11ac_-_Auto_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GAuto, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1042_5G_WPA3_802.11ac_-_Auto_DC_Off/On_", "5G_WPA3_5G-802.11ac_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GAuto, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1043_5G_WPA3_802.11ac_-_Auto_AC_Off/On_", "5G_WPA3_5G-802.11ac_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GAuto, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1044_5G_WPA3_802.11ac_-_Auto_AP_Off/On_", "5G_WPA3_5G-802.11ac_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GAuto, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1045_5G_WPA3_802.11ac_-_Auto_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GAuto, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1046_5G_WPA3_802.11ac_-_CH36_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH36, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1047_5G_WPA3_802.11ac_-_CH36_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH36, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1048_5G_WPA3_802.11ac_-_CH36_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH36, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1049_5G_WPA3_802.11ac_-_CH36_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH36, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1050_5G_WPA3_802.11ac_-_CH36_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH36, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1051_5G_WPA3_802.11ac_-_CH40_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH40, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1052_5G_WPA3_802.11ac_-_CH40_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH40, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1053_5G_WPA3_802.11ac_-_CH40_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH40, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1054_5G_WPA3_802.11ac_-_CH40_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH40, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1055_5G_WPA3_802.11ac_-_CH40_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH40, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1056_5G_WPA3_802.11ac_-_CH44_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH44, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1057_5G_WPA3_802.11ac_-_CH44_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH44, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1058_5G_WPA3_802.11ac_-_CH44_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH44, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1059_5G_WPA3_802.11ac_-_CH44_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH44, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1060_5G_WPA3_802.11ac_-_CH44_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH44, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1061_5G_WPA3_802.11ac_-_CH48_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH48, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1062_5G_WPA3_802.11ac_-_CH48_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH48, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1063_5G_WPA3_802.11ac_-_CH48_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH48, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1064_5G_WPA3_802.11ac_-_CH48_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH48, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1065_5G_WPA3_802.11ac_-_CH48_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH48, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1066_5G_WPA3_802.11ac_-_CH149_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH149, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1067_5G_WPA3_802.11ac_-_CH149_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH149, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1068_5G_WPA3_802.11ac_-_CH149_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH149, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1069_5G_WPA3_802.11ac_-_CH149_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH149, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1070_5G_WPA3_802.11ac_-_CH149_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH149, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1071_5G_WPA3_802.11ac_-_CH153_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH153, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1072_5G_WPA3_802.11ac_-_CH153_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH153, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1073_5G_WPA3_802.11ac_-_CH153_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH153, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1074_5G_WPA3_802.11ac_-_CH153_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH153, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1075_5G_WPA3_802.11ac_-_CH153_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH153, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1076_5G_WPA3_802.11ac_-_CH157_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH157, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1077_5G_WPA3_802.11ac_-_CH157_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH157, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1078_5G_WPA3_802.11ac_-_CH157_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH157, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1079_5G_WPA3_802.11ac_-_CH157_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH157, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1080_5G_WPA3_802.11ac_-_CH157_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH157, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1081_5G_WPA3_802.11ac_-_CH161_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH161, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1082_5G_WPA3_802.11ac_-_CH161_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH161, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1083_5G_WPA3_802.11ac_-_CH161_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH161, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1084_5G_WPA3_802.11ac_-_CH161_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH161, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1085_5G_WPA3_802.11ac_-_CH161_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH161, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1086_5G_WPA3_802.11ac_-_CH165_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH165, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1087_5G_WPA3_802.11ac_-_CH165_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH165, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1088_5G_WPA3_802.11ac_-_CH165_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH165, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1089_5G_WPA3_802.11ac_-_CH165_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH165, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1090_5G_WPA3_802.11ac_-_CH165_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ac, AP_5GCH165, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1091_5G_WPA3_802.11ax_-_Auto_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_Auto_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GAuto, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1092_5G_WPA3_802.11ax_-_Auto_DC_Off/On_", "5G_WPA3_5G-802.11ax_Auto_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GAuto, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1093_5G_WPA3_802.11ax_-_Auto_AC_Off/On_", "5G_WPA3_5G-802.11ax_Auto_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GAuto, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1094_5G_WPA3_802.11ax_-_Auto_AP_Off/On_", "5G_WPA3_5G-802.11ax_Auto_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GAuto, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1095_5G_WPA3_802.11ax_-_Auto_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_Auto_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GAuto, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1096_5G_WPA3_802.11ax_-_CH36_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH36_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH36, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1097_5G_WPA3_802.11ax_-_CH36_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH36_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH36, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1098_5G_WPA3_802.11ax_-_CH36_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH36_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH36, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1099_5G_WPA3_802.11ax_-_CH36_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH36_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH36, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1100_5G_WPA3_802.11ax_-_CH36_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH36_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH36, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1101_5G_WPA3_802.11ax_-_CH40_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH40_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH40, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1102_5G_WPA3_802.11ax_-_CH40_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH40_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH40, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1103_5G_WPA3_802.11ax_-_CH40_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH40_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH40, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1104_5G_WPA3_802.11ax_-_CH40_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH40_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH40, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1105_5G_WPA3_802.11ax_-_CH40_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH40_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH40, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1106_5G_WPA3_802.11ax_-_CH44_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH44_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH44, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1107_5G_WPA3_802.11ax_-_CH44_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH44_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH44, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1108_5G_WPA3_802.11ax_-_CH44_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH44_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH44, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1109_5G_WPA3_802.11ax_-_CH44_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH44_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH44, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1110_5G_WPA3_802.11ax_-_CH44_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH44_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH44, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1111_5G_WPA3_802.11ax_-_CH48_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH48_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH48, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1112_5G_WPA3_802.11ax_-_CH48_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH48_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH48, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1113_5G_WPA3_802.11ax_-_CH48_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH48_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH48, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1114_5G_WPA3_802.11ax_-_CH48_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH48_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH48, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1115_5G_WPA3_802.11ax_-_CH48_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH48_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH48, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1116_5G_WPA3_802.11ax_-_CH149_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH149_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH149, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1117_5G_WPA3_802.11ax_-_CH149_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH149_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH149, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1118_5G_WPA3_802.11ax_-_CH149_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH149_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH149, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1119_5G_WPA3_802.11ax_-_CH149_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH149_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH149, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1120_5G_WPA3_802.11ax_-_CH149_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH149_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH149, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1121_5G_WPA3_802.11ax_-_CH153_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH153_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH153, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1122_5G_WPA3_802.11ax_-_CH153_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH153_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH153, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1123_5G_WPA3_802.11ax_-_CH153_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH153_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH153, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1124_5G_WPA3_802.11ax_-_CH153_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH153_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH153, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1125_5G_WPA3_802.11ax_-_CH153_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH153_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH153, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1126_5G_WPA3_802.11ax_-_CH157_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH157_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH157, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1127_5G_WPA3_802.11ax_-_CH157_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH157_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH157, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1128_5G_WPA3_802.11ax_-_CH157_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH157_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH157, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1129_5G_WPA3_802.11ax_-_CH157_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH157_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH157, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1130_5G_WPA3_802.11ax_-_CH157_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH157_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH157, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1131_5G_WPA3_802.11ax_-_CH161_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH161_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH161, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1132_5G_WPA3_802.11ax_-_CH161_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH161_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH161, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1133_5G_WPA3_802.11ax_-_CH161_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH161_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH161, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1134_5G_WPA3_802.11ax_-_CH161_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH161_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH161, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1135_5G_WPA3_802.11ax_-_CH161_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH161_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH161, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["1136_5G_WPA3_802.11ax_-_CH165_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH165_WifiTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH165, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["1137_5G_WPA3_802.11ax_-_CH165_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH165_DCTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH165, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["1138_5G_WPA3_802.11ax_-_CH165_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH165_ACTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH165, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["1139_5G_WPA3_802.11ax_-_CH165_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH165_APTriggerOnOff",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH165, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["1140_5G_WPA3_802.11ax_-_CH165_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH165_ConnectionTest",
     AP_5GSettings, AP_5GWPA3, AP_5G80211ax, AP_5GCH165, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
]

def AP_WIFIAction(AP_Type):
    File_Info.filePath = 'Test Report_' + time.strftime("%Y%m%d-%H%M%S") + '.txt'
    with open(File_Info.filePath, 'w') as log:
        device = os.popen('adb shell getprop ro.product.brand').read()
        log.write("Device Brand: " + device + '\n')
        deviceName = os.popen('adb shell getprop ro.product.model').read()
        log.write("Device Name: " + deviceName + '\n')
        platformVersion = os.popen('adb shell getprop ro.build.version.release').read()
        log.write("Android Version: " + platformVersion + '\n')
        print(AP_Type)
        log.write("AP Type: " + AP_Type + '\n')
        Test_Times = TestLoopInfo.Tframe4.get()
        print('Test loop =', Test_Times)
        count = 0
        while count <= int(Test_Times):
            Test_Loops = count + 1
            print('Current test loop:', Test_Loops)
            log.write("Test loop: " + str(Test_Loops) + '\n')
            LogTextBoxUpdate("Current test loop: " + str(Test_Loops) + '\n')
            TestLoopBoxUpdate(str(Test_Loops) + '\n')
            keyevent = os.popen('adb shell input keyevent 3')
            IP_Address = EthernetInfo.IP_Address.get()
            CheckNumber = len(WifiEventList)
            for CheckIndex in range(0, CheckNumber, 1):
                run = (getRouterValue(AP_Type, WifiEventList[CheckIndex][1].split("_")[0], 1) +
                       getRouterValue(AP_Type, WifiEventList[CheckIndex][1].split("_")[1], 1) +
                       getRouterValue(AP_Type, WifiEventList[CheckIndex][1].split("_")[2], 1) +
                       getRouterValue(AP_Type, WifiEventList[CheckIndex][1].split("_")[3], 1) +
                       getRouterValue(AP_Type, WifiEventList[CheckIndex][1].split("_")[4], 1))
                if (run == 5):
                    for wifiEvent in range(2, 9):
                        if wifiEvent == 8:
                            WifiEventList[CheckIndex][wifiEvent]()
                            print(WifiEventList[CheckIndex][wifiEvent])
                            hostname = IP_Address
                            response = subprocess.call('ping -n 1 ' + hostname, shell=True)
                            if response == 0:
                                Result = ':Pass'
                                print(WifiEventList[CheckIndex][0], ": Pass")
                            else:
                                Result = ':Fail'
                                LogTextBoxUpdate("IP ping fail, Ping IP again..." + '\n')
                                sleep(10)
                                response = subprocess.call('ping -n 1 ' + hostname, shell=True)
                                if response == 0:
                                    Result = ':Pass'
                                    print(WifiEventList[CheckIndex][0], ": Pass")
                                else:
                                    Result = ':Fail'
                                    print(WifiEventList[CheckIndex][0], ": Fail")
                            Result0 = (WifiEventList[CheckIndex][0] + Result)
                            log.write(time.strftime("%Y/%m/%d %H:%M:%S ") + WifiEventList[CheckIndex][0] + Result + '\n')
                            LogTextBoxUpdate(Result0 + '\n')
                            sleep(5)

                        else:
                            WifiEventList[CheckIndex][wifiEvent]()
                            print(WifiEventList[CheckIndex][wifiEvent])

            count += 1
            if count == int(Test_Times):
                break
    LogTextBoxUpdate("All test finish..." + '\n')
    LogTextBoxUpdate("generate report..." + '\n')
    TXTFile_To_ExcelFile(File_Info.filePath)
    AP_Info.driver.close()
    return


def SeleniumFinish():
    AP_Info.driver.quit()
    return
