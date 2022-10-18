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
    TestLoopBoxUpdate('0' + '\n')
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
    print('You open browser is', Browser_Type)
    LogTextBoxUpdate("You open browser is " + Browser_Type + '\n')
    # Input address
    print('Router ID: ' + ID, 'Router Password: ' + PW, sep='\n')
    AP_Webaddress = EthernetInfo.AP_Webaddress.get()
    AP_Info.driver.get(AP_Webaddress)
    sleep(10)
    # Enter password
    context = AP_Info.driver.find_element_by_xpath("//input[@type='password']")
    context.send_keys(PW)
    sleep(2)
    # Login
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/a").click()
    sleep(15)
    return


def AP_WiFiEnter():
    # Enter Wi-Fi Setting page
    AP_Info.driver.find_element_by_xpath("//div[@id='main-menu']/div/div/ul/li[4]/a/span").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("//div[@id='navigator']/div/div/ul/li[4]/a/span[2]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("//div[@id='navigator']/div/div/ul/li[4]/ul/li/a/span[2]").click()
    sleep(5)
    element0 = AP_Info.driver.find_elements_by_name("tj_login")
    sleep(15)


def AP_24G_WPA2():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[3]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/ul/li[2]/label/span[2]").click()
    sleep(5)


def AP_24G_WPA3():
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[1]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[3]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/ul/li[3]/label/span[2]").click()
    sleep(5)


def AP_5G_WPA2():
    target = AP_Info.driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/span[2]/input')
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[3]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/ul/li[2]/label/span[2]").click()
    sleep(5)


def AP_5G_WPA3():
    target = AP_Info.driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/span[2]/input')
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[3]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/ul/li[3]/label/span[2]").click()
    sleep(5)


def AP_24G80211ax():
    target = AP_Info.driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[1]')
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[9]/div[3]/div[2]/div[1]/span[2]/input").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/ul/li[1]/label/span[2]").click()
    sleep(5)


def AP_24G80211bgn():
    target = AP_Info.driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[1]')
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[9]/div[3]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/ul/li[2]/label/span[2]").click()
    sleep(5)


def AP_24G80211bgnax():
    target = AP_Info.driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[1]')
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[9]/div[3]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/ul/li[3]/label/span[2]").click()
    sleep(5)


def AP_5G80211ax():
    target = AP_Info.driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/span[2]/input')
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[9]/div[3]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/ul/li[1]/label").click()
    sleep(5)


def AP_5G80211ac():
    target = AP_Info.driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/span[2]/input')
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[9]/div[3]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/ul/li[2]/label").click()
    sleep(5)


def AP_5G80211a():
    target = AP_Info.driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[3]/div[2]/div[1]/span[2]/input')
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div[2]/div[6]/div[2]/div[1]/div/div/div[2]/div[3]/div[2]/div[9]/div[3]").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/ul/li[3]/label").click()
    sleep(5)


def AP_24GWPASSIDConnect():
    SSIDFrame24 = WifiInfo.SSIDFrame24.get()
    PWFrame24 = WifiInfo.PWFrame24.get()
    sleep(5)
    # save
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[1]/a").click()
    sleep(8)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[5]/div[11]/div[4]/div/div/div[2]/div/div/div/div[2]/div[1]/a/span[2]").click()
    sleep(10)
    # SSID connect
    SSIDclear = os.popen('adb shell pm clear com.steinwurf.adbjoinwifi')
    sleep(5)
    SSIDconnect = os.popen(
        'adb shell am start -n com.steinwurf.adbjoinwifi/com.steinwurf.adbjoinwifi.MainActivity -e ssid ' + SSIDFrame24 + ' -e password_type WPA -e password ' + PWFrame24)
    sleep(10)
    # Home key
    keyevent = os.popen('adb shell input keyevent 3')
    sleep(10)


def AP_5GWPASSIDConnect():
    SSIDFrame5 = WifiInfo.SSIDFrame5.get()
    PWFrame5 = WifiInfo.PWFrame5.get()
    sleep(5)
    # save
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[1]/a/span[2]").click()
    sleep(5)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[5]/div[11]/div[4]/div/div/div[2]/div/div/div/div[2]/div[1]/a").click()
    sleep(10)
    # SSID connect
    SSIDclear = os.popen('adb shell pm clear com.steinwurf.adbjoinwifi')
    sleep(5)
    SSIDconnect = os.popen(
        'adb shell am start -n com.steinwurf.adbjoinwifi/com.steinwurf.adbjoinwifi.MainActivity -e ssid ' + SSIDFrame5 + ' -e password_type WPA -e password ' + PWFrame5)
    sleep(10)
    # Home key
    keyevent = os.popen('adb shell input keyevent 3')
    sleep(10)


