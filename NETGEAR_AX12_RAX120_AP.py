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
    sleep(1)


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

    LogTextBoxUpdate("You open browser is " + Browser_Type + '\n')
    # Input address
    print('Router ID: ' + ID, 'Router Password: ' + PW, sep='\n')
    AP_Info.driver.get(('http://{un}:{pw}@' + EthernetInfo.AP_Webaddress.get() + '/index.htm').format(un=ID, pw=PW))
    sleep(10)
    return


def AP_WiFiEnter():
    # WIFI setting
    AP_Info.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[3]/b/span").click()
    sleep(10)
    # Change frame
    xf = AP_Info.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/iframe')
    AP_Info.driver.switch_to.frame(xf)
    sleep(2)


def AP_24GWPA():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[2]/tbody/tr[2]/td/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[2]/tbody/tr[6]/td/label").click()
    sleep(3)


def AP_24GWPA2():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[2]/tbody/tr[2]/td/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[2]/tbody/tr[5]/td/label").click()
    sleep(3)


def AP_24GWPA3():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[2]/tbody/tr[2]/td/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[2]/tbody/tr[8]/td/label").click()
    sleep(3)


def AP_5GWPA2():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[8]/td[2]/select")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[2]/tbody/tr[5]/td/label").click()
    sleep(3)


def AP_5GWPA3():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[8]/td[2]/select")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[2]/tbody/tr[8]/td/label").click()
    sleep(3)


def AP_24G80211g():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[15]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[15]/td[2]/select/option[1]").click()
    sleep(5)


def AP_24G80211gn():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[15]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[15]/td[2]/select/option[3]").click()
    sleep(5)


def AP_24G80211ax():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[15]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[15]/td[2]/select/option[3]").click()
    sleep(5)


def AP_5G80211ac():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[5]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[8]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[4]/div[11]/table[1]/tbody/tr[8]/td[2]/select/option[4]").click()
    sleep(5)


def AP_5G80211ax():
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[5]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[8]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form/div[4]/div[11]/table[1]/tbody/tr[8]/td[2]/select/option[4]").click()
    sleep(5)

def AP_24GAuto():
    #2.4G_CH Auto
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[1]").click()
    sleep(5)

def AP_24GCH1():
    #2.4G_CH1
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[2]").click()
    sleep(5)

def AP_24GCH2():
    #2.4G_CH2
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[3]").click()
    sleep(5)

def AP_24GCH3():
    #2.4G_CH3
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[4]").click()
    sleep(5)

def AP_24GCH4():
    #2.4G_CH4
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[5]").click()
    sleep(5)

def AP_24GCH5():
    #2.4G_CH5
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[6]").click()
    sleep(5)

def AP_24GCH6():
    #2.4G_CH6
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[7]").click()
    sleep(5)

def AP_24GCH7():
    #2.4G_CH7
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[8]").click()
    sleep(5)

def AP_24GCH8():
    #2.4G_CH8
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[9]").click()
    sleep(5)

def AP_24GCH9():
    #2.4G_CH9
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[10]").click()
    sleep(5)

def AP_24GCH10():
    #2.4G_CH10
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[11]").click()
    sleep(5)

def AP_24GCH11():
    #2.4G_CH11
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[12]").click()
    sleep(5)

def AP_24GCH12():
    #2.4G_CH12
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[13]").click()
    sleep(5)


def AP_24GCH13():
    #2.4G_CH13
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[12]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[14]/td[2]/select/option[14]").click()
    sleep(5)

def AP_5GCH36():
    #5G_CH36
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[5]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[6]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[6]/td[2]/select/option[1]").click()
    sleep(5)

def AP_5GCH40():
    #5G_CH40
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[5]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[6]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[6]/td[2]/select/option[2]").click()
    sleep(5)

def AP_5GCH44():
    #5G_CH44
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[5]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[6]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[6]/td[2]/select/option[3]").click()
    sleep(5)

def AP_5GCH48():
    #5G_CH48
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[5]/td[2]/input")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[6]/td[2]/select").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[6]/td[2]/select/option[4]").click()
    sleep(5)


def AP_24GWPASSIDConnect():
    SSIDFrame24 = WifiInfo.SSIDFrame24.get()
    PWFrame24 = WifiInfo.PWFrame24.get()
    # Save
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/input[2]").click()
    sleep(40)
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
    SSIDFrame5 = WifiInfo.SSIDFrame5.get()
    PWFrame5 = WifiInfo.PWFrame5.get()
    # Save
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/input[2]").click()
    sleep(40)
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
    # Save
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/input[2]").click()
    sleep(40)


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
    sleep(3)
    LogTextBoxUpdate("AP WiFi Disable" + '\n')
    # SSID Disable
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[10]/td/label")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[10]/td/label").click()
    sleep(3)
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[3]/td/label")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[3]/td/label").click()
    sleep(3)
    # SAVE
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/input[2]").click()
    sleep(3)
    confirm = AP_Info.driver.switch_to.alert
    confirm.accept()
    sleep(40)
    # SSID Enable
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[10]/td/label")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/table[1]/tbody/tr[10]/td/label").click()
    sleep(3)
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[3]/td/label")
    AP_Info.driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[4]/div[11]/table[1]/tbody/tr[3]/td/label").click()
    sleep(3)
    # SAVE
    AP_Info.driver.find_element_by_xpath("/html/body/form/div[3]/table/tbody/tr/td/input[2]").click()
    sleep(40)

def ConnectionTest():
    sleep(15)

def Pingip():
    sleep(1)

