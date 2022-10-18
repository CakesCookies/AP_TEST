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
    print('You open browser is', Browser_Type)
    LogTextBoxUpdate("You open browser is " + Browser_Type + '\n')
    # Input address
    print('Router ID: ' + ID, 'Router Password: ' + PW, sep='\n')
    AP_Webaddress = EthernetInfo.AP_Webaddress.get()
    AP_Info.driver.get(AP_Webaddress)
    sleep(15)
    #Enter ID
    context = AP_Info.driver.find_element_by_css_selector('#login_username')
    context.send_keys(ID)
    sleep(5)
    # Enter password    
    context = AP_Info.driver.find_element_by_css_selector("#login_filed > div.password_gap > input")
    context.send_keys(PW)
    sleep(1)
    # Login
    commit = AP_Info.driver.find_element_by_css_selector('#login_filed > input')
    commit.click()
    sleep(5)
    return


def AP_WiFiEnter():
    # Enter Wi-Fi Setting page
    AP_Info.driver.find_element_by_id("Advanced_Wireless_Content_menu").click()
    sleep(5)


def AP_24G():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/select/option[1]").click()
    sleep(2)


def AP_5G():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td/select/option[2]").click()
    sleep(2)


def AP_24G_11gWPA():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select/option[3]").click()
    sleep(2)


def AP_24G_11gWPA2():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select/option[4]").click()
    sleep(2)


def AP_24G_11nWPA():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select/option[3]").click()
    sleep(2)


def AP_24G_11nWPA2():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select/option[2]").click()
    sleep(2)

def AP_5G_WPA():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select/option[3]").click()
    sleep(2)


def AP_5G_WPA2():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/select/option[2]").click()
    sleep(2)


def AP_24G80211g():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td/select/option[3]").click()
    sleep(2)


def AP_24G80211n():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td/select/option[2]").click()
    sleep(2)


def AP_5G80211n():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td/select/option[2]").click()
    sleep(2)


def AP_5G80211ac():
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td/select").click()
    sleep(1)
    AP_Info.driver.find_element_by_xpath(
        "/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[6]/td/select/option[1]").click()
    sleep(2)


def AP_24GWPASSIDConnect():
    SSIDFrame24 = WifiInfo.SSIDFrame24.get()
    PWFrame24 = WifiInfo.PWFrame24.get()
    # save
    AP_Info.driver.find_element_by_id("applyButton").click()
    sleep(20)
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
    # save
    AP_Info.driver.find_element_by_id("applyButton").click()
    sleep(20)
    # SSID connect
    SSIDclear = os.popen('adb shell pm clear com.steinwurf.adbjoinwifi')
    sleep(5)
    SSIDconnect = os.popen(
        'adb shell am start -n com.steinwurf.adbjoinwifi/com.steinwurf.adbjoinwifi.MainActivity -e ssid ' + SSIDFrame5 + ' -e password_type WPA -e password ' + PWFrame5)
    sleep(5)
    # Home key
    keyevent = os.popen('adb shell input keyevent 3')
    sleep(10)


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
    print("Device reboot.... wait for device turn on")
    LogTextBoxUpdate("Device reboot.... wait for device turn on" + '\n')
    sleep(120)
    keyevent = os.popen('adb shell input keyevent 3')
    sleep(10)


def Pingip():
    sleep(1)