def AP_WPA3SSIDConnect():
    # save
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[1]/a/span[2]").click()
    sleep(5)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[5]/div[11]/div[4]/div/div/div[2]/div/div/div/div[2]/div[1]/a").click()
    sleep(35)


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
    sleep(100)
    keyevent = os.popen('adb shell input keyevent 3')
    sleep(10)


def APTriggerOnOff():
    LogTextBoxUpdate("AP Wifi Trigger Off/On Test" + '\n')
    keyevent = os.popen('adb shell input keyevent 3')
    target = AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div["
        "2]/div[1]/div[2]/div[1]/ul/li/div/label/span[2]")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div["
        "2]/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[1]/ul/li/div/label/span[2]").click()
    sleep(2)
    # 5g diable
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div["
        "2]/div[6]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/ul/li/div/label/span[2]").click()
    sleep(2)
    # Save
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[1]/a/span[2]").click()
    sleep(5)
    # Double confirm_OK
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[5]/div[9]/div[4]/div/div/div[2]/div/div/div/div[2]/div[1]/a/span[2]").click()
    sleep(10)

    # 2.4g enable
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div["
        "2]/div[5]/div/div[2]/div[2]/div[1]/div[2]/div[1]/ul/li/div/label/span[2]").click()
    sleep(2)
    target = AP_Info.driver.find_element_by_xpath(
        '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div['
        '2]/div[5]/div/div[2]/div[2]/div[3]/div[2]/div[9]/div[3]')
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    # 5g enable
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div[2]/div["
        "2]/div[6]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div[1]/ul/li/div/label/span[2]").click()
    sleep(2)
    # Save
    AP_Info.driver.find_element_by_xpath(
        "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div[1]/a/span[2]").click()
    sleep(5)
    AP_Info.driver.find_element_by_xpath("/html/body/div[5]/div[11]/div[4]/div/div/div[2]/div/div/div").click()
    sleep(30)


def Pingip():
    sleep(1)