WifiEventList = [
    ["001_2.4G_WPA_802.11g_-_Auto_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_2.4G-Auto_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["002_2.4G_WPA_802.11g_-_Auto_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_2.4G-Auto_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["003_2.4G_WPA_802.11g_-_Auto_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_2.4G-Auto_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["004_2.4G_WPA_802.11g_-_Auto_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_2.4G-Auto_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["005_2.4G_WPA_802.11g_-_Auto_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_2.4G-Auto_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["006_2.4G_WPA_802.11g_-_CH1_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH1_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["007_2.4G_WPA_802.11g_-_CH1_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH1_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["008_2.4G_WPA_802.11g_-_CH1_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH1_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["009_2.4G_WPA_802.11g_-_CH1_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH1_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["010_2.4G_WPA_802.11g_-_CH1_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH1_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["011_2.4G_WPA_802.11g_-_CH2_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH2_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["012_2.4G_WPA_802.11g_-_CH2_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH2_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["013_2.4G_WPA_802.11g_-_CH2_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH2_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["014_2.4G_WPA_802.11g_-_CH2_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH2_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["015_2.4G_WPA_802.11g_-_CH2_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH2_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["016_2.4G_WPA_802.11g_-_CH3_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH3_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["017_2.4G_WPA_802.11g_-_CH3_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH3_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["018_2.4G_WPA_802.11g_-_CH3_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH3_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["019_2.4G_WPA_802.11g_-_CH3_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH3_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["020_2.4G_WPA_802.11g_-_CH3_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH3_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["021_2.4G_WPA_802.11g_-_CH4_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH4_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["022_2.4G_WPA_802.11g_-_CH4_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH4_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["023_2.4G_WPA_802.11g_-_CH4_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH4_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["024_2.4G_WPA_802.11g_-_CH4_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH4_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["025_2.4G_WPA_802.11g_-_CH4_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH4_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["026_2.4G_WPA_802.11g_-_CH5_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH5_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["027_2.4G_WPA_802.11g_-_CH5_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH5_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["028_2.4G_WPA_802.11g_-_CH5_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH5_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["029_2.4G_WPA_802.11g_-_CH5_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH5_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["030_2.4G_WPA_802.11g_-_CH5_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH5_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["031_2.4G_WPA_802.11g_-_CH6_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH6_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["032_2.4G_WPA_802.11g_-_CH6_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH6_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["033_2.4G_WPA_802.11g_-_CH6_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH6_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["034_2.4G_WPA_802.11g_-_CH6_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH6_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["035_2.4G_WPA_802.11g_-_CH6_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH6_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["036_2.4G_WPA_802.11g_-_CH7_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH7_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["037_2.4G_WPA_802.11g_-_CH7_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH7_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["038_2.4G_WPA_802.11g_-_CH7_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH7_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["039_2.4G_WPA_802.11g_-_CH7_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH7_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["040_2.4G_WPA_802.11g_-_CH7_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH7_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["041_2.4G_WPA_802.11g_-_CH8_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH8_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["042_2.4G_WPA_802.11g_-_CH8_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH8_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["043_2.4G_WPA_802.11g_-_CH8_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH8_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["044_2.4G_WPA_802.11g_-_CH8_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH8_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["045_2.4G_WPA_802.11g_-_CH8_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH8_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["046_2.4G_WPA_802.11g_-_CH9_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH9_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["047_2.4G_WPA_802.11g_-_CH9_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH9_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["048_2.4G_WPA_802.11g_-_CH9_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH9_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["049_2.4G_WPA_802.11g_-_CH9_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH9_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["050_2.4G_WPA_802.11g_-_CH9_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH9_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["051_2.4G_WPA_802.11g_-_CH10_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH10_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["052_2.4G_WPA_802.11g_-_CH10_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH10_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["053_2.4G_WPA_802.11g_-_CH10_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH10_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["054_2.4G_WPA_802.11g_-_CH10_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH10_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["055_2.4G_WPA_802.11g_-_CH10_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH10_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["056_2.4G_WPA_802.11g_-_CH11_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH11_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["057_2.4G_WPA_802.11g_-_CH11_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH11_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["058_2.4G_WPA_802.11g_-_CH11_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH11_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["059_2.4G_WPA_802.11g_-_CH11_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH11_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["060_2.4G_WPA_802.11g_-_CH11_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH11_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["061_2.4G_WPA_802.11g_-_CH12_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH12_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH12, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["062_2.4G_WPA_802.11g_-_CH12_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH12_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH12, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["063_2.4G_WPA_802.11g_-_CH12_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH12_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH12, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["064_2.4G_WPA_802.11g_-_CH12_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH12_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH12, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["065_2.4G_WPA_802.11g_-_CH12_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH12_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH12, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["066_2.4G_WPA_802.11g_-_CH13_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_CH13_WifiTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH13, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["067_2.4G_WPA_802.11g_-_CH13_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH13_DCTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH13, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["068_2.4G_WPA_802.11g_-_CH13_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_CH13_ACTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH13, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["069_2.4G_WPA_802.11g_-_CH13_AP_Off/On_", "2.4G_WPA_2.4G-802.11g_CH13_APTriggerOnOff", 
     AP_24GWPA, AP_24G80211g, AP_24GCH13, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["070_2.4G_WPA_802.11g_-_CH13_IP_ConnectionTest_", "2.4G_WPA_2.4G-802.11g_CH13_ConnectionTest", 
     AP_24GWPA, AP_24G80211g, AP_24GCH13, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["071_2.4G_WPA2_802.11g_-_Auto_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_2.4G-Auto_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["072_2.4G_WPA2_802.11g_-_Auto_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_2.4G-Auto_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["073_2.4G_WPA2_802.11g_-_Auto_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_2.4G-Auto_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["074_2.4G_WPA2_802.11g_-_Auto_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_2.4G-Auto_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["075_2.4G_WPA2_802.11g_-_Auto_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_2.4G-Auto_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["076_2.4G_WPA2_802.11g_-_CH1_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH1_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["077_2.4G_WPA2_802.11g_-_CH1_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH1_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["078_2.4G_WPA2_802.11g_-_CH1_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH1_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["079_2.4G_WPA2_802.11g_-_CH1_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH1_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["080_2.4G_WPA2_802.11g_-_CH1_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH1_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["081_2.4G_WPA2_802.11g_-_CH2_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH2_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["082_2.4G_WPA2_802.11g_-_CH2_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH2_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["083_2.4G_WPA2_802.11g_-_CH2_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH2_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["084_2.4G_WPA2_802.11g_-_CH2_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH2_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["085_2.4G_WPA2_802.11g_-_CH2_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH2_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["086_2.4G_WPA2_802.11g_-_CH3_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH3_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["087_2.4G_WPA2_802.11g_-_CH3_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH3_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["088_2.4G_WPA2_802.11g_-_CH3_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH3_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["089_2.4G_WPA2_802.11g_-_CH3_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH3_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["090_2.4G_WPA2_802.11g_-_CH3_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH3_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["091_2.4G_WPA2_802.11g_-_CH4_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH4_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["092_2.4G_WPA2_802.11g_-_CH4_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH4_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["093_2.4G_WPA2_802.11g_-_CH4_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH4_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["094_2.4G_WPA2_802.11g_-_CH4_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH4_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["095_2.4G_WPA2_802.11g_-_CH4_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH4_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["096_2.4G_WPA2_802.11g_-_CH5_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH5_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["097_2.4G_WPA2_802.11g_-_CH5_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH5_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["098_2.4G_WPA2_802.11g_-_CH5_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH5_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["099_2.4G_WPA2_802.11g_-_CH5_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH5_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["100_2.4G_WPA2_802.11g_-_CH5_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH5_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["101_2.4G_WPA2_802.11g_-_CH6_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH6_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["102_2.4G_WPA2_802.11g_-_CH6_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH6_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["103_2.4G_WPA2_802.11g_-_CH6_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH6_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["104_2.4G_WPA2_802.11g_-_CH6_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH6_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["105_2.4G_WPA2_802.11g_-_CH6_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH6_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["106_2.4G_WPA2_802.11g_-_CH7_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH7_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["107_2.4G_WPA2_802.11g_-_CH7_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH7_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["108_2.4G_WPA2_802.11g_-_CH7_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH7_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["109_2.4G_WPA2_802.11g_-_CH7_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH7_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["110_2.4G_WPA2_802.11g_-_CH7_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH7_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["111_2.4G_WPA2_802.11g_-_CH8_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH8_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["112_2.4G_WPA2_802.11g_-_CH8_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH8_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["113_2.4G_WPA2_802.11g_-_CH8_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH8_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["114_2.4G_WPA2_802.11g_-_CH8_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH8_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["115_2.4G_WPA2_802.11g_-_CH8_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH8_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["116_2.4G_WPA2_802.11g_-_CH9_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH9_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["117_2.4G_WPA2_802.11g_-_CH9_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH9_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["118_2.4G_WPA2_802.11g_-_CH9_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH9_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["119_2.4G_WPA2_802.11g_-_CH9_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH9_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["120_2.4G_WPA2_802.11g_-_CH9_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH9_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["121_2.4G_WPA2_802.11g_-_CH10_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH10_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["122_2.4G_WPA2_802.11g_-_CH10_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH10_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["123_2.4G_WPA2_802.11g_-_CH10_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH10_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["124_2.4G_WPA2_802.11g_-_CH10_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH10_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["125_2.4G_WPA2_802.11g_-_CH10_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH10_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["126_2.4G_WPA2_802.11g_-_CH11_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH11_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["127_2.4G_WPA2_802.11g_-_CH11_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH11_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["128_2.4G_WPA2_802.11g_-_CH11_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH11_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["129_2.4G_WPA2_802.11g_-_CH11_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH11_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["130_2.4G_WPA2_802.11g_-_CH11_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH11_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["131_2.4G_WPA2_802.11g_-_CH12_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH12_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH12, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["132_2.4G_WPA2_802.11g_-_CH12_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH12_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH12, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["133_2.4G_WPA2_802.11g_-_CH12_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH12_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH12, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["134_2.4G_WPA2_802.11g_-_CH12_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH12_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH12, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["135_2.4G_WPA2_802.11g_-_CH12_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH12_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH12, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["136_2.4G_WPA2_802.11g_-_CH13_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH13_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH13, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["137_2.4G_WPA2_802.11g_-_CH13_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH13_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH13, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["138_2.4G_WPA2_802.11g_-_CH13_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH13_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH13, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["139_2.4G_WPA2_802.11g_-_CH13_AP_Off/On_", "2.4G_WPA2_2.4G-802.11g_CH13_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH13, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["140_2.4G_WPA2_802.11g_-_CH13_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11g_CH13_ConnectionTest", 
     AP_24GWPA2, AP_24G80211g, AP_24GCH13, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["141_2.4G_WPA2_802.11gn_-_Auto_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_2.4G-Auto_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["142_2.4G_WPA2_802.11gn_-_Auto_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_2.4G-Auto_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["143_2.4G_WPA2_802.11gn_-_Auto_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_2.4G-Auto_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["144_2.4G_WPA2_802.11gn_-_Auto_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_2.4G-Auto_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["145_2.4G_WPA2_802.11gn_-_Auto_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_2.4G-Auto_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["146_2.4G_WPA2_802.11gn_-_CH1_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH1_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["147_2.4G_WPA2_802.11gn_-_CH1_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH1_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["148_2.4G_WPA2_802.11gn_-_CH1_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH1_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["149_2.4G_WPA2_802.11gn_-_CH1_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH1_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["150_2.4G_WPA2_802.11gn_-_CH1_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH1_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["151_2.4G_WPA2_802.11gn_-_CH2_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH2_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["152_2.4G_WPA2_802.11gn_-_CH2_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH2_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["153_2.4G_WPA2_802.11gn_-_CH2_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH2_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["154_2.4G_WPA2_802.11gn_-_CH2_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH2_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["155_2.4G_WPA2_802.11gn_-_CH2_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH2_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["156_2.4G_WPA2_802.11gn_-_CH3_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH3_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["157_2.4G_WPA2_802.11gn_-_CH3_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH3_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["158_2.4G_WPA2_802.11gn_-_CH3_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH3_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["159_2.4G_WPA2_802.11gn_-_CH3_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH3_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["160_2.4G_WPA2_802.11gn_-_CH3_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH3_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["161_2.4G_WPA2_802.11gn_-_CH4_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH4_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["162_2.4G_WPA2_802.11gn_-_CH4_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH4_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["163_2.4G_WPA2_802.11gn_-_CH4_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH4_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["164_2.4G_WPA2_802.11gn_-_CH4_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH4_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["165_2.4G_WPA2_802.11gn_-_CH4_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH4_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["166_2.4G_WPA2_802.11gn_-_CH5_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH5_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["167_2.4G_WPA2_802.11gn_-_CH5_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH5_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["168_2.4G_WPA2_802.11gn_-_CH5_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH5_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["169_2.4G_WPA2_802.11gn_-_CH5_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH5_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["170_2.4G_WPA2_802.11gn_-_CH5_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH5_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["171_2.4G_WPA2_802.11gn_-_CH6_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH6_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["172_2.4G_WPA2_802.11gn_-_CH6_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH6_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["173_2.4G_WPA2_802.11gn_-_CH6_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH6_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["174_2.4G_WPA2_802.11gn_-_CH6_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH6_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["175_2.4G_WPA2_802.11gn_-_CH6_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH6_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["176_2.4G_WPA2_802.11gn_-_CH7_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH7_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["177_2.4G_WPA2_802.11gn_-_CH7_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH7_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["178_2.4G_WPA2_802.11gn_-_CH7_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH7_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["179_2.4G_WPA2_802.11gn_-_CH7_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH7_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["180_2.4G_WPA2_802.11gn_-_CH7_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH7_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["181_2.4G_WPA2_802.11gn_-_CH8_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH8_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["182_2.4G_WPA2_802.11gn_-_CH8_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH8_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["183_2.4G_WPA2_802.11gn_-_CH8_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH8_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["184_2.4G_WPA2_802.11gn_-_CH8_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH8_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["185_2.4G_WPA2_802.11gn_-_CH8_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH8_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["186_2.4G_WPA2_802.11gn_-_CH9_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH9_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["187_2.4G_WPA2_802.11gn_-_CH9_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH9_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["188_2.4G_WPA2_802.11gn_-_CH9_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH9_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["189_2.4G_WPA2_802.11gn_-_CH9_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH9_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["190_2.4G_WPA2_802.11gn_-_CH9_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH9_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["191_2.4G_WPA2_802.11gn_-_CH10_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH10_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["192_2.4G_WPA2_802.11gn_-_CH10_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH10_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["193_2.4G_WPA2_802.11gn_-_CH10_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH10_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["194_2.4G_WPA2_802.11gn_-_CH10_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH10_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["195_2.4G_WPA2_802.11gn_-_CH10_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH10_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["196_2.4G_WPA2_802.11gn_-_CH11_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH11_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["197_2.4G_WPA2_802.11gn_-_CH11_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH11_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["198_2.4G_WPA2_802.11gn_-_CH11_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH11_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["199_2.4G_WPA2_802.11gn_-_CH11_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH11_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["200_2.4G_WPA2_802.11gn_-_CH11_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH11_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["201_2.4G_WPA2_802.11gn_-_CH12_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH12_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH12, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["202_2.4G_WPA2_802.11gn_-_CH12_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH12_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH12, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["203_2.4G_WPA2_802.11gn_-_CH12_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH12_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH12, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["204_2.4G_WPA2_802.11gn_-_CH12_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH12_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH12, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["205_2.4G_WPA2_802.11gn_-_CH12_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH12_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH12, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["206_2.4G_WPA2_802.11gn_-_CH13_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH13_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH13, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["207_2.4G_WPA2_802.11gn_-_CH13_DC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH13_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH13, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["208_2.4G_WPA2_802.11gn_-_CH13_AC_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH13_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH13, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["209_2.4G_WPA2_802.11gn_-_CH13_AP_Off/On_", "2.4G_WPA2_2.4G-802.11gn_CH13_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH13, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["210_2.4G_WPA2_802.11gn_-_CH13_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11gn_CH13_ConnectionTest", 
     AP_24GWPA2, AP_24G80211gn, AP_24GCH13, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["211_2.4G_WPA3_802.11g_-_Auto_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_2.4G-Auto_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GAuto, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["212_2.4G_WPA3_802.11g_-_Auto_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_2.4G-Auto_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GAuto, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["213_2.4G_WPA3_802.11g_-_Auto_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_2.4G-Auto_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GAuto, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["214_2.4G_WPA3_802.11g_-_Auto_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_2.4G-Auto_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GAuto, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["215_2.4G_WPA3_802.11g_-_Auto_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_2.4G-Auto_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GAuto, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["216_2.4G_WPA3_802.11g_-_CH1_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH1_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH1, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["217_2.4G_WPA3_802.11g_-_CH1_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH1_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH1, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["218_2.4G_WPA3_802.11g_-_CH1_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH1_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH1, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["219_2.4G_WPA3_802.11g_-_CH1_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH1_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH1, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["220_2.4G_WPA3_802.11g_-_CH1_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH1_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH1, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["221_2.4G_WPA3_802.11g_-_CH2_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH2_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH2, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["222_2.4G_WPA3_802.11g_-_CH2_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH2_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH2, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["223_2.4G_WPA3_802.11g_-_CH2_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH2_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH2, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["224_2.4G_WPA3_802.11g_-_CH2_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH2_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH2, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["225_2.4G_WPA3_802.11g_-_CH2_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH2_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH2, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["226_2.4G_WPA3_802.11g_-_CH3_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH3_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH3, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["227_2.4G_WPA3_802.11g_-_CH3_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH3_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH3, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["228_2.4G_WPA3_802.11g_-_CH3_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH3_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH3, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["229_2.4G_WPA3_802.11g_-_CH3_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH3_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH3, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["230_2.4G_WPA3_802.11g_-_CH3_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH3_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH3, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["231_2.4G_WPA3_802.11g_-_CH4_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH4_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH4, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["232_2.4G_WPA3_802.11g_-_CH4_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH4_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH4, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["233_2.4G_WPA3_802.11g_-_CH4_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH4_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH4, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["234_2.4G_WPA3_802.11g_-_CH4_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH4_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH4, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["235_2.4G_WPA3_802.11g_-_CH4_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH4_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH4, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["236_2.4G_WPA3_802.11g_-_CH5_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH5_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH5, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["237_2.4G_WPA3_802.11g_-_CH5_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH5_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH5, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["238_2.4G_WPA3_802.11g_-_CH5_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH5_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH5, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["239_2.4G_WPA3_802.11g_-_CH5_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH5_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH5, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["240_2.4G_WPA3_802.11g_-_CH5_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH5_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH5, AP_WPA3SSIDConnect, ConnectionTest, Pingip],    
    ["241_2.4G_WPA3_802.11g_-_CH6_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH6_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH6, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["242_2.4G_WPA3_802.11g_-_CH6_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH6_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH6, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["243_2.4G_WPA3_802.11g_-_CH6_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH6_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH6, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["244_2.4G_WPA3_802.11g_-_CH6_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH6_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH6, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["245_2.4G_WPA3_802.11g_-_CH6_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH6_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH6, AP_WPA3SSIDConnect, ConnectionTest, Pingip],  
    ["246_2.4G_WPA3_802.11g_-_CH7_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH7_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH7, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["247_2.4G_WPA3_802.11g_-_CH7_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH7_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH7, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["248_2.4G_WPA3_802.11g_-_CH7_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH7_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH7, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["249_2.4G_WPA3_802.11g_-_CH7_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH7_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH7, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["250_2.4G_WPA3_802.11g_-_CH7_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH7_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH7, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["251_2.4G_WPA3_802.11g_-_CH8_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH8_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH8, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["252_2.4G_WPA3_802.11g_-_CH8_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH8_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH8, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["253_2.4G_WPA3_802.11g_-_CH8_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH8_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH8, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["254_2.4G_WPA3_802.11g_-_CH8_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH8_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH8, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["255_2.4G_WPA3_802.11g_-_CH8_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH8_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH8, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["256_2.4G_WPA3_802.11g_-_CH9_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH9_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH9, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["257_2.4G_WPA3_802.11g_-_CH9_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH9_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH9, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["258_2.4G_WPA3_802.11g_-_CH9_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH9_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH9, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["259_2.4G_WPA3_802.11g_-_CH9_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH9_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH9, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["260_2.4G_WPA3_802.11g_-_CH9_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH9_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH9, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["261_2.4G_WPA3_802.11g_-_CH10_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH10_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH10, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["262_2.4G_WPA3_802.11g_-_CH10_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH10_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH10, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["263_2.4G_WPA3_802.11g_-_CH10_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH10_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH10, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["264_2.4G_WPA3_802.11g_-_CH10_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH10_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH10, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["265_2.4G_WPA3_802.11g_-_CH10_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH10_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH10, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["266_2.4G_WPA3_802.11g_-_CH11_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH11_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH11, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["267_2.4G_WPA3_802.11g_-_CH11_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH11_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH11, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["268_2.4G_WPA3_802.11g_-_CH11_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH11_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH11, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["269_2.4G_WPA3_802.11g_-_CH11_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH11_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH11, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["270_2.4G_WPA3_802.11g_-_CH11_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH11_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH11, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["271_2.4G_WPA3_802.11g_-_CH12_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH12_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH12, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["272_2.4G_WPA3_802.11g_-_CH12_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH12_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH12, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["273_2.4G_WPA3_802.11g_-_CH12_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH12_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH12, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["274_2.4G_WPA3_802.11g_-_CH12_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH12_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH12, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["275_2.4G_WPA3_802.11g_-_CH12_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH12_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH12, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["276_2.4G_WPA3_802.11g_-_CH13_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH13_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH13, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["277_2.4G_WPA3_802.11g_-_CH13_DC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH13_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH13, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["278_2.4G_WPA3_802.11g_-_CH13_AC_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH13_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH13, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["279_2.4G_WPA3_802.11g_-_CH13_AP_Off/On_", "2.4G_WPA3_2.4G-802.11g_CH13_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH13, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["280_2.4G_WPA3_802.11g_-_CH13_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11g_CH13_ConnectionTest", 
     AP_24GWPA3, AP_24G80211g, AP_24GCH13, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["281_2.4G_WPA3_802.11gn_-_Auto_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_2.4G-Auto_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GAuto, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["282_2.4G_WPA3_802.11gn_-_Auto_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_2.4G-Auto_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GAuto, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["283_2.4G_WPA3_802.11gn_-_Auto_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_2.4G-Auto_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GAuto, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["284_2.4G_WPA3_802.11gn_-_Auto_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_2.4G-Auto_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GAuto, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["285_2.4G_WPA3_802.11gn_-_Auto_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_2.4G-Auto_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GAuto, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["286_2.4G_WPA3_802.11gn_-_CH1_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH1_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH1, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["287_2.4G_WPA3_802.11gn_-_CH1_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH1_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH1, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["288_2.4G_WPA3_802.11gn_-_CH1_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH1_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH1, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["289_2.4G_WPA3_802.11gn_-_CH1_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH1_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH1, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["290_2.4G_WPA3_802.11gn_-_CH1_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH1_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH1, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["291_2.4G_WPA3_802.11gn_-_CH2_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH2_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH2, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["292_2.4G_WPA3_802.11gn_-_CH2_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH2_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH2, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["293_2.4G_WPA3_802.11gn_-_CH2_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH2_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH2, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["294_2.4G_WPA3_802.11gn_-_CH2_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH2_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH2, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["295_2.4G_WPA3_802.11gn_-_CH2_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH2_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH2, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["296_2.4G_WPA3_802.11gn_-_CH3_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH3_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH3, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["297_2.4G_WPA3_802.11gn_-_CH3_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH3_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH3, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["298_2.4G_WPA3_802.11gn_-_CH3_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH3_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH3, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["299_2.4G_WPA3_802.11gn_-_CH3_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH3_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH3, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["300_2.4G_WPA3_802.11gn_-_CH3_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH3_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH3, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["301_2.4G_WPA3_802.11gn_-_CH4_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH4_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH4, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["302_2.4G_WPA3_802.11gn_-_CH4_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH4_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH4, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["303_2.4G_WPA3_802.11gn_-_CH4_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH4_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH4, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["304_2.4G_WPA3_802.11gn_-_CH4_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH4_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH4, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["305_2.4G_WPA3_802.11gn_-_CH4_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH4_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH4, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["306_2.4G_WPA3_802.11gn_-_CH5_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH5_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH5, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["307_2.4G_WPA3_802.11gn_-_CH5_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH5_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH5, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["308_2.4G_WPA3_802.11gn_-_CH5_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH5_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH5, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["309_2.4G_WPA3_802.11gn_-_CH5_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH5_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH5, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["310_2.4G_WPA3_802.11gn_-_CH5_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH5_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH5, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["311_2.4G_WPA3_802.11gn_-_CH6_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH6_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH6, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["312_2.4G_WPA3_802.11gn_-_CH6_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH6_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH6, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["313_2.4G_WPA3_802.11gn_-_CH6_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH6_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH6, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["314_2.4G_WPA3_802.11gn_-_CH6_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH6_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH6, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["315_2.4G_WPA3_802.11gn_-_CH6_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH6_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH6, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["316_2.4G_WPA3_802.11gn_-_CH7_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH7_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH7, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["317_2.4G_WPA3_802.11gn_-_CH7_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH7_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH7, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["318_2.4G_WPA3_802.11gn_-_CH7_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH7_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH7, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["319_2.4G_WPA3_802.11gn_-_CH7_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH7_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH7, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["320_2.4G_WPA3_802.11gn_-_CH7_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH7_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH7, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["321_2.4G_WPA3_802.11gn_-_CH8_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH8_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH8, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["322_2.4G_WPA3_802.11gn_-_CH8_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH8_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH8, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["323_2.4G_WPA3_802.11gn_-_CH8_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH8_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH8, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["324_2.4G_WPA3_802.11gn_-_CH8_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH8_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH8, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["325_2.4G_WPA3_802.11gn_-_CH8_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH8_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH8, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["326_2.4G_WPA3_802.11gn_-_CH9_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH9_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH9, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["327_2.4G_WPA3_802.11gn_-_CH9_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH9_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH9, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["328_2.4G_WPA3_802.11gn_-_CH9_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH9_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH9, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["329_2.4G_WPA3_802.11gn_-_CH9_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH9_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH9, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["330_2.4G_WPA3_802.11gn_-_CH9_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH9_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH9, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["331_2.4G_WPA3_802.11gn_-_CH10_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH10_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH10, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["332_2.4G_WPA3_802.11gn_-_CH10_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH10_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH10, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["333_2.4G_WPA3_802.11gn_-_CH10_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH10_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH10, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["334_2.4G_WPA3_802.11gn_-_CH10_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH10_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH10, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["335_2.4G_WPA3_802.11gn_-_CH10_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH10_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH10, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["336_2.4G_WPA3_802.11gn_-_CH11_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH11_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH11, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["337_2.4G_WPA3_802.11gn_-_CH11_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH11_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH11, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["338_2.4G_WPA3_802.11gn_-_CH11_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH11_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH11, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["339_2.4G_WPA3_802.11gn_-_CH11_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH11_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH11, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["340_2.4G_WPA3_802.11gn_-_CH11_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH11_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH11, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["341_2.4G_WPA3_802.11gn_-_CH12_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH12_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH12, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["342_2.4G_WPA3_802.11gn_-_CH12_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH12_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH12, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["343_2.4G_WPA3_802.11gn_-_CH12_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH12_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH12, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["344_2.4G_WPA3_802.11gn_-_CH12_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH12_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH12, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["345_2.4G_WPA3_802.11gn_-_CH12_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH12_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH12, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["346_2.4G_WPA3_802.11gn_-_CH13_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH13_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH13, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["347_2.4G_WPA3_802.11gn_-_CH13_DC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH13_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH13, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["348_2.4G_WPA3_802.11gn_-_CH13_AC_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH13_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH13, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["349_2.4G_WPA3_802.11gn_-_CH13_AP_Off/On_", "2.4G_WPA3_2.4G-802.11gn_CH13_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH13, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["350_2.4G_WPA3_802.11gn_-_CH13_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11gn_CH13_ConnectionTest", 
     AP_24GWPA3, AP_24G80211gn, AP_24GCH13, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["351_2.4G_WPA2_802.11ax_-_Auto_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_2.4G-Auto_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["352_2.4G_WPA2_802.11ax_-_Auto_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_2.4G-Auto_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["353_2.4G_WPA2_802.11ax_-_Auto_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_2.4G-Auto_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["354_2.4G_WPA2_802.11ax_-_Auto_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_2.4G-Auto_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["355_2.4G_WPA2_802.11ax_-_Auto_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_2.4G-Auto_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["356_2.4G_WPA2_802.11ax_-_CH1_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH1_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["357_2.4G_WPA2_802.11ax_-_CH1_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH1_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["358_2.4G_WPA2_802.11ax_-_CH1_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH1_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["359_2.4G_WPA2_802.11ax_-_CH1_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH1_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["360_2.4G_WPA2_802.11ax_-_CH1_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH1_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["361_2.4G_WPA2_802.11ax_-_CH2_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH2_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["362_2.4G_WPA2_802.11ax_-_CH2_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH2_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["363_2.4G_WPA2_802.11ax_-_CH2_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH2_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["364_2.4G_WPA2_802.11ax_-_CH2_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH2_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["365_2.4G_WPA2_802.11ax_-_CH2_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH2_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["366_2.4G_WPA2_802.11ax_-_CH3_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH3_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["367_2.4G_WPA2_802.11ax_-_CH3_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH3_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["368_2.4G_WPA2_802.11ax_-_CH3_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH3_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["369_2.4G_WPA2_802.11ax_-_CH3_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH3_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["370_2.4G_WPA2_802.11ax_-_CH3_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH3_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["371_2.4G_WPA2_802.11ax_-_CH4_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH4_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["372_2.4G_WPA2_802.11ax_-_CH4_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH4_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["373_2.4G_WPA2_802.11ax_-_CH4_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH4_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["374_2.4G_WPA2_802.11ax_-_CH4_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH4_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["375_2.4G_WPA2_802.11ax_-_CH4_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH4_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["376_2.4G_WPA2_802.11ax_-_CH5_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH5_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["377_2.4G_WPA2_802.11ax_-_CH5_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH5_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["378_2.4G_WPA2_802.11ax_-_CH5_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH5_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["379_2.4G_WPA2_802.11ax_-_CH5_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH5_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["380_2.4G_WPA2_802.11ax_-_CH5_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH5_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["381_2.4G_WPA2_802.11ax_-_CH6_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH6_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["382_2.4G_WPA2_802.11ax_-_CH6_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH6_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["383_2.4G_WPA2_802.11ax_-_CH6_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH6_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["384_2.4G_WPA2_802.11ax_-_CH6_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH6_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["385_2.4G_WPA2_802.11ax_-_CH6_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH6_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["386_2.4G_WPA2_802.11ax_-_CH7_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH7_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["387_2.4G_WPA2_802.11ax_-_CH7_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH7_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["388_2.4G_WPA2_802.11ax_-_CH7_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH7_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["389_2.4G_WPA2_802.11ax_-_CH7_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH7_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["390_2.4G_WPA2_802.11ax_-_CH7_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH7_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["391_2.4G_WPA2_802.11ax_-_CH8_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH8_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["392_2.4G_WPA2_802.11ax_-_CH8_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH8_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["393_2.4G_WPA2_802.11ax_-_CH8_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH8_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["394_2.4G_WPA2_802.11ax_-_CH8_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH8_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["395_2.4G_WPA2_802.11ax_-_CH8_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH8_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["396_2.4G_WPA2_802.11ax_-_CH9_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH9_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["397_2.4G_WPA2_802.11ax_-_CH9_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH9_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["398_2.4G_WPA2_802.11ax_-_CH9_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH9_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["399_2.4G_WPA2_802.11ax_-_CH9_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH9_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["400_2.4G_WPA2_802.11ax_-_CH9_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH9_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["401_2.4G_WPA2_802.11ax_-_CH10_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH10_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["402_2.4G_WPA2_802.11ax_-_CH10_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH10_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["403_2.4G_WPA2_802.11ax_-_CH10_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH10_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["404_2.4G_WPA2_802.11ax_-_CH10_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH10_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["405_2.4G_WPA2_802.11ax_-_CH10_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH10_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["406_2.4G_WPA2_802.11ax_-_CH11_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH11_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["407_2.4G_WPA2_802.11ax_-_CH11_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH11_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["408_2.4G_WPA2_802.11ax_-_CH11_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH11_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["409_2.4G_WPA2_802.11ax_-_CH11_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH11_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["410_2.4G_WPA2_802.11ax_-_CH11_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH11_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["411_2.4G_WPA2_802.11ax_-_CH12_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH12_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH12, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["412_2.4G_WPA2_802.11ax_-_CH12_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH12_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH12, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["413_2.4G_WPA2_802.11ax_-_CH12_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH12_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH12, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["414_2.4G_WPA2_802.11ax_-_CH12_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH12_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH12, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["415_2.4G_WPA2_802.11ax_-_CH12_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH12_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH12, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["416_2.4G_WPA2_802.11ax_-_CH13_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH13_WifiTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH13, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["417_2.4G_WPA2_802.11ax_-_CH13_DC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH13_DCTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH13, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["418_2.4G_WPA2_802.11ax_-_CH13_AC_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH13_ACTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH13, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["419_2.4G_WPA2_802.11ax_-_CH13_AP_Off/On_", "2.4G_WPA2_2.4G-802.11ax_CH13_APTriggerOnOff", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH13, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["420_2.4G_WPA2_802.11ax_-_CH13_IP_ConnectionTest_", "2.4G_WPA2_2.4G-802.11ax_CH13_ConnectionTest", 
     AP_24GWPA2, AP_24G80211ax, AP_24GCH13, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["421_2.4G_WPA3_802.11ax_-_Auto_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_2.4G-Auto_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GAuto, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["422_2.4G_WPA3_802.11ax_-_Auto_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_2.4G-Auto_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GAuto, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["423_2.4G_WPA3_802.11ax_-_Auto_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_2.4G-Auto_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GAuto, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["424_2.4G_WPA3_802.11ax_-_Auto_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_2.4G-Auto_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GAuto, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["425_2.4G_WPA3_802.11ax_-_Auto_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_2.4G-Auto_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GAuto, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["426_2.4G_WPA3_802.11ax_-_CH1_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH1_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH1, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["427_2.4G_WPA3_802.11ax_-_CH1_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH1_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH1, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["428_2.4G_WPA3_802.11ax_-_CH1_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH1_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH1, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["429_2.4G_WPA3_802.11ax_-_CH1_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH1_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH1, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["430_2.4G_WPA3_802.11ax_-_CH1_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH1_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH1, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["431_2.4G_WPA3_802.11ax_-_CH2_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH2_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH2, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["432_2.4G_WPA3_802.11ax_-_CH2_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH2_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH2, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["433_2.4G_WPA3_802.11ax_-_CH2_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH2_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH2, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["434_2.4G_WPA3_802.11ax_-_CH2_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH2_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH2, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["435_2.4G_WPA3_802.11ax_-_CH2_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH2_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH2, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["436_2.4G_WPA3_802.11ax_-_CH3_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH3_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH3, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["437_2.4G_WPA3_802.11ax_-_CH3_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH3_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH3, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["438_2.4G_WPA3_802.11ax_-_CH3_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH3_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH3, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["439_2.4G_WPA3_802.11ax_-_CH3_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH3_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH3, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["440_2.4G_WPA3_802.11ax_-_CH3_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH3_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH3, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["441_2.4G_WPA3_802.11ax_-_CH4_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH4_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH4, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["442_2.4G_WPA3_802.11ax_-_CH4_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH4_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH4, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["443_2.4G_WPA3_802.11ax_-_CH4_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH4_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH4, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["444_2.4G_WPA3_802.11ax_-_CH4_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH4_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH4, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["445_2.4G_WPA3_802.11ax_-_CH4_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH4_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH4, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["446_2.4G_WPA3_802.11ax_-_CH5_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH5_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH5, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["447_2.4G_WPA3_802.11ax_-_CH5_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH5_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH5, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["448_2.4G_WPA3_802.11ax_-_CH5_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH5_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH5, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["449_2.4G_WPA3_802.11ax_-_CH5_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH5_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH5, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["450_2.4G_WPA3_802.11ax_-_CH5_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH5_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH5, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["451_2.4G_WPA3_802.11ax_-_CH6_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH6_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH6, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["452_2.4G_WPA3_802.11ax_-_CH6_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH6_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH6, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["453_2.4G_WPA3_802.11ax_-_CH6_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH6_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH6, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["454_2.4G_WPA3_802.11ax_-_CH6_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH6_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH6, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["455_2.4G_WPA3_802.11ax_-_CH6_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH6_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH6, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["456_2.4G_WPA3_802.11ax_-_CH7_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH7_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH7, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["457_2.4G_WPA3_802.11ax_-_CH7_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH7_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH7, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["458_2.4G_WPA3_802.11ax_-_CH7_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH7_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH7, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["459_2.4G_WPA3_802.11ax_-_CH7_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH7_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH7, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["460_2.4G_WPA3_802.11ax_-_CH7_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH7_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH7, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["461_2.4G_WPA3_802.11ax_-_CH8_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH8_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH8, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["462_2.4G_WPA3_802.11ax_-_CH8_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH8_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH8, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["463_2.4G_WPA3_802.11ax_-_CH8_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH8_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH8, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["464_2.4G_WPA3_802.11ax_-_CH8_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH8_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH8, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["465_2.4G_WPA3_802.11ax_-_CH8_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH8_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH8, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["466_2.4G_WPA3_802.11ax_-_CH9_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH9_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH9, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["467_2.4G_WPA3_802.11ax_-_CH9_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH9_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH9, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["468_2.4G_WPA3_802.11ax_-_CH9_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH9_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH9, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["469_2.4G_WPA3_802.11ax_-_CH9_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH9_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH9, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["470_2.4G_WPA3_802.11ax_-_CH9_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH9_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH9, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["471_2.4G_WPA3_802.11ax_-_CH10_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH10_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH10, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["472_2.4G_WPA3_802.11ax_-_CH10_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH10_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH10, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["473_2.4G_WPA3_802.11ax_-_CH10_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH10_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH10, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["474_2.4G_WPA3_802.11ax_-_CH10_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH10_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH10, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["475_2.4G_WPA3_802.11ax_-_CH10_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH10_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH10, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["476_2.4G_WPA3_802.11ax_-_CH11_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH11_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH11, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["477_2.4G_WPA3_802.11ax_-_CH11_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH11_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH11, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["478_2.4G_WPA3_802.11ax_-_CH11_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH11_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH11, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["479_2.4G_WPA3_802.11ax_-_CH11_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH11_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH11, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["480_2.4G_WPA3_802.11ax_-_CH11_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH11_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH11, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["481_2.4G_WPA3_802.11ax_-_CH12_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH12_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH12, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["482_2.4G_WPA3_802.11ax_-_CH12_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH12_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH12, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["483_2.4G_WPA3_802.11ax_-_CH12_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH12_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH12, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["484_2.4G_WPA3_802.11ax_-_CH12_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH12_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH12, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["485_2.4G_WPA3_802.11ax_-_CH12_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH12_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH12, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["486_2.4G_WPA3_802.11ax_-_CH13_TV Wifi_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH13_WifiTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH13, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["487_2.4G_WPA3_802.11ax_-_CH13_DC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH13_DCTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH13, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["488_2.4G_WPA3_802.11ax_-_CH13_AC_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH13_ACTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH13, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["489_2.4G_WPA3_802.11ax_-_CH13_AP_Off/On_", "2.4G_WPA3_2.4G-802.11ax_CH13_APTriggerOnOff", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH13, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["490_2.4G_WPA3_802.11ax_-_CH13_IP_ConnectionTest_", "2.4G_WPA3_2.4G-802.11ax_CH13_ConnectionTest", 
     AP_24GWPA3, AP_24G80211ax, AP_24GCH13, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["491_5G_WPA2_802.11ac_-_CH36_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH36_WifiTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["492_5G_WPA2_802.11ac_-_CH36_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH36_DCTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["493_5G_WPA2_802.11ac_-_CH36_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH36_ACTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["494_5G_WPA2_802.11ac_-_CH36_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH36_APTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["495_5G_WPA2_802.11ac_-_CH36_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH36_ConnectionTest", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["496_5G_WPA2_802.11ac_-_CH40_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH40_WifiTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["497_5G_WPA2_802.11ac_-_CH40_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH40_DCTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["498_5G_WPA2_802.11ac_-_CH40_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH40_ACTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["499_5G_WPA2_802.11ac_-_CH40_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH40_APTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["500_5G_WPA2_802.11ac_-_CH40_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH40_ConnectionTest", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["501_5G_WPA2_802.11ac_-_CH44_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH44_WifiTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["502_5G_WPA2_802.11ac_-_CH44_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH44_DCTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["503_5G_WPA2_802.11ac_-_CH44_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH44_ACTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["504_5G_WPA2_802.11ac_-_CH44_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH44_APTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["505_5G_WPA2_802.11ac_-_CH44_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH44_ConnectionTest", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["506_5G_WPA2_802.11ac_-_CH48_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_CH48_WifiTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["507_5G_WPA2_802.11ac_-_CH48_DC_Off/On_", "5G_WPA2_5G-802.11ac_CH48_DCTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["508_5G_WPA2_802.11ac_-_CH48_AC_Off/On_", "5G_WPA2_5G-802.11ac_CH48_ACTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["509_5G_WPA2_802.11ac_-_CH48_AP_Off/On_", "5G_WPA2_5G-802.11ac_CH48_APTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["510_5G_WPA2_802.11ac_-_CH48_IP_ConnectionTest_", "5G_WPA2_5G-802.11ac_CH48_ConnectionTest", 
     AP_5GWPA2, AP_5G80211ac, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["511_5G_WPA3_802.11ac_-_CH36_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH36_WifiTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH36, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["512_5G_WPA3_802.11ac_-_CH36_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH36_DCTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH36, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["513_5G_WPA3_802.11ac_-_CH36_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH36_ACTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH36, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["514_5G_WPA3_802.11ac_-_CH36_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH36_APTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH36, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["515_5G_WPA3_802.11ac_-_CH36_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH36_ConnectionTest", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH36, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["516_5G_WPA3_802.11ac_-_CH40_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH40_WifiTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH40, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["517_5G_WPA3_802.11ac_-_CH40_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH40_DCTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH40, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["518_5G_WPA3_802.11ac_-_CH40_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH40_ACTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH40, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["519_5G_WPA3_802.11ac_-_CH40_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH40_APTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH40, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["520_5G_WPA3_802.11ac_-_CH40_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH40_ConnectionTest", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH40, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["521_5G_WPA3_802.11ac_-_CH44_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH44_WifiTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH44, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["522_5G_WPA3_802.11ac_-_CH44_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH44_DCTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH44, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["523_5G_WPA3_802.11ac_-_CH44_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH44_ACTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH44, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["524_5G_WPA3_802.11ac_-_CH44_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH44_APTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH44, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["525_5G_WPA3_802.11ac_-_CH44_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH44_ConnectionTest", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH44, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["526_5G_WPA3_802.11ac_-_CH48_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ac_CH48_WifiTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH48, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["527_5G_WPA3_802.11ac_-_CH48_DC_Off/On_", "5G_WPA3_5G-802.11ac_CH48_DCTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH48, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["528_5G_WPA3_802.11ac_-_CH48_AC_Off/On_", "5G_WPA3_5G-802.11ac_CH48_ACTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH48, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["529_5G_WPA3_802.11ac_-_CH48_AP_Off/On_", "5G_WPA3_5G-802.11ac_CH48_APTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH48, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["530_5G_WPA3_802.11ac_-_CH48_IP_ConnectionTest_", "5G_WPA3_5G-802.11ac_CH48_ConnectionTest", 
     AP_5GWPA3, AP_5G80211ac, AP_5GCH48, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["531_5G_WPA2_802.11ax_-_CH36_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH36_WifiTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["532_5G_WPA2_802.11ax_-_CH36_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH36_DCTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["533_5G_WPA2_802.11ax_-_CH36_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH36_ACTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["534_5G_WPA2_802.11ax_-_CH36_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH36_APTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["535_5G_WPA2_802.11ax_-_CH36_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH36_ConnectionTest", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["536_5G_WPA2_802.11ax_-_CH40_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH40_WifiTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["537_5G_WPA2_802.11ax_-_CH40_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH40_DCTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["538_5G_WPA2_802.11ax_-_CH40_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH40_ACTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["539_5G_WPA2_802.11ax_-_CH40_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH40_APTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["540_5G_WPA2_802.11ax_-_CH40_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH40_ConnectionTest", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["541_5G_WPA2_802.11ax_-_CH44_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH44_WifiTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["542_5G_WPA2_802.11ax_-_CH44_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH44_DCTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["543_5G_WPA2_802.11ax_-_CH44_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH44_ACTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["544_5G_WPA2_802.11ax_-_CH44_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH44_APTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["545_5G_WPA2_802.11ax_-_CH44_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH44_ConnectionTest", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["546_5G_WPA2_802.11ax_-_CH48_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ax_CH48_WifiTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["547_5G_WPA2_802.11ax_-_CH48_DC_Off/On_", "5G_WPA2_5G-802.11ax_CH48_DCTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["548_5G_WPA2_802.11ax_-_CH48_AC_Off/On_", "5G_WPA2_5G-802.11ax_CH48_ACTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["549_5G_WPA2_802.11ax_-_CH48_AP_Off/On_", "5G_WPA2_5G-802.11ax_CH48_APTriggerOnOff", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["550_5G_WPA2_802.11ax_-_CH48_IP_ConnectionTest_", "5G_WPA2_5G-802.11ax_CH48_ConnectionTest", 
     AP_5GWPA2, AP_5G80211ax, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["551_5G_WPA3_802.11ax_-_CH36_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH36_WifiTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH36, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["552_5G_WPA3_802.11ax_-_CH36_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH36_DCTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH36, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["553_5G_WPA3_802.11ax_-_CH36_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH36_ACTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH36, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["554_5G_WPA3_802.11ax_-_CH36_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH36_APTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH36, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["555_5G_WPA3_802.11ax_-_CH36_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH36_ConnectionTest", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH36, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["556_5G_WPA3_802.11ax_-_CH40_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH40_WifiTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH40, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["557_5G_WPA3_802.11ax_-_CH40_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH40_DCTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH40, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["558_5G_WPA3_802.11ax_-_CH40_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH40_ACTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH40, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["559_5G_WPA3_802.11ax_-_CH40_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH40_APTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH40, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["560_5G_WPA3_802.11ax_-_CH40_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH40_ConnectionTest", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH40, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["561_5G_WPA3_802.11ax_-_CH44_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH44_WifiTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH44, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["562_5G_WPA3_802.11ax_-_CH44_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH44_DCTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH44, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["563_5G_WPA3_802.11ax_-_CH44_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH44_ACTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH44, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["564_5G_WPA3_802.11ax_-_CH44_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH44_APTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH44, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["565_5G_WPA3_802.11ax_-_CH44_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH44_ConnectionTest", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH44, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
    ["566_5G_WPA3_802.11ax_-_CH48_TV Wifi_Off/On_", "5G_WPA3_5G-802.11ax_CH48_WifiTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH48, AP_WPA3SSIDConnect, WifiTriggerOnOff, Pingip],
    ["567_5G_WPA3_802.11ax_-_CH48_DC_Off/On_", "5G_WPA3_5G-802.11ax_CH48_DCTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH48, AP_WPA3SSIDConnect, DCTriggerOnOff, Pingip],
    ["568_5G_WPA3_802.11ax_-_CH48_AC_Off/On_", "5G_WPA3_5G-802.11ax_CH48_ACTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH48, AP_WPA3SSIDConnect, ACTriggerOnOff, Pingip],
    ["569_5G_WPA3_802.11ax_-_CH48_AP_Off/On_", "5G_WPA3_5G-802.11ax_CH48_APTriggerOnOff", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH48, AP_WPA3SSIDConnect, APTriggerOnOff, Pingip],
    ["570_5G_WPA3_802.11ax_-_CH48_IP_ConnectionTest_", "5G_WPA3_5G-802.11ax_CH48_ConnectionTest", 
     AP_5GWPA3, AP_5G80211ax, AP_5GCH48, AP_WPA3SSIDConnect, ConnectionTest, Pingip],
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
                if run == 5:
                    for wifiEvent in range(2, 8):
                        if wifiEvent == 7:
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