WifiEventList = [
    ["001_2.4G_WPA_802.11g_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11g_WifiTriggerOnOff", AP_24G, 
     AP_24G80211g, AP_24G_11gWPA, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["002_2.4G_WPA_802.11g_DC_Off/On_", "2.4G_WPA_2.4G-802.11g_DCTriggerOnOff", AP_24G, 
     AP_24G80211g, AP_24G_11gWPA, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["003_2.4G_WPA_802.11g_AC_Off/On_", "2.4G_WPA_2.4G-802.11g_ACTriggerOnOff", AP_24G, 
     AP_24G80211g, AP_24G_11gWPA, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["004_2.4G_WPA2_802.11g_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11g_WifiTriggerOnOff", AP_24G, 
     AP_24G80211g, AP_24G_11gWPA2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["005_2.4G_WPA2_802.11g_DC_Off/On_", "2.4G_WPA2_2.4G-802.11g_DCTriggerOnOff", AP_24G, 
     AP_24G80211g, AP_24G_11gWPA2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["006_2.4G_WPA2_802.11g_AC_Off/On_", "2.4G_WPA2_2.4G-802.11g_ACTriggerOnOff", AP_24G, 
     AP_24G80211g, AP_24G_11gWPA2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["007_2.4G_WPA_802.11n_TV Wifi_Off/On_", "2.4G_WPA_2.4G-802.11n_WifiTriggerOnOff", AP_24G, 
     AP_24G80211n, AP_24G_11nWPA, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["008_2.4G_WPA_802.11n_DC_Off/On_", "2.4G_WPA_2.4G-802.11n_DCTriggerOnOff", AP_24G, 
     AP_24G80211n, AP_24G_11nWPA, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["009_2.4G_WPA_802.11n_AC_Off/On_", "2.4G_WPA_2.4G-802.11n_ACTriggerOnOff", AP_24G, 
     AP_24G80211n, AP_24G_11nWPA, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["010_2.4G_WPA2_802.11n_TV Wifi_Off/On_", "2.4G_WPA2_2.4G-802.11n_WifiTriggerOnOff", AP_24G, 
     AP_24G80211n, AP_24G_11nWPA2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["011_2.4G_WPA2_802.11n_DC_Off/On_", "2.4G_WPA2_2.4G-802.11n_DCTriggerOnOff", AP_24G, 
     AP_24G80211n, AP_24G_11nWPA2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["012_2.4G_WPA2_802.11n_AC_Off/On_", "2.4G_WPA2_2.4G-802.11n_ACTriggerOnOff", AP_24G, 
     AP_24G80211n, AP_24G_11nWPA2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["013_5G_WPA_802.11n_TV Wifi_Off/On_", "5G_WPA_5G-802.11n_WifiTriggerOnOff", AP_5G, 
     AP_5G80211n, AP_5G_WPA, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["014_5G_WPA_802.11n_DC_Off/On_", "5G_WPA_5G-802.11n_DCTriggerOnOff", AP_5G, 
     AP_5G80211n, AP_5G_WPA, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["015_5G_WPA_802.11n_AC_Off/On_", "5G_WPA_5G-802.11n_ACTriggerOnOff", AP_5G, 
     AP_5G80211n, AP_5G_WPA, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["016_5G_WPA2_802.11n_TV Wifi_Off/On_", "5G_WPA2_5G-802.11n_WifiTriggerOnOff", AP_5G, 
     AP_5G80211n, AP_5G_WPA2, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["017_5G_WPA2_802.11n_DC_Off/On_", "5G_WPA2_5G-802.11n_DCTriggerOnOff", AP_5G, 
     AP_5G80211n, AP_5G_WPA2, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["018_5G_WPA2_802.11n_AC_Off/On_", "5G_WPA2_5G-802.11n_ACTriggerOnOff", AP_5G, 
     AP_5G80211n, AP_5G_WPA2, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["019_5G_WPA_802.11ac_TV Wifi_Off/On_", "5G_WPA_5G-802.11ac_WifiTriggerOnOff", AP_5G, 
     AP_5G80211ac, AP_5G_WPA, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["020_5G_WPA_802.11ac_DC_Off/On_", "5G_WPA_5G-802.11ac_DCTriggerOnOff", AP_5G, 
     AP_5G80211ac, AP_5G_WPA, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["021_5G_WPA_802.11ac_AC_Off/On_", "5G_WPA_5G-802.11ac_ACTriggerOnOff", AP_5G, 
     AP_5G80211ac, AP_5G_WPA, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["022_5G_WPA2_802.11ac_TV Wifi_Off/On_", "5G_WPA2_5G-802.11ac_WifiTriggerOnOff", AP_5G, 
     AP_5G80211ac, AP_5G_WPA2, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["023_5G_WPA2_802.11ac_DC_Off/On_", "5G_WPA2_5G-802.11ac_DCTriggerOnOff", AP_5G, 
     AP_5G80211ac, AP_5G_WPA2, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["024_5G_WPA2_802.11ac_AC_Off/On_", "5G_WPA2_5G-802.11ac_ACTriggerOnOff", AP_5G, 
     AP_5G80211ac, AP_5G_WPA2, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
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
        log.write("AP Type: " + AP_Type +'\n')
        Test_Times = TestLoopInfo.Tframe4.get()
        print('Test loop =', Test_Times)
        count = 0
        while count <= int(Test_Times):
            Test_Loops = count+1
            print('Current test loop:', Test_Loops)
            log.write("Test loop: " + str(Test_Loops) +'\n')
            LogTextBoxUpdate("Current test loop: " + str(Test_Loops) +'\n')
            TestLoopBoxUpdate(str(Test_Loops) +'\n')
            keyevent = os.popen('adb shell input keyevent 3')
            IP_Address = EthernetInfo.IP_Address.get()
            CheckNumber = len(WifiEventList)
            for CheckIndex in range(0, CheckNumber, 1):

                run = (getRouterValue(AP_Type, WifiEventList[CheckIndex][1].split("_")[0], 1) +
                       getRouterValue(AP_Type, WifiEventList[CheckIndex][1].split("_")[1], 1) +
                       getRouterValue(AP_Type, WifiEventList[CheckIndex][1].split("_")[2], 1) +
                       getRouterValue(AP_Type, WifiEventList[CheckIndex][1].split("_")[3], 1))

                if (run == 4):
                    for wifiEvent in range(2, 8):
                        if (wifiEvent == 7):
                            WifiEventList[CheckIndex][wifiEvent]()
                            print(WifiEventList[CheckIndex][wifiEvent])
                            hostname = IP_Address
                            response = subprocess.call('ping -n 1 '+hostname, shell=True)
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