WifiEventList = [
    ["001_2.4G_WPA2_802.11ax_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_WifiTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211ax, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["002_2.4G_WPA2_802.11ax_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_DCTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211ax, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["003_2.4G_WPA2_802.11ax_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_ACTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211ax, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["004_2.4G_WPA2_802.11ax_AP_Power_Off/On_", "2.4G_WPA2_2.4G-802.11ax_APTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211ax, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],                  
    ["005_2.4G_WPA2_802.11bgn_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_WifiTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211bgn, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["006_2.4G_WPA2_802.11bgn_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_DCTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211bgn, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["007_2.4G_WPA2_802.11bgn_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_ACTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211bgn, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["008_2.4G_WPA2_802.11bgn_AP_Power_Off/On_", "2.4G_WPA2_2.4G-802.11bgn_APTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211bgn, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],       
    ["009_2.4G_WPA2_802.11bgnax_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11bgnax_WifiTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211bgnax, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["010_2.4G_WPA2_802.11bgnax_DC_Off/On_", "2.4G_WPA2_2.4G-802.11bgnax_DCTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211bgnax, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["011_2.4G_WPA2_802.11bgnax_AC_Off/On_", "2.4G_WPA2_2.4G-802.11bgnax_ACTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211bgnax, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["012_2.4G_WPA2_802.11bgnax_AP_Power_Off/On_", "2.4G_WPA2_2.4G-802.11bgnax_APTriggerOnOff", AP_24G_WPA2, 
     AP_24G80211bgnax, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["013_2.4G_WPA3_802.11ax_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_WifiTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211ax, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["014_2.4G_WPA3_802.11ax_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_DCTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211ax, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["015_2.4G_WPA3_802.11ax_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_ACTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211ax, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["016_2.4G_WPA3_802.11ax_AP_Power_Off/On_", "2.4G_WPA3_2.4G-802.11ax_APTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211ax, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip], 
    ["017_2.4G_WPA3_802.11bgn_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_WifiTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211bgn, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["018_2.4G_WPA3_802.11bgn_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_DCTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211bgn, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["019_2.4G_WPA3_802.11bgn_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_ACTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211bgn, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["020_2.4G_WPA3_802.11bgn_AP_Power_Off/On_", "2.4G_WPA3_2.4G-802.11bgn_APTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211bgn, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip], 
    ["021_2.4G_WPA3_802.11bgnax_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11bgnax_WifiTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211bgnax, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["022_2.4G_WPA3_802.11bgnax_DC_Off/On_", "2.4G_WPA3_2.4G-802.11bgnax_DCTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211bgnax, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["023_2.4G_WPA3_802.11bgnax_AC_Off/On_", "2.4G_WPA3_2.4G-802.11bgnax_ACTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211bgnax, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["024_2.4G_WPA3_802.11bgnax_AP_Power_Off/On_", "2.4G_WPA3_2.4G-802.11bgnax_APTriggerOnOff", AP_24G_WPA3, 
     AP_24G80211bgnax, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip], 
    ["025_5G_WPA2_802.11ax_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_WifiTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211ax, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["026_5G_WPA2_802.11ax_DC_Off/On_", "5G_WPA2_5G-802.11ax_DCTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211ax, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["027_5G_WPA2_802.11ax_AC_Off/On_", "5G_WPA2_5G-802.11ax_ACTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211ax, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["028_5G_WPA2_802.11ax_AP_Power_Off/On_", "5G_WPA2_5G-802.11ax_APTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211ax, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["029_5G_WPA2_802.11ac_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_WifiTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211ac, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["030_5G_WPA2_802.11ac_DC_Off/On_", "5G_WPA2_5G-802.11ac_DCTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211ac, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["031_5G_WPA2_802.11ac_AC_Off/On_", "5G_WPA2_5G-802.11ac_ACTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211ac, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["032_5G_WPA2_802.11ac_AP_Power_Off/On_", "5G_WPA2_5G-802.11ac_APTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211ac, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["033_5G_WPA2_802.11a_TV Wifi_Off/On_", "5G_WPA2_5G-802.11a_WifiTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211a, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["034_5G_WPA2_802.11a_DC_Off/On_", "5G_WPA2_5G-802.11a_DCTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211a, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["035_5G_WPA2_802.11a_AC_Off/On_", "5G_WPA2_5G-802.11a_ACTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211a, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["036_5G_WPA2_802.11a_AP_Power_Off/On_", "5G_WPA2_5G-802.11a_APTriggerOnOff", AP_5G_WPA2, 
     AP_5G80211a, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["037_5G_WPA3_802.11ax_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_WifiTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211ax, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["038_5G_WPA3_802.11ax_DC_Off/On_", "5G_WPA3_5G-802.11ax_DCTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211ax, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["039_5G_WPA3_802.11ax_AC_Off/On_", "5G_WPA3_5G-802.11ax_ACTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211ax, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["040_5G_WPA3_802.11ax_AP_Power_Off/On_", "5G_WPA3_5G-802.11ax_APTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211ax, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["041_5G_WPA3_802.11ac_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_WifiTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211ac, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["042_5G_WPA3_802.11ac_DC_Off/On_", "5G_WPA3_5G-802.11ac_DCTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211ac, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["043_5G_WPA3_802.11ac_AC_Off/On_", "5G_WPA3_5G-802.11ac_ACTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211ac, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["044_5G_WPA3_802.11ac_AP_Power_Off/On_", "5G_WPA3_5G-802.11ac_APTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211ac, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["045_5G_WPA3_802.11a_TV Wifi_Off/On_", "5G_WPA3_5G-802.11a_WifiTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211a, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["046_5G_WPA3_802.11a_DC_Off/On_", "5G_WPA3_5G-802.11a_DCTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211a, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["047_5G_WPA3_802.11a_AC_Off/On_", "5G_WPA3_5G-802.11a_ACTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211a, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["048_5G_WPA3_802.11a_AP_Power_Off/On_", "5G_WPA3_5G-802.11a_APTriggerOnOff", AP_5G_WPA3, 
     AP_5G80211a, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
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
                       getRouterValue(AP_Type, WifiEventList[CheckIndex][1].split("_")[3], 1))
                if (run == 4):
                    for wifiEvent in range(2, 7):
                        if wifiEvent == 6:
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
                                response = subprocess.call('ping -n 1 '+hostname, shell=True)
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
    log.close()
    AP_Info.driver.close()
    return


def SeleniumFinish():
    AP_Info.driver.quit()
    return
