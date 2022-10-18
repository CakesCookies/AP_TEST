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
    sleep(2)


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
    AP_Webaddress = EthernetInfo.AP_Webaddress.get()
    AP_Info.driver.get(AP_Webaddress)
    sleep(10)
    # Enter ID
    context = AP_Info.driver.find_element_by_xpath("/html/body/form/div/div/div[3]/div[3]/input")
    context.send_keys(ID)
    sleep(5)
    # Enter password    
    context = AP_Info.driver.find_element_by_xpath("/html/body/form/div/div/div[3]/div[5]/input")
    context.send_keys(PW)
    sleep(2)
    # Login
    commit = AP_Info.driver.find_element_by_xpath("/html/body/form/div/div/div[3]/div[7]")
    commit.click()
    sleep(5)
    return


def AP_WiFiEnter():
    # WIFI setting
    AP_Info.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/div[1]/div/div[12]/table/tbody/tr/td[2]").click()
    sleep(10)


def AP_24G():
    #2.4G
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td[1]/div/span").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td/select/option[1]").click()
    sleep(2)
   

def AP_5G():
    #5G
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/div/div/table/tbody/tr/td[1]/div/span").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[3]/td/select/option[2]").click()
    sleep(2)


def AP_24Gmedium():
    #2.4G_20/40 MHz
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select/option[1]").click()
    sleep(2)


def AP_24Glow():
    #2.4G_20 MHz
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select/option[2]").click()
    sleep(2)


def AP_24Ghigh():
    #2.4G_40 MHz
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select/option[3]").click()
    sleep(2)


def AP_5Gmedium():
    #5G_20/40/80 MHz
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select/option[1]").click()
    sleep(2)


def AP_5Glow():
    #5G_20 MHz
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select/option[2]").click()
    sleep(2)


def AP_5Ghigh():
    #5G_40 MHz
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select/option[3]").click()
    sleep(2)


def AP_5Gsuperhigh():
    #5G_80 MHz
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[8]/td/select/option[4]").click()
    sleep(2)


def AP_24GAuto():
    #2.4G_CH Auto
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[1]").click()
    sleep(2)


def AP_24GCH1():
    #2.4G_CH1
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[2]").click()
    sleep(2)


def AP_24GCH2():
    #2.4G_CH2
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[3]").click()
    sleep(2)


def AP_24GCH3():
    #2.4G_CH3
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[4]").click()
    sleep(2)


def AP_24GCH4():
    #2.4G_CH4
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[5]").click()
    sleep(2)


def AP_24GCH5():
    #2.4G_CH5
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[6]").click()
    sleep(2)


def AP_24GCH6():
    #2.4G_CH6
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[7]").click()
    sleep(2)


def AP_24GCH7():
    #2.4G_CH7
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[8]").click()
    sleep(2)


def AP_24GCH8():
    #2.4G_CH8
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[9]").click()
    sleep(2)


def AP_24GCH9():
    #2.4G_CH9
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[10]").click()
    sleep(2)


def AP_24GCH10():
    #2.4G_CH10
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[11]").click()
    sleep(2)


def AP_24GCH11():
    #2.4G_CH11
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[12]").click()
    sleep(2)


def AP_5GAuto():
    #5G Auto
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[1]").click()
    sleep(2)


def AP_5GCH36():
    #5G CH36
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[2]").click()
    sleep(2)


def AP_5GCH40():
    #5G CH40
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[3]").click()
    sleep(2)


def AP_5GCH44():
    #5G CH44
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[4]").click()
    sleep(2)


def AP_5GCH48():
    #5G CH48
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[5]").click()
    sleep(2)


def AP_5GCH52():
    #5G CH52
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[6]").click()
    sleep(2)


def AP_5GCH56():
    #5G CH56
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[7]").click()
    sleep(2)


def AP_5GCH60():
    #5G CH60
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[8]").click()
    sleep(2)


def AP_5GCH64():
    #5G CH64
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[9]").click()
    sleep(2)


def AP_5GCH100():
    #5G CH100
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[10]").click()
    sleep(2)


def AP_5GCH104():
    #5G CH104
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[11]").click()
    sleep(2)


def AP_5GCH108():
    #5G CH108
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[12]").click()
    sleep(2)


def AP_5GCH112():
    #5G CH112
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[13]").click()
    sleep(2)


def AP_5GCH116():
    #5G CH116
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[14]").click()
    sleep(2)


def AP_5GCH120():
    #5G CH120
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[15]").click()
    sleep(2)


def AP_5GCH124():
    #5G CH124
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[16]").click()
    sleep(2)


def AP_5GCH128():
    #5G CH128
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[17]").click()
    sleep(2)


def AP_5GCH132():
    #5G CH132
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[18]").click()
    sleep(2)


def AP_5GCH136():
    #5G CH136
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[19]").click()
    sleep(2)


def AP_5GCH140():
    #5G CH140
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[20]").click()
    sleep(2)


def AP_5GCH144():
    #5G CH144
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[21]").click()
    sleep(2)


def AP_5GCH149():
    #5G CH149
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[22]").click()
    sleep(2)


def AP_5GCH153():
    #5G CH153
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[23]").click()
    sleep(2)


def AP_5GCH157():
    #5G CH157
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[24]").click()
    sleep(2)


def AP_5GCH161():
    #5G CH161
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[25]").click()
    sleep(2)


def AP_5GCH165():
    #5G CH165
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select").click()
    sleep(2)
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table[1]/tbody/tr[9]/td/select/option[26]").click()
    sleep(2)


def AP_24GWPASSIDConnect():
    SSIDFrame24 = WifiInfo.SSIDFrame24.get()
    PWFrame24 = WifiInfo.PWFrame24.get()
    # Save
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/div[5]/input").click()
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
    AP_Info.driver.find_element_by_xpath("/html/body/form[2]/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/div[5]/input").click()
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
    # SSID 2.4G Disable
    target = AP_Info.driver.find_element_by_css_selector("#Advanced_WAdvanced_Content_tab > span").click()
    sleep(3)
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/select")
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/select/option[1]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/input[2]").click()
    sleep(3)
    # SAVE
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/div[9]/input").click()
    sleep(3)
    confirm = AP_Info.driver.switch_to.alert
    confirm.accept()
    sleep(40)
    #SSID 5G Disable
    target = AP_Info.driver.find_element_by_css_selector("#Advanced_WAdvanced_Content_tab > span").click()
    sleep(3)
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/select")
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/select/option[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/input[2]").click()
    sleep(3)
    # SAVE
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/div[9]/input").click()
    sleep(3)
    confirm = AP_Info.driver.switch_to.alert
    confirm.accept()
    sleep(40)
    # SSID 2.4G Enable
    target = AP_Info.driver.find_element_by_css_selector("#Advanced_WAdvanced_Content_tab > span").click()
    sleep(3)
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/select")
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/select/option[1]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/input[1]").click()
    sleep(3)
    # SAVE
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/div[9]/input").click()
    sleep(40)
    # SSID 5G Enable
    target = AP_Info.driver.find_element_by_css_selector("#Advanced_WAdvanced_Content_tab > span").click()
    sleep(3)
    target = AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/select")
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td/select/option[2]").click()
    sleep(3)
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/input[1]").click()
    sleep(3)
    # SAVE
    AP_Info.driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[3]/div/table/tbody/tr/td/table/tbody/tr/td/div[9]/input").click()
    sleep(40)


def ConnectionTest():
    sleep(15)


def Pingip():
    sleep(2)


WifiEventList = [
    ["001_2.4G_-_-_20/40 MHz_Auto_TV Wifi_Off/On_", "2.4G_Auto_2.4G-Auto_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["002_2.4G_-_-_20/40 MHz_Auto_DC_Off/On_", "2.4G_Auto_2.4G-Auto_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["003_2.4G_-_-_20/40 MHz_Auto_AC_Off/On_", "2.4G_Auto_2.4G-Auto_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["004_2.4G_-_-_20/40 MHz_Auto_AP_Off/On_", "2.4G_Auto_2.4G-Auto_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["005_2.4G_-_-_20/40 MHz_Auto_IP_ConnectionTest_", "2.4G_Auto_2.4G-Auto_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["006_2.4G_-_-_20/40 MHz_CH1_TV Wifi_Off/On_", "2.4G_Auto_CH1_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["007_2.4G_-_-_20/40 MHz_CH1_DC_Off/On_", "2.4G_Auto_CH1_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["008_2.4G_-_-_20/40 MHz_CH1_AC_Off/On_", "2.4G_Auto_CH1_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["009_2.4G_-_-_20/40 MHz_CH1_AP_Off/On_", "2.4G_Auto_CH1_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["010_2.4G_-_-_20/40 MHz_CH1_IP_ConnectionTest_", "2.4G_Auto_CH1_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],  
    ["011_2.4G_-_-_20/40 MHz_CH2_TV Wifi_Off/On_", "2.4G_Auto_CH2_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["012_2.4G_-_-_20/40 MHz_CH2_DC_Off/On_", "2.4G_Auto_CH2_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["013_2.4G_-_-_20/40 MHz_CH2_AC_Off/On_", "2.4G_Auto_CH2_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["014_2.4G_-_-_20/40 MHz_CH2_AP_Off/On_", "2.4G_Auto_CH2_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["015_2.4G_-_-_20/40 MHz_CH2_IP_ConnectionTest_", "2.4G_Auto_CH2_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["016_2.4G_-_-_20/40 MHz_CH3_TV Wifi_Off/On_", "2.4G_Auto_CH3_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["017_2.4G_-_-_20/40 MHz_CH3_DC_Off/On_", "2.4G_Auto_CH3_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["018_2.4G_-_-_20/40 MHz_CH3_AC_Off/On_", "2.4G_Auto_CH3_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["019_2.4G_-_-_20/40 MHz_CH3_AP_Off/On_", "2.4G_Auto_CH3_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["020_2.4G_-_-_20/40 MHz_CH3_IP_ConnectionTest_", "2.4G_Auto_CH3_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["021_2.4G_-_-_20/40 MHz_CH4_TV Wifi_Off/On_", "2.4G_Auto_CH4_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["022_2.4G_-_-_20/40 MHz_CH4_DC_Off/On_", "2.4G_Auto_CH4_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["023_2.4G_-_-_20/40 MHz_CH4_AC_Off/On_", "2.4G_Auto_CH4_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["024_2.4G_-_-_20/40 MHz_CH4_AP_Off/On_", "2.4G_Auto_CH4_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["025_2.4G_-_-_20/40 MHz_CH4_IP_ConnectionTest_", "2.4G_Auto_CH4_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["026_2.4G_-_-_20/40 MHz_CH5_TV Wifi_Off/On_", "2.4G_Auto_CH5_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["027_2.4G_-_-_20/40 MHz_CH5_DC_Off/On_", "2.4G_Auto_CH5_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["028_2.4G_-_-_20/40 MHz_CH5_AC_Off/On_", "2.4G_Auto_CH5_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["029_2.4G_-_-_20/40 MHz_CH5_AP_Off/On_", "2.4G_Auto_CH5_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["030_2.4G_-_-_20/40 MHz_CH5_IP_ConnectionTest_", "2.4G_Auto_CH5_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["031_2.4G_-_-_20/40 MHz_CH6_TV Wifi_Off/On_", "2.4G_Auto_CH6_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["032_2.4G_-_-_20/40 MHz_CH6_DC_Off/On_", "2.4G_Auto_CH6_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["033_2.4G_-_-_20/40 MHz_CH6_AC_Off/On_", "2.4G_Auto_CH6_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["034_2.4G_-_-_20/40 MHz_CH6_AP_Off/On_", "2.4G_Auto_CH6_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["035_2.4G_-_-_20/40 MHz_CH6_IP_ConnectionTest_", "2.4G_Auto_CH6_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["036_2.4G_-_-_20/40 MHz_CH7_TV Wifi_Off/On_", "2.4G_Auto_CH7_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["037_2.4G_-_-_20/40 MHz_CH7_DC_Off/On_", "2.4G_Auto_CH7_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["038_2.4G_-_-_20/40 MHz_CH7_AC_Off/On_", "2.4G_Auto_CH7_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["039_2.4G_-_-_20/40 MHz_CH7_AP_Off/On_", "2.4G_Auto_CH7_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["040_2.4G_-_-_20/40 MHz_CH7_IP_ConnectionTest_", "2.4G_Auto_CH7_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["041_2.4G_-_-_20/40 MHz_CH8_TV Wifi_Off/On_", "2.4G_Auto_CH8_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["042_2.4G_-_-_20/40 MHz_CH8_DC_Off/On_", "2.4G_Auto_CH8_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["043_2.4G_-_-_20/40 MHz_CH8_AC_Off/On_", "2.4G_Auto_CH8_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["044_2.4G_-_-_20/40 MHz_CH8_AP_Off/On_", "2.4G_Auto_CH8_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["045_2.4G_-_-_20/40 MHz_CH8_IP_ConnectionTest_", "2.4G_Auto_CH8_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["046_2.4G_-_-_20/40 MHz_CH9_TV Wifi_Off/On_", "2.4G_Auto_CH9_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["047_2.4G_-_-_20/40 MHz_CH9_DC_Off/On_", "2.4G_Auto_CH9_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["048_2.4G_-_-_20/40 MHz_CH9_AC_Off/On_", "2.4G_Auto_CH9_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["049_2.4G_-_-_20/40 MHz_CH9_AP_Off/On_", "2.4G_Auto_CH9_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["050_2.4G_-_-_20/40 MHz_CH9_IP_ConnectionTest_", "2.4G_Auto_CH9_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["051_2.4G_-_-_20/40 MHz_CH10_TV Wifi_Off/On_", "2.4G_Auto_CH10_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["052_2.4G_-_-_20/40 MHz_CH10_DC_Off/On_", "2.4G_Auto_CH10_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["053_2.4G_-_-_20/40 MHz_CH10_AC_Off/On_", "2.4G_Auto_CH10_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["054_2.4G_-_-_20/40 MHz_CH10_AP_Off/On_", "2.4G_Auto_CH10_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["055_2.4G_-_-_20/40 MHz_CH10_IP_ConnectionTest_", "2.4G_Auto_CH10_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["056_2.4G_-_-_20/40 MHz_CH11_TV Wifi_Off/On_", "2.4G_Auto_CH11_WifiTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["057_2.4G_-_-_20/40 MHz_CH11_DC_Off/On_", "2.4G_Auto_CH11_DCTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["058_2.4G_-_-_20/40 MHz_CH11_AC_Off/On_", "2.4G_Auto_CH11_ACTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["059_2.4G_-_-_20/40 MHz_CH11_AP_Off/On_", "2.4G_Auto_CH11_APTriggerOnOff", 
     AP_24G, AP_24Gmedium, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["060_2.4G_-_-_20/40 MHz_CH11_IP_ConnectionTest_", "2.4G_Auto_CH11_ConnectionTest", 
     AP_24G, AP_24Gmedium, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["061_2.4G_-_-_20 MHz_Auto_TV Wifi_Off/On_", "2.4G_20MHz_2.4G-Auto_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["062_2.4G_-_-_20 MHz_Auto_DC_Off/On_", "2.4G_20MHz_2.4G-Auto_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["063_2.4G_-_-_20 MHz_Auto_AC_Off/On_", "2.4G_20MHz_2.4G-Auto_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["064_2.4G_-_-_20 MHz_Auto_AP_Off/On_", "2.4G_20MHz_2.4G-Auto_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["065_2.4G_-_-_20 MHz_Auto_IP_ConnectionTest_", "2.4G_20MHz_2.4G-Auto_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["066_2.4G_-_-_20 MHz_CH1_TV Wifi_Off/On_", "2.4G_20MHz_CH1_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["067_2.4G_-_-_20 MHz_CH1_DC_Off/On_", "2.4G_20MHz_CH1_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["068_2.4G_-_-_20 MHz_CH1_AC_Off/On_", "2.4G_20MHz_CH1_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["069_2.4G_-_-_20 MHz_CH1_AP_Off/On_", "2.4G_20MHz_CH1_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["070_2.4G_-_-_20 MHz_CH1_IP_ConnectionTest_", "2.4G_20MHz_CH1_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["071_2.4G_-_-_20 MHz_CH2_TV Wifi_Off/On_", "2.4G_20MHz_CH2_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["072_2.4G_-_-_20 MHz_CH2_DC_Off/On_", "2.4G_20MHz_CH2_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["073_2.4G_-_-_20 MHz_CH2_AC_Off/On_", "2.4G_20MHz_CH2_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["074_2.4G_-_-_20 MHz_CH2_AP_Off/On_", "2.4G_20MHz_CH2_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["075_2.4G_-_-_20 MHz_CH2_IP_ConnectionTest_", "2.4G_20MHz_CH2_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["076_2.4G_-_-_20 MHz_CH3_TV Wifi_Off/On_", "2.4G_20MHz_CH3_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["077_2.4G_-_-_20 MHz_CH3_DC_Off/On_", "2.4G_20MHz_CH3_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["078_2.4G_-_-_20 MHz_CH3_AC_Off/On_", "2.4G_20MHz_CH3_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["079_2.4G_-_-_20 MHz_CH3_AP_Off/On_", "2.4G_20MHz_CH3_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["080_2.4G_-_-_20 MHz_CH3_IP_ConnectionTest_", "2.4G_20MHz_CH3_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["081_2.4G_-_-_20 MHz_CH4_TV Wifi_Off/On_", "2.4G_20MHz_CH4_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["082_2.4G_-_-_20 MHz_CH4_DC_Off/On_", "2.4G_20MHz_CH4_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["083_2.4G_-_-_20 MHz_CH4_AC_Off/On_", "2.4G_20MHz_CH4_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["084_2.4G_-_-_20 MHz_CH4_AP_Off/On_", "2.4G_20MHz_CH4_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["085_2.4G_-_-_20 MHz_CH4_IP_ConnectionTest_", "2.4G_20MHz_CH4_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["086_2.4G_-_-_20 MHz_CH5_TV Wifi_Off/On_", "2.4G_20MHz_CH5_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["087_2.4G_-_-_20 MHz_CH5_DC_Off/On_", "2.4G_20MHz_CH5_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["088_2.4G_-_-_20 MHz_CH5_AC_Off/On_", "2.4G_20MHz_CH5_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["089_2.4G_-_-_20 MHz_CH5_AP_Off/On_", "2.4G_20MHz_CH5_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["090_2.4G_-_-_20 MHz_CH5_IP_ConnectionTest_", "2.4G_20MHz_CH5_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["091_2.4G_-_-_20 MHz_CH6_TV Wifi_Off/On_", "2.4G_20MHz_CH6_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["092_2.4G_-_-_20 MHz_CH6_DC_Off/On_", "2.4G_20MHz_CH6_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["093_2.4G_-_-_20 MHz_CH6_AC_Off/On_", "2.4G_20MHz_CH6_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["094_2.4G_-_-_20 MHz_CH6_AP_Off/On_", "2.4G_20MHz_CH6_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["095_2.4G_-_-_20 MHz_CH6_IP_ConnectionTest_", "2.4G_20MHz_CH6_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["096_2.4G_-_-_20 MHz_CH7_TV Wifi_Off/On_", "2.4G_20MHz_CH7_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["097_2.4G_-_-_20 MHz_CH7_DC_Off/On_", "2.4G_20MHz_CH7_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["098_2.4G_-_-_20 MHz_CH7_AC_Off/On_", "2.4G_20MHz_CH7_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["099_2.4G_-_-_20 MHz_CH7_AP_Off/On_", "2.4G_20MHz_CH7_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["100_2.4G_-_-_20 MHz_CH7_IP_ConnectionTest_", "2.4G_20MHz_CH7_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["101_2.4G_-_-_20 MHz_CH8_TV Wifi_Off/On_", "2.4G_20MHz_CH8_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["102_2.4G_-_-_20 MHz_CH8_DC_Off/On_", "2.4G_20MHz_CH8_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["103_2.4G_-_-_20 MHz_CH8_AC_Off/On_", "2.4G_20MHz_CH8_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["104_2.4G_-_-_20 MHz_CH8_AP_Off/On_", "2.4G_20MHz_CH8_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["105_2.4G_-_-_20 MHz_CH8_IP_ConnectionTest_", "2.4G_20MHz_CH8_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["106_2.4G_-_-_20 MHz_CH9_TV Wifi_Off/On_", "2.4G_20MHz_CH9_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["107_2.4G_-_-_20 MHz_CH9_DC_Off/On_", "2.4G_20MHz_CH9_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["108_2.4G_-_-_20 MHz_CH9_AC_Off/On_", "2.4G_20MHz_CH9_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["109_2.4G_-_-_20 MHz_CH9_AP_Off/On_", "2.4G_20MHz_CH9_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["110_2.4G_-_-_20 MHz_CH9_IP_ConnectionTest_", "2.4G_20MHz_CH9_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["111_2.4G_-_-_20 MHz_CH10_TV Wifi_Off/On_", "2.4G_20MHz_CH10_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["112_2.4G_-_-_20 MHz_CH10_DC_Off/On_", "2.4G_20MHz_CH10_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["113_2.4G_-_-_20 MHz_CH10_AC_Off/On_", "2.4G_20MHz_CH10_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["114_2.4G_-_-_20 MHz_CH10_AP_Off/On_", "2.4G_20MHz_CH10_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["115_2.4G_-_-_20 MHz_CH10_IP_ConnectionTest_", "2.4G_20MHz_CH10_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["116_2.4G_-_-_20 MHz_CH11_TV Wifi_Off/On_", "2.4G_20MHz_CH11_WifiTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["117_2.4G_-_-_20 MHz_CH11_DC_Off/On_", "2.4G_20MHz_CH11_DCTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["118_2.4G_-_-_20 MHz_CH11_AC_Off/On_", "2.4G_20MHz_CH11_ACTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["119_2.4G_-_-_20 MHz_CH11_AP_Off/On_", "2.4G_20MHz_CH11_APTriggerOnOff", 
     AP_24G, AP_24Glow, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["120_2.4G_-_-_20 MHz_CH11_IP_ConnectionTest_", "2.4G_20MHz_CH11_ConnectionTest", 
     AP_24G, AP_24Glow, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["121_2.4G_-_-_40 MHz_Auto_TV Wifi_Off/On_", "2.4G_40MHz_2.4G-Auto_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GAuto, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["122_2.4G_-_-_40 MHz_Auto_DC_Off/On_", "2.4G_40MHz_2.4G-Auto_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GAuto, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["123_2.4G_-_-_40 MHz_Auto_AC_Off/On_", "2.4G_40MHz_2.4G-Auto_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GAuto, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["124_2.4G_-_-_40 MHz_Auto_AP_Off/On_", "2.4G_40MHz_2.4G-Auto_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GAuto, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["125_2.4G_-_-_40 MHz_Auto_IP_ConnectionTest_", "2.4G_40MHz_2.4G-Auto_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GAuto, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["126_2.4G_-_-_40 MHz_CH1_TV Wifi_Off/On_", "2.4G_40MHz_CH1_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH1, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["127_2.4G_-_-_40 MHz_CH1_DC_Off/On_", "2.4G_40MHz_CH1_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH1, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["128_2.4G_-_-_40 MHz_CH1_AC_Off/On_", "2.4G_40MHz_CH1_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH1, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["129_2.4G_-_-_40 MHz_CH1_AP_Off/On_", "2.4G_40MHz_CH1_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH1, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["130_2.4G_-_-_40 MHz_CH1_IP_ConnectionTest_", "2.4G_40MHz_CH1_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH1, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["131_2.4G_-_-_40 MHz_CH2_TV Wifi_Off/On_", "2.4G_40MHz_CH2_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH2, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["132_2.4G_-_-_40 MHz_CH2_DC_Off/On_", "2.4G_40MHz_CH2_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH2, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["133_2.4G_-_-_40 MHz_CH2_AC_Off/On_", "2.4G_40MHz_CH2_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH2, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["134_2.4G_-_-_40 MHz_CH2_AP_Off/On_", "2.4G_40MHz_CH2_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH2, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["135_2.4G_-_-_40 MHz_CH2_IP_ConnectionTest_", "2.4G_40MHz_CH2_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH2, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["136_2.4G_-_-_40 MHz_CH3_TV Wifi_Off/On_", "2.4G_40MHz_CH3_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH3, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["137_2.4G_-_-_40 MHz_CH3_DC_Off/On_", "2.4G_40MHz_CH3_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH3, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["138_2.4G_-_-_40 MHz_CH3_AC_Off/On_", "2.4G_40MHz_CH3_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH3, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["139_2.4G_-_-_40 MHz_CH3_AP_Off/On_", "2.4G_40MHz_CH3_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH3, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["140_2.4G_-_-_40 MHz_CH3_IP_ConnectionTest_", "2.4G_40MHz_CH3_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH3, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["141_2.4G_-_-_40 MHz_CH4_TV Wifi_Off/On_", "2.4G_40MHz_CH4_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH4, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["142_2.4G_-_-_40 MHz_CH4_DC_Off/On_", "2.4G_40MHz_CH4_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH4, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["143_2.4G_-_-_40 MHz_CH4_AC_Off/On_", "2.4G_40MHz_CH4_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH4, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["144_2.4G_-_-_40 MHz_CH4_AP_Off/On_", "2.4G_40MHz_CH4_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH4, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["145_2.4G_-_-_40 MHz_CH4_IP_ConnectionTest_", "2.4G_40MHz_CH4_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH4, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["146_2.4G_-_-_40 MHz_CH5_TV Wifi_Off/On_", "2.4G_40MHz_CH5_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH5, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["147_2.4G_-_-_40 MHz_CH5_DC_Off/On_", "2.4G_40MHz_CH5_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH5, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["148_2.4G_-_-_40 MHz_CH5_AC_Off/On_", "2.4G_40MHz_CH5_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH5, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["149_2.4G_-_-_40 MHz_CH5_AP_Off/On_", "2.4G_40MHz_CH5_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH5, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["150_2.4G_-_-_40 MHz_CH5_IP_ConnectionTest_", "2.4G_40MHz_CH5_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH5, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["151_2.4G_-_-_40 MHz_CH6_TV Wifi_Off/On_", "2.4G_40MHz_CH6_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH6, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["152_2.4G_-_-_40 MHz_CH6_DC_Off/On_", "2.4G_40MHz_CH6_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH6, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["153_2.4G_-_-_40 MHz_CH6_AC_Off/On_", "2.4G_40MHz_CH6_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH6, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["154_2.4G_-_-_40 MHz_CH6_AP_Off/On_", "2.4G_40MHz_CH6_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH6, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["155_2.4G_-_-_40 MHz_CH6_IP_ConnectionTest_", "2.4G_40MHz_CH6_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH6, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["156_2.4G_-_-_40 MHz_CH7_TV Wifi_Off/On_", "2.4G_40MHz_CH7_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH7, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["157_2.4G_-_-_40 MHz_CH7_DC_Off/On_", "2.4G_40MHz_CH7_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH7, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["158_2.4G_-_-_40 MHz_CH7_AC_Off/On_", "2.4G_40MHz_CH7_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH7, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["159_2.4G_-_-_40 MHz_CH7_AP_Off/On_", "2.4G_40MHz_CH7_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH7, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["160_2.4G_-_-_40 MHz_CH7_IP_ConnectionTest_", "2.4G_40MHz_CH7_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH7, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["161_2.4G_-_-_40 MHz_CH8_TV Wifi_Off/On_", "2.4G_40MHz_CH8_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH8, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["162_2.4G_-_-_40 MHz_CH8_DC_Off/On_", "2.4G_40MHz_CH8_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH8, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["163_2.4G_-_-_40 MHz_CH8_AC_Off/On_", "2.4G_40MHz_CH8_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH8, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["164_2.4G_-_-_40 MHz_CH8_AP_Off/On_", "2.4G_40MHz_CH8_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH8, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["165_2.4G_-_-_40 MHz_CH8_IP_ConnectionTest_", "2.4G_40MHz_CH8_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH8, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["166_2.4G_-_-_40 MHz_CH9_TV Wifi_Off/On_", "2.4G_40MHz_CH9_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH9, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["167_2.4G_-_-_40 MHz_CH9_DC_Off/On_", "2.4G_40MHz_CH9_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH9, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["168_2.4G_-_-_40 MHz_CH9_AC_Off/On_", "2.4G_40MHz_CH9_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH9, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["169_2.4G_-_-_40 MHz_CH9_AP_Off/On_", "2.4G_40MHz_CH9_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH9, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["170_2.4G_-_-_40 MHz_CH9_IP_ConnectionTest_", "2.4G_40MHz_CH9_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH9, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["171_2.4G_-_-_40 MHz_CH10_TV Wifi_Off/On_", "2.4G_40MHz_CH10_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH10, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["172_2.4G_-_-_40 MHz_CH10_DC_Off/On_", "2.4G_40MHz_CH10_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH10, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["173_2.4G_-_-_40 MHz_CH10_AC_Off/On_", "2.4G_40MHz_CH10_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH10, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["174_2.4G_-_-_40 MHz_CH10_AP_Off/On_", "2.4G_40MHz_CH10_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH10, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["175_2.4G_-_-_40 MHz_CH10_IP_ConnectionTest_", "2.4G_40MHz_CH10_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH10, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["176_2.4G_-_-_40 MHz_CH11_TV Wifi_Off/On_", "2.4G_40MHz_CH11_WifiTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH11, AP_24GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["177_2.4G_-_-_40 MHz_CH11_DC_Off/On_", "2.4G_40MHz_CH11_DCTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH11, AP_24GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["178_2.4G_-_-_40 MHz_CH11_AC_Off/On_", "2.4G_40MHz_CH11_ACTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH11, AP_24GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["179_2.4G_-_-_40 MHz_CH11_AP_Off/On_", "2.4G_40MHz_CH11_APTriggerOnOff", 
     AP_24G, AP_24Ghigh, AP_24GCH11, AP_24GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["180_2.4G_-_-_40 MHz_CH11_IP_ConnectionTest_", "2.4G_40MHz_CH11_ConnectionTest", 
     AP_24G, AP_24Ghigh, AP_24GCH11, AP_24GWPASSIDConnect, ConnectionTest, Pingip],
    ["181_5G_-_-_20/40/80 MHz_Auto_TV Wifi_Off/On_", "5G_Auto_5G-Auto_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["182_5G_-_-_20/40/80 MHz_Auto_DC_Off/On_", "5G_Auto_5G-Auto_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["183_5G_-_-_20/40/80 MHz_Auto_AC_Off/On_", "5G_Auto_5G-Auto_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["184_5G_-_-_20/40/80 MHz_Auto_AP_Off/On_", "5G_Auto_5G-Auto_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["185_5G_-_-_20/40/80 MHz_Auto_IP_ConnectionTest_", "5G_Auto_5G-Auto_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["186_5G_-_-_20/40/80 MHz_CH36_TV Wifi_Off/On_", "5G_Auto_CH36_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["187_5G_-_-_20/40/80 MHz_CH36_DC_Off/On_", "5G_Auto_CH36_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["188_5G_-_-_20/40/80 MHz_CH36_AC_Off/On_", "5G_Auto_CH36_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["189_5G_-_-_20/40/80 MHz_CH36_AP_Off/On_", "5G_Auto_CH36_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["190_5G_-_-_20/40/80 MHz_CH36_IP_ConnectionTest_", "5G_Auto_CH36_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["191_5G_-_-_20/40/80 MHz_CH40_TV Wifi_Off/On_", "5G_Auto_CH40_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["192_5G_-_-_20/40/80 MHz_CH40_DC_Off/On_", "5G_Auto_CH40_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["193_5G_-_-_20/40/80 MHz_CH40_AC_Off/On_", "5G_Auto_CH40_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["194_5G_-_-_20/40/80 MHz_CH40_AP_Off/On_", "5G_Auto_CH40_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["195_5G_-_-_20/40/80 MHz_CH40_IP_ConnectionTest_", "5G_Auto_CH40_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["196_5G_-_-_20/40/80 MHz_CH44_TV Wifi_Off/On_", "5G_Auto_CH44_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["197_5G_-_-_20/40/80 MHz_CH44_DC_Off/On_", "5G_Auto_CH44_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["198_5G_-_-_20/40/80 MHz_CH44_AC_Off/On_", "5G_Auto_CH44_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["199_5G_-_-_20/40/80 MHz_CH44_AP_Off/On_", "5G_Auto_CH44_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["200_5G_-_-_20/40/80 MHz_CH44_IP_ConnectionTest_", "5G_Auto_CH44_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["201_5G_-_-_20/40/80 MHz_CH48_TV Wifi_Off/On_", "5G_Auto_CH48_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["202_5G_-_-_20/40/80 MHz_CH48_DC_Off/On_", "5G_Auto_CH48_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["203_5G_-_-_20/40/80 MHz_CH48_AC_Off/On_", "5G_Auto_CH48_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["204_5G_-_-_20/40/80 MHz_CH48_AP_Off/On_", "5G_Auto_CH48_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["205_5G_-_-_20/40/80 MHz_CH48_IP_ConnectionTest_", "5G_Auto_CH48_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["206_5G_-_-_20/40/80 MHz_CH52_TV Wifi_Off/On_", "5G_Auto_CH52_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH52, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["207_5G_-_-_20/40/80 MHz_CH52_DC_Off/On_", "5G_Auto_CH52_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH52, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["208_5G_-_-_20/40/80 MHz_CH52_AC_Off/On_", "5G_Auto_CH52_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH52, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["209_5G_-_-_20/40/80 MHz_CH52_AP_Off/On_", "5G_Auto_CH52_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH52, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["210_5G_-_-_20/40/80 MHz_CH52_IP_ConnectionTest_", "5G_Auto_CH52_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH52, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["211_5G_-_-_20/40/80 MHz_CH56_TV Wifi_Off/On_", "5G_Auto_CH56_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH56, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["212_5G_-_-_20/40/80 MHz_CH56_DC_Off/On_", "5G_Auto_CH56_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH56, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["213_5G_-_-_20/40/80 MHz_CH56_AC_Off/On_", "5G_Auto_CH56_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH56, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["214_5G_-_-_20/40/80 MHz_CH56_AP_Off/On_", "5G_Auto_CH56_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH56, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["215_5G_-_-_20/40/80 MHz_CH56_IP_ConnectionTest_", "5G_Auto_CH56_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH56, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["216_5G_-_-_20/40/80 MHz_CH60_TV Wifi_Off/On_", "5G_Auto_CH60_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH60, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["217_5G_-_-_20/40/80 MHz_CH60_DC_Off/On_", "5G_Auto_CH60_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH60, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["218_5G_-_-_20/40/80 MHz_CH60_AC_Off/On_", "5G_Auto_CH60_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH60, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["219_5G_-_-_20/40/80 MHz_CH60_AP_Off/On_", "5G_Auto_CH60_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH60, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["220_5G_-_-_20/40/80 MHz_CH60_IP_ConnectionTest_", "5G_Auto_CH60_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH60, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["221_5G_-_-_20/40/80 MHz_CH64_TV Wifi_Off/On_", "5G_Auto_CH64_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH64, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["222_5G_-_-_20/40/80 MHz_CH64_DC_Off/On_", "5G_Auto_CH64_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH64, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["223_5G_-_-_20/40/80 MHz_CH64_AC_Off/On_", "5G_Auto_CH64_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH64, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["224_5G_-_-_20/40/80 MHz_CH64_AP_Off/On_", "5G_Auto_CH64_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH64, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["225_5G_-_-_20/40/80 MHz_CH64_IP_ConnectionTest_", "5G_Auto_CH64_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH64, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["226_5G_-_-_20/40/80 MHz_CH100_TV Wifi_Off/On_", "5G_Auto_CH100_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH100, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["227_5G_-_-_20/40/80 MHz_CH100_DC_Off/On_", "5G_Auto_CH100_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH100, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["228_5G_-_-_20/40/80 MHz_CH100_AC_Off/On_", "5G_Auto_CH100_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH100, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["229_5G_-_-_20/40/80 MHz_CH100_AP_Off/On_", "5G_Auto_CH100_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH100, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["230_5G_-_-_20/40/80 MHz_CH100_IP_ConnectionTest_", "5G_Auto_CH100_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH100, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["231_5G_-_-_20/40/80 MHz_CH104_TV Wifi_Off/On_", "5G_Auto_CH104_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH104, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["232_5G_-_-_20/40/80 MHz_CH104_DC_Off/On_", "5G_Auto_CH104_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH104, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["233_5G_-_-_20/40/80 MHz_CH104_AC_Off/On_", "5G_Auto_CH104_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH104, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["234_5G_-_-_20/40/80 MHz_CH104_AP_Off/On_", "5G_Auto_CH104_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH104, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["235_5G_-_-_20/40/80 MHz_CH104_IP_ConnectionTest_", "5G_Auto_CH104_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH104, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["236_5G_-_-_20/40/80 MHz_CH108_TV Wifi_Off/On_", "5G_Auto_CH108_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH108, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["237_5G_-_-_20/40/80 MHz_CH108_DC_Off/On_", "5G_Auto_CH108_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH108, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["238_5G_-_-_20/40/80 MHz_CH108_AC_Off/On_", "5G_Auto_CH108_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH108, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["239_5G_-_-_20/40/80 MHz_CH108_AP_Off/On_", "5G_Auto_CH108_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH108, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["240_5G_-_-_20/40/80 MHz_CH108_IP_ConnectionTest_", "5G_Auto_CH108_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH108, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["241_5G_-_-_20/40/80 MHz_CH112_TV Wifi_Off/On_", "5G_Auto_CH112_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH112, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["242_5G_-_-_20/40/80 MHz_CH112_DC_Off/On_", "5G_Auto_CH112_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH112, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["243_5G_-_-_20/40/80 MHz_CH112_AC_Off/On_", "5G_Auto_CH112_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH112, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["244_5G_-_-_20/40/80 MHz_CH112_AP_Off/On_", "5G_Auto_CH112_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH112, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["245_5G_-_-_20/40/80 MHz_CH112_IP_ConnectionTest_", "5G_Auto_CH112_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH112, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["246_5G_-_-_20/40/80 MHz_CH116_TV Wifi_Off/On_", "5G_Auto_CH116_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH116, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["247_5G_-_-_20/40/80 MHz_CH116_DC_Off/On_", "5G_Auto_CH116_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH116, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["248_5G_-_-_20/40/80 MHz_CH116_AC_Off/On_", "5G_Auto_CH116_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH116, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["249_5G_-_-_20/40/80 MHz_CH116_AP_Off/On_", "5G_Auto_CH116_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH116, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["250_5G_-_-_20/40/80 MHz_CH116_IP_ConnectionTest_", "5G_Auto_CH116_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH116, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["251_5G_-_-_20/40/80 MHz_CH120_TV Wifi_Off/On_", "5G_Auto_CH120_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH120, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["252_5G_-_-_20/40/80 MHz_CH120_DC_Off/On_", "5G_Auto_CH120_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH120, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["253_5G_-_-_20/40/80 MHz_CH120_AC_Off/On_", "5G_Auto_CH120_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH120, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["254_5G_-_-_20/40/80 MHz_CH120_AP_Off/On_", "5G_Auto_CH120_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH120, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["255_5G_-_-_20/40/80 MHz_CH120_IP_ConnectionTest_", "5G_Auto_CH120_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH120, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["256_5G_-_-_20/40/80 MHz_CH124_TV Wifi_Off/On_", "5G_Auto_CH124_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH124, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["257_5G_-_-_20/40/80 MHz_CH124_DC_Off/On_", "5G_Auto_CH124_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH124, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["258_5G_-_-_20/40/80 MHz_CH124_AC_Off/On_", "5G_Auto_CH124_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH124, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["259_5G_-_-_20/40/80 MHz_CH124_AP_Off/On_", "5G_Auto_CH124_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH124, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["260_5G_-_-_20/40/80 MHz_CH124_IP_ConnectionTest_", "5G_Auto_CH124_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH124, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["261_5G_-_-_20/40/80 MHz_CH128_TV Wifi_Off/On_", "5G_Auto_CH128_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH128, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["262_5G_-_-_20/40/80 MHz_CH128_DC_Off/On_", "5G_Auto_CH128_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH128, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["263_5G_-_-_20/40/80 MHz_CH128_AC_Off/On_", "5G_Auto_CH128_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH128, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["264_5G_-_-_20/40/80 MHz_CH128_AP_Off/On_", "5G_Auto_CH128_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH128, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["265_5G_-_-_20/40/80 MHz_CH128_IP_ConnectionTest_", "5G_Auto_CH128_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH128, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["266_5G_-_-_20/40/80 MHz_CH132_TV Wifi_Off/On_", "5G_Auto_CH132_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH132, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["267_5G_-_-_20/40/80 MHz_CH132_DC_Off/On_", "5G_Auto_CH132_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH132, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["268_5G_-_-_20/40/80 MHz_CH132_AC_Off/On_", "5G_Auto_CH132_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH132, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["269_5G_-_-_20/40/80 MHz_CH132_AP_Off/On_", "5G_Auto_CH132_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH132, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["270_5G_-_-_20/40/80 MHz_CH132_IP_ConnectionTest_", "5G_Auto_CH132_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH132, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["271_5G_-_-_20/40/80 MHz_CH136_TV Wifi_Off/On_", "5G_Auto_CH136_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH136, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["272_5G_-_-_20/40/80 MHz_CH136_DC_Off/On_", "5G_Auto_CH136_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH136, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["273_5G_-_-_20/40/80 MHz_CH136_AC_Off/On_", "5G_Auto_CH136_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH136, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["274_5G_-_-_20/40/80 MHz_CH136_AP_Off/On_", "5G_Auto_CH136_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH136, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["275_5G_-_-_20/40/80 MHz_CH136_IP_ConnectionTest_", "5G_Auto_CH136_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH136, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["276_5G_-_-_20/40/80 MHz_CH140_TV Wifi_Off/On_", "5G_Auto_CH140_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH140, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["277_5G_-_-_20/40/80 MHz_CH140_DC_Off/On_", "5G_Auto_CH140_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH140, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["278_5G_-_-_20/40/80 MHz_CH140_AC_Off/On_", "5G_Auto_CH140_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH140, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["279_5G_-_-_20/40/80 MHz_CH140_AP_Off/On_", "5G_Auto_CH140_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH140, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["280_5G_-_-_20/40/80 MHz_CH140_IP_ConnectionTest_", "5G_Auto_CH140_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH140, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["281_5G_-_-_20/40/80 MHz_CH144_TV Wifi_Off/On_", "5G_Auto_CH144_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH144, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["282_5G_-_-_20/40/80 MHz_CH144_DC_Off/On_", "5G_Auto_CH144_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH144, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["283_5G_-_-_20/40/80 MHz_CH144_AC_Off/On_", "5G_Auto_CH144_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH144, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["284_5G_-_-_20/40/80 MHz_CH144_AP_Off/On_", "5G_Auto_CH144_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH144, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["285_5G_-_-_20/40/80 MHz_CH144_IP_ConnectionTest_", "5G_Auto_CH144_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH144, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["286_5G_-_-_20/40/80 MHz_CH149_TV Wifi_Off/On_", "5G_Auto_CH149_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["287_5G_-_-_20/40/80 MHz_CH149_DC_Off/On_", "5G_Auto_CH149_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["288_5G_-_-_20/40/80 MHz_CH149_AC_Off/On_", "5G_Auto_CH149_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["289_5G_-_-_20/40/80 MHz_CH149_AP_Off/On_", "5G_Auto_CH149_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["290_5G_-_-_20/40/80 MHz_CH149_IP_ConnectionTest_", "5G_Auto_CH149_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["291_5G_-_-_20/40/80 MHz_CH153_TV Wifi_Off/On_", "5G_Auto_CH153_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["292_5G_-_-_20/40/80 MHz_CH153_DC_Off/On_", "5G_Auto_CH153_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["293_5G_-_-_20/40/80 MHz_CH153_AC_Off/On_", "5G_Auto_CH153_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["294_5G_-_-_20/40/80 MHz_CH153_AP_Off/On_", "5G_Auto_CH153_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["295_5G_-_-_20/40/80 MHz_CH153_IP_ConnectionTest_", "5G_Auto_CH153_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["296_5G_-_-_20/40/80 MHz_CH157_TV Wifi_Off/On_", "5G_Auto_CH157_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["297_5G_-_-_20/40/80 MHz_CH157_DC_Off/On_", "5G_Auto_CH157_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["298_5G_-_-_20/40/80 MHz_CH157_AC_Off/On_", "5G_Auto_CH157_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["299_5G_-_-_20/40/80 MHz_CH157_AP_Off/On_", "5G_Auto_CH157_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["300_5G_-_-_20/40/80 MHz_CH157_IP_ConnectionTest_", "5G_Auto_CH157_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["301_5G_-_-_20/40/80 MHz_CH161_TV Wifi_Off/On_", "5G_Auto_CH161_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["302_5G_-_-_20/40/80 MHz_CH161_DC_Off/On_", "5G_Auto_CH161_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["303_5G_-_-_20/40/80 MHz_CH161_AC_Off/On_", "5G_Auto_CH161_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["304_5G_-_-_20/40/80 MHz_CH161_AP_Off/On_", "5G_Auto_CH161_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["305_5G_-_-_20/40/80 MHz_CH161_IP_ConnectionTest_", "5G_Auto_CH161_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["306_5G_-_-_20/40/80 MHz_CH165_TV Wifi_Off/On_", "5G_Auto_CH165_WifiTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH165, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["307_5G_-_-_20/40/80 MHz_CH165_DC_Off/On_", "5G_Auto_CH165_DCTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH165, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["308_5G_-_-_20/40/80 MHz_CH165_AC_Off/On_", "5G_Auto_CH165_ACTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH165, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["309_5G_-_-_20/40/80 MHz_CH165_AP_Off/On_", "5G_Auto_CH165_APTriggerOnOff", 
     AP_5G, AP_5Gmedium, AP_5GCH165, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["310_5G_-_-_20/40/80 MHz_CH165_IP_ConnectionTest_", "5G_Auto_CH165_ConnectionTest", 
     AP_5G, AP_5Gmedium, AP_5GCH165, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["311_5G_-_-_20 MHz_Auto_TV Wifi_Off/On_", "5G_20MHz_5G-Auto_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["312_5G_-_-_20 MHz_Auto_DC_Off/On_", "5G_20MHz_5G-Auto_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["313_5G_-_-_20 MHz_Auto_AC_Off/On_", "5G_20MHz_5G-Auto_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["314_5G_-_-_20 MHz_Auto_AP_Off/On_", "5G_20MHz_5G-Auto_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["315_5G_-_-_20 MHz_Auto_IP_ConnectionTest_", "5G_20MHz_5G-Auto_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["316_5G_-_-_20 MHz_CH36_TV Wifi_Off/On_", "5G_20MHz_CH36_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["317_5G_-_-_20 MHz_CH36_DC_Off/On_", "5G_20MHz_CH36_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["318_5G_-_-_20 MHz_CH36_AC_Off/On_", "5G_20MHz_CH36_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["319_5G_-_-_20 MHz_CH36_AP_Off/On_", "5G_20MHz_CH36_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["320_5G_-_-_20 MHz_CH36_IP_ConnectionTest_", "5G_20MHz_CH36_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["321_5G_-_-_20 MHz_CH40_TV Wifi_Off/On_", "5G_20MHz_CH40_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["322_5G_-_-_20 MHz_CH40_DC_Off/On_", "5G_20MHz_CH40_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["323_5G_-_-_20 MHz_CH40_AC_Off/On_", "5G_20MHz_CH40_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["324_5G_-_-_20 MHz_CH40_AP_Off/On_", "5G_20MHz_CH40_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["325_5G_-_-_20 MHz_CH40_IP_ConnectionTest_", "5G_20MHz_CH40_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["326_5G_-_-_20 MHz_CH44_TV Wifi_Off/On_", "5G_20MHz_CH44_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["327_5G_-_-_20 MHz_CH44_DC_Off/On_", "5G_20MHz_CH44_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["328_5G_-_-_20 MHz_CH44_AC_Off/On_", "5G_20MHz_CH44_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["329_5G_-_-_20 MHz_CH44_AP_Off/On_", "5G_20MHz_CH44_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["330_5G_-_-_20 MHz_CH44_IP_ConnectionTest_", "5G_20MHz_CH44_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["331_5G_-_-_20 MHz_CH48_TV Wifi_Off/On_", "5G_20MHz_CH48_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["332_5G_-_-_20 MHz_CH48_DC_Off/On_", "5G_20MHz_CH48_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["333_5G_-_-_20 MHz_CH48_AC_Off/On_", "5G_20MHz_CH48_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["334_5G_-_-_20 MHz_CH48_AP_Off/On_", "5G_20MHz_CH48_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["335_5G_-_-_20 MHz_CH48_IP_ConnectionTest_", "5G_20MHz_CH48_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["336_5G_-_-_20 MHz_CH52_TV Wifi_Off/On_", "5G_20MHz_CH52_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH52, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["337_5G_-_-_20 MHz_CH52_DC_Off/On_", "5G_20MHz_CH52_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH52, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["338_5G_-_-_20 MHz_CH52_AC_Off/On_", "5G_20MHz_CH52_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH52, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["339_5G_-_-_20 MHz_CH52_AP_Off/On_", "5G_20MHz_CH52_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH52, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["340_5G_-_-_20 MHz_CH52_IP_ConnectionTest_", "5G_20MHz_CH52_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH52, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["341_5G_-_-_20 MHz_CH56_TV Wifi_Off/On_", "5G_20MHz_CH56_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH56, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["342_5G_-_-_20 MHz_CH56_DC_Off/On_", "5G_20MHz_CH56_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH56, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["343_5G_-_-_20 MHz_CH56_AC_Off/On_", "5G_20MHz_CH56_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH56, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["344_5G_-_-_20 MHz_CH56_AP_Off/On_", "5G_20MHz_CH56_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH56, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["345_5G_-_-_20 MHz_CH56_IP_ConnectionTest_", "5G_20MHz_CH56_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH56, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["346_5G_-_-_20 MHz_CH60_TV Wifi_Off/On_", "5G_20MHz_CH60_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH60, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["347_5G_-_-_20 MHz_CH60_DC_Off/On_", "5G_20MHz_CH60_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH60, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["348_5G_-_-_20 MHz_CH60_AC_Off/On_", "5G_20MHz_CH60_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH60, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["349_5G_-_-_20 MHz_CH60_AP_Off/On_", "5G_20MHz_CH60_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH60, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["350_5G_-_-_20 MHz_CH60_IP_ConnectionTest_", "5G_20MHz_CH60_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH60, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["351_5G_-_-_20 MHz_CH64_TV Wifi_Off/On_", "5G_20MHz_CH64_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH64, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["352_5G_-_-_20 MHz_CH64_DC_Off/On_", "5G_20MHz_CH64_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH64, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["353_5G_-_-_20 MHz_CH64_AC_Off/On_", "5G_20MHz_CH64_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH64, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["354_5G_-_-_20 MHz_CH64_AP_Off/On_", "5G_20MHz_CH64_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH64, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["355_5G_-_-_20 MHz_CH64_IP_ConnectionTest_", "5G_20MHz_CH64_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH64, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["356_5G_-_-_20 MHz_CH100_TV Wifi_Off/On_", "5G_20MHz_CH100_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH100, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["357_5G_-_-_20 MHz_CH100_DC_Off/On_", "5G_20MHz_CH100_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH100, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["358_5G_-_-_20 MHz_CH100_AC_Off/On_", "5G_20MHz_CH100_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH100, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["359_5G_-_-_20 MHz_CH100_AP_Off/On_", "5G_20MHz_CH100_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH100, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["360_5G_-_-_20 MHz_CH100_IP_ConnectionTest_", "5G_20MHz_CH100_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH100, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["361_5G_-_-_20 MHz_CH104_TV Wifi_Off/On_", "5G_20MHz_CH104_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH104, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["362_5G_-_-_20 MHz_CH104_DC_Off/On_", "5G_20MHz_CH104_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH104, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["363_5G_-_-_20 MHz_CH104_AC_Off/On_", "5G_20MHz_CH104_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH104, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["364_5G_-_-_20 MHz_CH104_AP_Off/On_", "5G_20MHz_CH104_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH104, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["365_5G_-_-_20 MHz_CH104_IP_ConnectionTest_", "5G_20MHz_CH104_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH104, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["366_5G_-_-_20 MHz_CH108_TV Wifi_Off/On_", "5G_20MHz_CH108_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH108, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["367_5G_-_-_20 MHz_CH108_DC_Off/On_", "5G_20MHz_CH108_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH108, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["368_5G_-_-_20 MHz_CH108_AC_Off/On_", "5G_20MHz_CH108_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH108, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["369_5G_-_-_20 MHz_CH108_AP_Off/On_", "5G_20MHz_CH108_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH108, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["370_5G_-_-_20 MHz_CH108_IP_ConnectionTest_", "5G_20MHz_CH108_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH108, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["371_5G_-_-_20 MHz_CH112_TV Wifi_Off/On_", "5G_20MHz_CH112_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH112, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["372_5G_-_-_20 MHz_CH112_DC_Off/On_", "5G_20MHz_CH112_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH112, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["373_5G_-_-_20 MHz_CH112_AC_Off/On_", "5G_20MHz_CH112_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH112, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["374_5G_-_-_20 MHz_CH112_AP_Off/On_", "5G_20MHz_CH112_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH112, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["375_5G_-_-_20 MHz_CH112_IP_ConnectionTest_", "5G_20MHz_CH112_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH112, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["376_5G_-_-_20 MHz_CH116_TV Wifi_Off/On_", "5G_20MHz_CH116_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH116, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["377_5G_-_-_20 MHz_CH116_DC_Off/On_", "5G_20MHz_CH116_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH116, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["378_5G_-_-_20 MHz_CH116_AC_Off/On_", "5G_20MHz_CH116_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH116, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["379_5G_-_-_20 MHz_CH116_AP_Off/On_", "5G_20MHz_CH116_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH116, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["380_5G_-_-_20 MHz_CH116_IP_ConnectionTest_", "5G_20MHz_CH116_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH116, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["381_5G_-_-_20 MHz_CH120_TV Wifi_Off/On_", "5G_20MHz_CH120_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH120, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["382_5G_-_-_20 MHz_CH120_DC_Off/On_", "5G_20MHz_CH120_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH120, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["383_5G_-_-_20 MHz_CH120_AC_Off/On_", "5G_20MHz_CH120_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH120, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["384_5G_-_-_20 MHz_CH120_AP_Off/On_", "5G_20MHz_CH120_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH120, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["385_5G_-_-_20 MHz_CH120_IP_ConnectionTest_", "5G_20MHz_CH120_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH120, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["386_5G_-_-_20 MHz_CH124_TV Wifi_Off/On_", "5G_20MHz_CH124_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH124, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["387_5G_-_-_20 MHz_CH124_DC_Off/On_", "5G_20MHz_CH124_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH124, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["388_5G_-_-_20 MHz_CH124_AC_Off/On_", "5G_20MHz_CH124_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH124, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["389_5G_-_-_20 MHz_CH124_AP_Off/On_", "5G_20MHz_CH124_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH124, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["390_5G_-_-_20 MHz_CH124_IP_ConnectionTest_", "5G_20MHz_CH124_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH124, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["391_5G_-_-_20 MHz_CH128_TV Wifi_Off/On_", "5G_20MHz_CH128_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH128, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["392_5G_-_-_20 MHz_CH128_DC_Off/On_", "5G_20MHz_CH128_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH128, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["393_5G_-_-_20 MHz_CH128_AC_Off/On_", "5G_20MHz_CH128_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH128, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["394_5G_-_-_20 MHz_CH128_AP_Off/On_", "5G_20MHz_CH128_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH128, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["395_5G_-_-_20 MHz_CH128_IP_ConnectionTest_", "5G_20MHz_CH128_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH128, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["396_5G_-_-_20 MHz_CH132_TV Wifi_Off/On_", "5G_20MHz_CH132_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH132, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["397_5G_-_-_20 MHz_CH132_DC_Off/On_", "5G_20MHz_CH132_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH132, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["398_5G_-_-_20 MHz_CH132_AC_Off/On_", "5G_20MHz_CH132_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH132, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["399_5G_-_-_20 MHz_CH132_AP_Off/On_", "5G_20MHz_CH132_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH132, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["400_5G_-_-_20 MHz_CH132_IP_ConnectionTest_", "5G_20MHz_CH132_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH132, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["401_5G_-_-_20 MHz_CH136_TV Wifi_Off/On_", "5G_20MHz_CH136_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH136, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["402_5G_-_-_20 MHz_CH136_DC_Off/On_", "5G_20MHz_CH136_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH136, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["403_5G_-_-_20 MHz_CH136_AC_Off/On_", "5G_20MHz_CH136_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH136, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["404_5G_-_-_20 MHz_CH136_AP_Off/On_", "5G_20MHz_CH136_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH136, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["405_5G_-_-_20 MHz_CH136_IP_ConnectionTest_", "5G_20MHz_CH136_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH136, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["406_5G_-_-_20 MHz_CH140_TV Wifi_Off/On_", "5G_20MHz_CH140_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH140, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["407_5G_-_-_20 MHz_CH140_DC_Off/On_", "5G_20MHz_CH140_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH140, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["408_5G_-_-_20 MHz_CH140_AC_Off/On_", "5G_20MHz_CH140_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH140, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["409_5G_-_-_20 MHz_CH140_AP_Off/On_", "5G_20MHz_CH140_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH140, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["410_5G_-_-_20 MHz_CH140_IP_ConnectionTest_", "5G_20MHz_CH140_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH140, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["411_5G_-_-_20 MHz_CH144_TV Wifi_Off/On_", "5G_20MHz_CH144_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH144, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["412_5G_-_-_20 MHz_CH144_DC_Off/On_", "5G_20MHz_CH144_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH144, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["413_5G_-_-_20 MHz_CH144_AC_Off/On_", "5G_20MHz_CH144_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH144, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["414_5G_-_-_20 MHz_CH144_AP_Off/On_", "5G_20MHz_CH144_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH144, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["415_5G_-_-_20 MHz_CH144_IP_ConnectionTest_", "5G_20MHz_CH144_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH144, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["416_5G_-_-_20 MHz_CH149_TV Wifi_Off/On_", "5G_20MHz_CH149_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["417_5G_-_-_20 MHz_CH149_DC_Off/On_", "5G_20MHz_CH149_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["418_5G_-_-_20 MHz_CH149_AC_Off/On_", "5G_20MHz_CH149_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["419_5G_-_-_20 MHz_CH149_AP_Off/On_", "5G_20MHz_CH149_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["420_5G_-_-_20 MHz_CH149_IP_ConnectionTest_", "5G_20MHz_CH149_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["421_5G_-_-_20 MHz_CH153_TV Wifi_Off/On_", "5G_20MHz_CH153_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["422_5G_-_-_20 MHz_CH153_DC_Off/On_", "5G_20MHz_CH153_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["423_5G_-_-_20 MHz_CH153_AC_Off/On_", "5G_20MHz_CH153_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["424_5G_-_-_20 MHz_CH153_AP_Off/On_", "5G_20MHz_CH153_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["425_5G_-_-_20 MHz_CH153_IP_ConnectionTest_", "5G_20MHz_CH153_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["426_5G_-_-_20 MHz_CH157_TV Wifi_Off/On_", "5G_20MHz_CH157_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["427_5G_-_-_20 MHz_CH157_DC_Off/On_", "5G_20MHz_CH157_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["428_5G_-_-_20 MHz_CH157_AC_Off/On_", "5G_20MHz_CH157_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["429_5G_-_-_20 MHz_CH157_AP_Off/On_", "5G_20MHz_CH157_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["430_5G_-_-_20 MHz_CH157_IP_ConnectionTest_", "5G_20MHz_CH157_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["431_5G_-_-_20 MHz_CH161_TV Wifi_Off/On_", "5G_20MHz_CH161_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["432_5G_-_-_20 MHz_CH161_DC_Off/On_", "5G_20MHz_CH161_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["433_5G_-_-_20 MHz_CH161_AC_Off/On_", "5G_20MHz_CH161_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["434_5G_-_-_20 MHz_CH161_AP_Off/On_", "5G_20MHz_CH161_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["435_5G_-_-_20 MHz_CH161_IP_ConnectionTest_", "5G_20MHz_CH161_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["436_5G_-_-_20 MHz_CH165_TV Wifi_Off/On_", "5G_20MHz_CH165_WifiTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH165, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["437_5G_-_-_20 MHz_CH165_DC_Off/On_", "5G_20MHz_CH165_DCTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH165, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["438_5G_-_-_20 MHz_CH165_AC_Off/On_", "5G_20MHz_CH165_ACTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH165, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["439_5G_-_-_20 MHz_CH165_AP_Off/On_", "5G_20MHz_CH165_APTriggerOnOff", 
     AP_5G, AP_5Glow, AP_5GCH165, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["440_5G_-_-_20 MHz_CH165_IP_ConnectionTest_", "5G_20MHz_CH165_ConnectionTest", 
     AP_5G, AP_5Glow, AP_5GCH165, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["441_5G_-_-_40 MHz_Auto_TV Wifi_Off/On_", "5G_40MHz_5G-Auto_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["442_5G_-_-_40 MHz_Auto_DC_Off/On_", "5G_40MHz_5G-Auto_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["443_5G_-_-_40 MHz_Auto_AC_Off/On_", "5G_40MHz_5G-Auto_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["444_5G_-_-_40 MHz_Auto_AP_Off/On_", "5G_40MHz_5G-Auto_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["445_5G_-_-_40 MHz_Auto_IP_ConnectionTest_", "5G_40MHz_5G-Auto_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["446_5G_-_-_40 MHz_CH36_TV Wifi_Off/On_", "5G_40MHz_CH36_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["447_5G_-_-_40 MHz_CH36_DC_Off/On_", "5G_40MHz_CH36_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["448_5G_-_-_40 MHz_CH36_AC_Off/On_", "5G_40MHz_CH36_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["449_5G_-_-_40 MHz_CH36_AP_Off/On_", "5G_40MHz_CH36_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["450_5G_-_-_40 MHz_CH36_IP_ConnectionTest_", "5G_40MHz_CH36_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["451_5G_-_-_40 MHz_CH40_TV Wifi_Off/On_", "5G_40MHz_CH40_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["452_5G_-_-_40 MHz_CH40_DC_Off/On_", "5G_40MHz_CH40_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["453_5G_-_-_40 MHz_CH40_AC_Off/On_", "5G_40MHz_CH40_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["454_5G_-_-_40 MHz_CH40_AP_Off/On_", "5G_40MHz_CH40_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["455_5G_-_-_40 MHz_CH40_IP_ConnectionTest_", "5G_40MHz_CH40_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["456_5G_-_-_40 MHz_CH44_TV Wifi_Off/On_", "5G_40MHz_CH44_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["457_5G_-_-_40 MHz_CH44_DC_Off/On_", "5G_40MHz_CH44_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["458_5G_-_-_40 MHz_CH44_AC_Off/On_", "5G_40MHz_CH44_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["459_5G_-_-_40 MHz_CH44_AP_Off/On_", "5G_40MHz_CH44_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["460_5G_-_-_40 MHz_CH44_IP_ConnectionTest_", "5G_40MHz_CH44_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["461_5G_-_-_40 MHz_CH48_TV Wifi_Off/On_", "5G_40MHz_CH48_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["462_5G_-_-_40 MHz_CH48_DC_Off/On_", "5G_40MHz_CH48_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["463_5G_-_-_40 MHz_CH48_AC_Off/On_", "5G_40MHz_CH48_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["464_5G_-_-_40 MHz_CH48_AP_Off/On_", "5G_40MHz_CH48_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["465_5G_-_-_40 MHz_CH48_IP_ConnectionTest_", "5G_40MHz_CH48_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["466_5G_-_-_40 MHz_CH52_TV Wifi_Off/On_", "5G_40MHz_CH52_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH52, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["467_5G_-_-_40 MHz_CH52_DC_Off/On_", "5G_40MHz_CH52_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH52, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["468_5G_-_-_40 MHz_CH52_AC_Off/On_", "5G_40MHz_CH52_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH52, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["469_5G_-_-_40 MHz_CH52_AP_Off/On_", "5G_40MHz_CH52_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH52, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["470_5G_-_-_40 MHz_CH52_IP_ConnectionTest_", "5G_40MHz_CH52_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH52, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["471_5G_-_-_40 MHz_CH56_TV Wifi_Off/On_", "5G_40MHz_CH56_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH56, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["472_5G_-_-_40 MHz_CH56_DC_Off/On_", "5G_40MHz_CH56_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH56, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["473_5G_-_-_40 MHz_CH56_AC_Off/On_", "5G_40MHz_CH56_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH56, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["474_5G_-_-_40 MHz_CH56_AP_Off/On_", "5G_40MHz_CH56_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH56, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["475_5G_-_-_40 MHz_CH56_IP_ConnectionTest_", "5G_40MHz_CH56_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH56, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["476_5G_-_-_40 MHz_CH60_TV Wifi_Off/On_", "5G_40MHz_CH60_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH60, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["477_5G_-_-_40 MHz_CH60_DC_Off/On_", "5G_40MHz_CH60_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH60, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["478_5G_-_-_40 MHz_CH60_AC_Off/On_", "5G_40MHz_CH60_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH60, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["479_5G_-_-_40 MHz_CH60_AP_Off/On_", "5G_40MHz_CH60_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH60, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["480_5G_-_-_40 MHz_CH60_IP_ConnectionTest_", "5G_40MHz_CH60_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH60, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["481_5G_-_-_40 MHz_CH64_TV Wifi_Off/On_", "5G_40MHz_CH64_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH64, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["482_5G_-_-_40 MHz_CH64_DC_Off/On_", "5G_40MHz_CH64_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH64, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["483_5G_-_-_40 MHz_CH64_AC_Off/On_", "5G_40MHz_CH64_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH64, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["484_5G_-_-_40 MHz_CH64_AP_Off/On_", "5G_40MHz_CH64_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH64, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["485_5G_-_-_40 MHz_CH64_IP_ConnectionTest_", "5G_40MHz_CH64_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH64, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["486_5G_-_-_40 MHz_CH100_TV Wifi_Off/On_", "5G_40MHz_CH100_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH100, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["487_5G_-_-_40 MHz_CH100_DC_Off/On_", "5G_40MHz_CH100_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH100, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["488_5G_-_-_40 MHz_CH100_AC_Off/On_", "5G_40MHz_CH100_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH100, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["489_5G_-_-_40 MHz_CH100_AP_Off/On_", "5G_40MHz_CH100_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH100, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["490_5G_-_-_40 MHz_CH100_IP_ConnectionTest_", "5G_40MHz_CH100_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH100, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["491_5G_-_-_40 MHz_CH104_TV Wifi_Off/On_", "5G_40MHz_CH104_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH104, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["492_5G_-_-_40 MHz_CH104_DC_Off/On_", "5G_40MHz_CH104_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH104, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["493_5G_-_-_40 MHz_CH104_AC_Off/On_", "5G_40MHz_CH104_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH104, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["494_5G_-_-_40 MHz_CH104_AP_Off/On_", "5G_40MHz_CH104_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH104, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["495_5G_-_-_40 MHz_CH104_IP_ConnectionTest_", "5G_40MHz_CH104_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH104, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["496_5G_-_-_40 MHz_CH108_TV Wifi_Off/On_", "5G_40MHz_CH108_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH108, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["497_5G_-_-_40 MHz_CH108_DC_Off/On_", "5G_40MHz_CH108_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH108, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["498_5G_-_-_40 MHz_CH108_AC_Off/On_", "5G_40MHz_CH108_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH108, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["499_5G_-_-_40 MHz_CH108_AP_Off/On_", "5G_40MHz_CH108_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH108, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
     ["500_5G_-_-_40 MHz_CH108_IP_ConnectionTest_", "5G_40MHz_CH108_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH108, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["501_5G_-_-_40 MHz_CH112_TV Wifi_Off/On_", "5G_40MHz_CH112_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH112, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["502_5G_-_-_40 MHz_CH112_DC_Off/On_", "5G_40MHz_CH112_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH112, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["503_5G_-_-_40 MHz_CH112_AC_Off/On_", "5G_40MHz_CH112_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH112, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["504_5G_-_-_40 MHz_CH112_AP_Off/On_", "5G_40MHz_CH112_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH112, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["505_5G_-_-_40 MHz_CH112_IP_ConnectionTest_", "5G_40MHz_CH112_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH112, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["506_5G_-_-_40 MHz_CH116_TV Wifi_Off/On_", "5G_40MHz_CH116_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH116, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["507_5G_-_-_40 MHz_CH116_DC_Off/On_", "5G_40MHz_CH116_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH116, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["508_5G_-_-_40 MHz_CH116_AC_Off/On_", "5G_40MHz_CH116_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH116, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["509_5G_-_-_40 MHz_CH116_AP_Off/On_", "5G_40MHz_CH116_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH116, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["510_5G_-_-_40 MHz_CH116_IP_ConnectionTest_", "5G_40MHz_CH116_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH116, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["511_5G_-_-_40 MHz_CH120_TV Wifi_Off/On_", "5G_40MHz_CH120_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH120, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["512_5G_-_-_40 MHz_CH120_DC_Off/On_", "5G_40MHz_CH120_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH120, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["513_5G_-_-_40 MHz_CH120_AC_Off/On_", "5G_40MHz_CH120_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH120, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["514_5G_-_-_40 MHz_CH120_AP_Off/On_", "5G_40MHz_CH120_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH120, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["515_5G_-_-_40 MHz_CH120_IP_ConnectionTest_", "5G_40MHz_CH120_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH120, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["516_5G_-_-_40 MHz_CH124_TV Wifi_Off/On_", "5G_40MHz_CH124_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH124, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["517_5G_-_-_40 MHz_CH124_DC_Off/On_", "5G_40MHz_CH124_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH124, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["518_5G_-_-_40 MHz_CH124_AC_Off/On_", "5G_40MHz_CH124_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH124, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["519_5G_-_-_40 MHz_CH124_AP_Off/On_", "5G_40MHz_CH124_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH124, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["520_5G_-_-_40 MHz_CH124_IP_ConnectionTest_", "5G_40MHz_CH124_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH124, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["521_5G_-_-_40 MHz_CH128_TV Wifi_Off/On_", "5G_40MHz_CH128_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH128, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["522_5G_-_-_40 MHz_CH128_DC_Off/On_", "5G_40MHz_CH128_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH128, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["523_5G_-_-_40 MHz_CH128_AC_Off/On_", "5G_40MHz_CH128_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH128, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["524_5G_-_-_40 MHz_CH128_AP_Off/On_", "5G_40MHz_CH128_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH128, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["525_5G_-_-_40 MHz_CH128_IP_ConnectionTest_", "5G_40MHz_CH128_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH128, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["526_5G_-_-_40 MHz_CH132_TV Wifi_Off/On_", "5G_40MHz_CH132_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH132, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["527_5G_-_-_40 MHz_CH132_DC_Off/On_", "5G_40MHz_CH132_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH132, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["528_5G_-_-_40 MHz_CH132_AC_Off/On_", "5G_40MHz_CH132_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH132, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["529_5G_-_-_40 MHz_CH132_AP_Off/On_", "5G_40MHz_CH132_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH132, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["530_5G_-_-_40 MHz_CH132_IP_ConnectionTest_", "5G_40MHz_CH132_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH132, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["531_5G_-_-_40 MHz_CH136_TV Wifi_Off/On_", "5G_40MHz_CH136_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH136, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["532_5G_-_-_40 MHz_CH136_DC_Off/On_", "5G_40MHz_CH136_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH136, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["533_5G_-_-_40 MHz_CH136_AC_Off/On_", "5G_40MHz_CH136_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH136, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["534_5G_-_-_40 MHz_CH136_AP_Off/On_", "5G_40MHz_CH136_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH136, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["535_5G_-_-_40 MHz_CH136_IP_ConnectionTest_", "5G_40MHz_CH136_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH136, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["536_5G_-_-_40 MHz_CH140_TV Wifi_Off/On_", "5G_40MHz_CH140_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH140, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["537_5G_-_-_40 MHz_CH140_DC_Off/On_", "5G_40MHz_CH140_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH140, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["538_5G_-_-_40 MHz_CH140_AC_Off/On_", "5G_40MHz_CH140_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH140, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["539_5G_-_-_40 MHz_CH140_AP_Off/On_", "5G_40MHz_CH140_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH140, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["540_5G_-_-_40 MHz_CH140_IP_ConnectionTest_", "5G_40MHz_CH140_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH140, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["541_5G_-_-_40 MHz_CH144_TV Wifi_Off/On_", "5G_40MHz_CH144_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH144, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["542_5G_-_-_40 MHz_CH144_DC_Off/On_", "5G_40MHz_CH144_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH144, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["543_5G_-_-_40 MHz_CH144_AC_Off/On_", "5G_40MHz_CH144_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH144, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["544_5G_-_-_40 MHz_CH144_AP_Off/On_", "5G_40MHz_CH144_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH144, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["545_5G_-_-_40 MHz_CH144_IP_ConnectionTest_", "5G_40MHz_CH144_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH144, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["546_5G_-_-_40 MHz_CH149_TV Wifi_Off/On_", "5G_40MHz_CH149_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["547_5G_-_-_40 MHz_CH149_DC_Off/On_", "5G_40MHz_CH149_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["548_5G_-_-_40 MHz_CH149_AC_Off/On_", "5G_40MHz_CH149_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["549_5G_-_-_40 MHz_CH149_AP_Off/On_", "5G_40MHz_CH149_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["550_5G_-_-_40 MHz_CH149_IP_ConnectionTest_", "5G_40MHz_CH149_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["551_5G_-_-_40 MHz_CH153_TV Wifi_Off/On_", "5G_40MHz_CH153_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["552_5G_-_-_40 MHz_CH153_DC_Off/On_", "5G_40MHz_CH153_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["553_5G_-_-_40 MHz_CH153_AC_Off/On_", "5G_40MHz_CH153_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["554_5G_-_-_40 MHz_CH153_AP_Off/On_", "5G_40MHz_CH153_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["555_5G_-_-_40 MHz_CH153_IP_ConnectionTest_", "5G_40MHz_CH153_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["556_5G_-_-_40 MHz_CH157_TV Wifi_Off/On_", "5G_40MHz_CH157_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["557_5G_-_-_40 MHz_CH157_DC_Off/On_", "5G_40MHz_CH157_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["558_5G_-_-_40 MHz_CH157_AC_Off/On_", "5G_40MHz_CH157_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["559_5G_-_-_40 MHz_CH157_AP_Off/On_", "5G_40MHz_CH157_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["560_5G_-_-_40 MHz_CH157_IP_ConnectionTest_", "5G_40MHz_CH157_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["561_5G_-_-_40 MHz_CH161_TV Wifi_Off/On_", "5G_40MHz_CH161_WifiTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["562_5G_-_-_40 MHz_CH161_DC_Off/On_", "5G_40MHz_CH161_DCTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["563_5G_-_-_40 MHz_CH161_AC_Off/On_", "5G_40MHz_CH161_ACTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["564_5G_-_-_40 MHz_CH161_AP_Off/On_", "5G_40MHz_CH161_APTriggerOnOff", 
     AP_5G, AP_5Ghigh, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["565_5G_-_-_40 MHz_CH161_IP_ConnectionTest_", "5G_40MHz_CH161_ConnectionTest", 
     AP_5G, AP_5Ghigh, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["566_5G_-_-_80 MHz_Auto_TV Wifi_Off/On_", "5G_80MHz_5G-Auto_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GAuto, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["567_5G_-_-_80 MHz_Auto_DC_Off/On_", "5G_80MHz_5G-Auto_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GAuto, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["568_5G_-_-_80 MHz_Auto_AC_Off/On_", "5G_80MHz_5G-Auto_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GAuto, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["569_5G_-_-_80 MHz_Auto_AP_Off/On_", "5G_80MHz_5G-Auto_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GAuto, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["570_5G_-_-_80 MHz_Auto_IP_ConnectionTest_", "5G_80MHz_5G-Auto_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GAuto, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["571_5G_-_-_80 MHz_CH36_TV Wifi_Off/On_", "5G_80MHz_CH36_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH36, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["572_5G_-_-_80 MHz_CH36_DC_Off/On_", "5G_80MHz_CH36_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH36, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["573_5G_-_-_80 MHz_CH36_AC_Off/On_", "5G_80MHz_CH36_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH36, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["574_5G_-_-_80 MHz_CH36_AP_Off/On_", "5G_80MHz_CH36_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH36, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["575_5G_-_-_80 MHz_CH36_IP_ConnectionTest_", "5G_80MHz_CH36_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH36, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["576_5G_-_-_80 MHz_CH40_TV Wifi_Off/On_", "5G_80MHz_CH40_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH40, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["577_5G_-_-_80 MHz_CH40_DC_Off/On_", "5G_80MHz_CH40_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH40, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["578_5G_-_-_80 MHz_CH40_AC_Off/On_", "5G_80MHz_CH40_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH40, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["579_5G_-_-_80 MHz_CH40_AP_Off/On_", "5G_80MHz_CH40_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH40, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["580_5G_-_-_80 MHz_CH40_IP_ConnectionTest_", "5G_80MHz_CH40_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH40, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["581_5G_-_-_80 MHz_CH44_TV Wifi_Off/On_", "5G_80MHz_CH44_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH44, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["582_5G_-_-_80 MHz_CH44_DC_Off/On_", "5G_80MHz_CH44_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH44, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["583_5G_-_-_80 MHz_CH44_AC_Off/On_", "5G_80MHz_CH44_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH44, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["584_5G_-_-_80 MHz_CH44_AP_Off/On_", "5G_80MHz_CH44_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH44, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["585_5G_-_-_80 MHz_CH44_IP_ConnectionTest_", "5G_80MHz_CH44_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH44, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["586_5G_-_-_80 MHz_CH48_TV Wifi_Off/On_", "5G_80MHz_CH48_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH48, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["587_5G_-_-_80 MHz_CH48_DC_Off/On_", "5G_80MHz_CH48_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH48, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["588_5G_-_-_80 MHz_CH48_AC_Off/On_", "5G_80MHz_CH48_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH48, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["589_5G_-_-_80 MHz_CH48_AP_Off/On_", "5G_80MHz_CH48_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH48, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["590_5G_-_-_80 MHz_CH48_IP_ConnectionTest_", "5G_80MHz_CH48_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH48, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["591_5G_-_-_80 MHz_CH52_TV Wifi_Off/On_", "5G_80MHz_CH52_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH52, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["592_5G_-_-_80 MHz_CH52_DC_Off/On_", "5G_80MHz_CH52_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH52, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["593_5G_-_-_80 MHz_CH52_AC_Off/On_", "5G_80MHz_CH52_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH52, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["594_5G_-_-_80 MHz_CH52_AP_Off/On_", "5G_80MHz_CH52_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH52, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["595_5G_-_-_80 MHz_CH52_IP_ConnectionTest_", "5G_80MHz_CH52_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH52, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["596_5G_-_-_80 MHz_CH56_TV Wifi_Off/On_", "5G_80MHz_CH56_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH56, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["597_5G_-_-_80 MHz_CH56_DC_Off/On_", "5G_80MHz_CH56_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH56, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["598_5G_-_-_80 MHz_CH56_AC_Off/On_", "5G_80MHz_CH56_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH56, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["599_5G_-_-_80 MHz_CH56_AP_Off/On_", "5G_80MHz_CH56_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH56, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["600_5G_-_-_80 MHz_CH56_IP_ConnectionTest_", "5G_80MHz_CH56_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH56, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["601_5G_-_-_80 MHz_CH60_TV Wifi_Off/On_", "5G_80MHz_CH60_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH60, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["602_5G_-_-_80 MHz_CH60_DC_Off/On_", "5G_80MHz_CH60_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH60, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["603_5G_-_-_80 MHz_CH60_AC_Off/On_", "5G_80MHz_CH60_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH60, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["604_5G_-_-_80 MHz_CH60_AP_Off/On_", "5G_80MHz_CH60_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH60, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["605_5G_-_-_80 MHz_CH60_IP_ConnectionTest_", "5G_80MHz_CH60_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH60, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["606_5G_-_-_80 MHz_CH64_TV Wifi_Off/On_", "5G_80MHz_CH64_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH64, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["607_5G_-_-_80 MHz_CH64_DC_Off/On_", "5G_80MHz_CH64_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH64, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["608_5G_-_-_80 MHz_CH64_AC_Off/On_", "5G_80MHz_CH64_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH64, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["609_5G_-_-_80 MHz_CH64_AP_Off/On_", "5G_80MHz_CH64_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH64, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["610_5G_-_-_80 MHz_CH64_IP_ConnectionTest_", "5G_80MHz_CH64_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH64, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["611_5G_-_-_80 MHz_CH100_TV Wifi_Off/On_", "5G_80MHz_CH100_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH100, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["612_5G_-_-_80 MHz_CH100_DC_Off/On_", "5G_80MHz_CH100_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH100, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["613_5G_-_-_80 MHz_CH100_AC_Off/On_", "5G_80MHz_CH100_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH100, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["614_5G_-_-_80 MHz_CH100_AP_Off/On_", "5G_80MHz_CH100_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH100, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["615_5G_-_-_80 MHz_CH100_IP_ConnectionTest_", "5G_80MHz_CH100_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH100, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["616_5G_-_-_80 MHz_CH104_TV Wifi_Off/On_", "5G_80MHz_CH104_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH104, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["617_5G_-_-_80 MHz_CH104_DC_Off/On_", "5G_80MHz_CH104_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH104, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["618_5G_-_-_80 MHz_CH104_AC_Off/On_", "5G_80MHz_CH104_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH104, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["619_5G_-_-_80 MHz_CH104_AP_Off/On_", "5G_80MHz_CH104_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH104, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["620_5G_-_-_80 MHz_CH104_IP_ConnectionTest_", "5G_80MHz_CH104_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH104, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["621_5G_-_-_80 MHz_CH108_TV Wifi_Off/On_", "5G_80MHz_CH108_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH108, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["622_5G_-_-_80 MHz_CH108_DC_Off/On_", "5G_80MHz_CH108_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH108, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["623_5G_-_-_80 MHz_CH108_AC_Off/On_", "5G_80MHz_CH108_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH108, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["624_5G_-_-_80 MHz_CH108_AP_Off/On_", "5G_80MHz_CH108_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH108, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["625_5G_-_-_80 MHz_CH108_IP_ConnectionTest_", "5G_80MHz_CH108_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH108, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["626_5G_-_-_80 MHz_CH112_TV Wifi_Off/On_", "5G_80MHz_CH112_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH112, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["627_5G_-_-_80 MHz_CH112_DC_Off/On_", "5G_80MHz_CH112_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH112, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["628_5G_-_-_80 MHz_CH112_AC_Off/On_", "5G_80MHz_CH112_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH112, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["629_5G_-_-_80 MHz_CH112_AP_Off/On_", "5G_80MHz_CH112_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH112, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["630_5G_-_-_80 MHz_CH112_IP_ConnectionTest_", "5G_80MHz_CH112_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH112, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["631_5G_-_-_80 MHz_CH116_TV Wifi_Off/On_", "5G_80MHz_CH116_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH116, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["632_5G_-_-_80 MHz_CH116_DC_Off/On_", "5G_80MHz_CH116_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH116, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["633_5G_-_-_80 MHz_CH116_AC_Off/On_", "5G_80MHz_CH116_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH116, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["634_5G_-_-_80 MHz_CH116_AP_Off/On_", "5G_80MHz_CH116_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH116, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["635_5G_-_-_80 MHz_CH116_IP_ConnectionTest_", "5G_80MHz_CH116_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH116, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["636_5G_-_-_80 MHz_CH120_TV Wifi_Off/On_", "5G_80MHz_CH120_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH120, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["637_5G_-_-_80 MHz_CH120_DC_Off/On_", "5G_80MHz_CH120_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH120, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["638_5G_-_-_80 MHz_CH120_AC_Off/On_", "5G_80MHz_CH120_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH120, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["639_5G_-_-_80 MHz_CH120_AP_Off/On_", "5G_80MHz_CH120_APTriggerOnOff",
     AP_5G, AP_5Gsuperhigh, AP_5GCH120, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["640_5G_-_-_80 MHz_CH120_IP_ConnectionTest_", "5G_80MHz_CH120_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH120, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["641_5G_-_-_80 MHz_CH124_TV Wifi_Off/On_", "5G_80MHz_CH124_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH124, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["642_5G_-_-_80 MHz_CH124_DC_Off/On_", "5G_80MHz_CH124_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH124, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["643_5G_-_-_80 MHz_CH124_AC_Off/On_", "5G_80MHz_CH124_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH124, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["644_5G_-_-_80 MHz_CH124_AP_Off/On_", "5G_80MHz_CH124_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH124, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["645_5G_-_-_80 MHz_CH124_IP_ConnectionTest_", "5G_80MHz_CH124_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH124, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["646_5G_-_-_80 MHz_CH128_TV Wifi_Off/On_", "5G_80MHz_CH128_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH128, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["647_5G_-_-_80 MHz_CH128_DC_Off/On_", "5G_80MHz_CH128_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH128, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["648_5G_-_-_80 MHz_CH128_AC_Off/On_", "5G_80MHz_CH128_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH128, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["649_5G_-_-_80 MHz_CH128_AP_Off/On_", "5G_80MHz_CH128_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH128, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["650_5G_-_-_80 MHz_CH128_IP_ConnectionTest_", "5G_80MHz_CH128_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH128, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["651_5G_-_-_80 MHz_CH132_TV Wifi_Off/On_", "5G_80MHz_CH132_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH132, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["652_5G_-_-_80 MHz_CH132_DC_Off/On_", "5G_80MHz_CH132_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH132, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["653_5G_-_-_80 MHz_CH132_AC_Off/On_", "5G_80MHz_CH132_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH132, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["654_5G_-_-_80 MHz_CH132_AP_Off/On_", "5G_80MHz_CH132_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH132, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["655_5G_-_-_80 MHz_CH132_IP_ConnectionTest_", "5G_80MHz_CH132_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH132, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["656_5G_-_-_80 MHz_CH136_TV Wifi_Off/On_", "5G_80MHz_CH136_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH136, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["657_5G_-_-_80 MHz_CH136_DC_Off/On_", "5G_80MHz_CH136_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH136, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["658_5G_-_-_80 MHz_CH136_AC_Off/On_", "5G_80MHz_CH136_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH136, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["659_5G_-_-_80 MHz_CH136_AP_Off/On_", "5G_80MHz_CH136_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH136, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["660_5G_-_-_80 MHz_CH136_IP_ConnectionTest_", "5G_80MHz_CH136_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH136, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["661_5G_-_-_80 MHz_CH140_TV Wifi_Off/On_", "5G_80MHz_CH140_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH140, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["662_5G_-_-_80 MHz_CH140_DC_Off/On_", "5G_80MHz_CH140_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH140, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["663_5G_-_-_80 MHz_CH140_AC_Off/On_", "5G_80MHz_CH140_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH140, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["664_5G_-_-_80 MHz_CH140_AP_Off/On_", "5G_80MHz_CH140_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH140, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["665_5G_-_-_80 MHz_CH140_IP_ConnectionTest_", "5G_80MHz_CH140_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH140, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["666_5G_-_-_80 MHz_CH144_TV Wifi_Off/On_", "5G_80MHz_CH144_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH144, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["667_5G_-_-_80 MHz_CH144_DC_Off/On_", "5G_80MHz_CH144_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH144, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["668_5G_-_-_80 MHz_CH144_AC_Off/On_", "5G_80MHz_CH144_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH144, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["669_5G_-_-_80 MHz_CH144_AP_Off/On_", "5G_80MHz_CH144_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH144, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["670_5G_-_-_80 MHz_CH144_IP_ConnectionTest_", "5G_80MHz_CH144_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH144, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["671_5G_-_-_80 MHz_CH149_TV Wifi_Off/On_", "5G_80MHz_CH149_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH149, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["672_5G_-_-_80 MHz_CH149_DC_Off/On_", "5G_80MHz_CH149_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH149, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["673_5G_-_-_80 MHz_CH149_AC_Off/On_", "5G_80MHz_CH149_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH149, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["674_5G_-_-_80 MHz_CH149_AP_Off/On_", "5G_80MHz_CH149_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH149, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["675_5G_-_-_80 MHz_CH149_IP_ConnectionTest_", "5G_80MHz_CH149_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH149, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["676_5G_-_-_80 MHz_CH153_TV Wifi_Off/On_", "5G_80MHz_CH153_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH153, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["677_5G_-_-_80 MHz_CH153_DC_Off/On_", "5G_80MHz_CH153_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH153, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["678_5G_-_-_80 MHz_CH153_AC_Off/On_", "5G_80MHz_CH153_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH153, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["679_5G_-_-_80 MHz_CH153_AP_Off/On_", "5G_80MHz_CH153_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH153, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["680_5G_-_-_80 MHz_CH153_IP_ConnectionTest_", "5G_80MHz_CH153_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH153, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["681_5G_-_-_80 MHz_CH157_TV Wifi_Off/On_", "5G_80MHz_CH157_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH157, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["682_5G_-_-_80 MHz_CH157_DC_Off/On_", "5G_80MHz_CH157_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH157, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["683_5G_-_-_80 MHz_CH157_AC_Off/On_", "5G_80MHz_CH157_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH157, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["684_5G_-_-_80 MHz_CH157_AP_Off/On_", "5G_80MHz_CH157_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH157, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["685_5G_-_-_80 MHz_CH157_IP_ConnectionTest_", "5G_80MHz_CH157_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH157, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
    ["686_5G_-_-_80 MHz_CH161_TV Wifi_Off/On_", "5G_80MHz_CH161_WifiTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH161, AP_5GWPASSIDConnect, WifiTriggerOnOff, Pingip],
    ["687_5G_-_-_80 MHz_CH161_DC_Off/On_", "5G_80MHz_CH161_DCTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH161, AP_5GWPASSIDConnect, DCTriggerOnOff, Pingip],
    ["688_5G_-_-_80 MHz_CH161_AC_Off/On_", "5G_80MHz_CH161_ACTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH161, AP_5GWPASSIDConnect, ACTriggerOnOff, Pingip],
    ["689_5G_-_-_80 MHz_CH161_AP_Off/On_", "5G_80MHz_CH161_APTriggerOnOff", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH161, AP_5GWPASSIDConnect, APTriggerOnOff, Pingip],
    ["690_5G_-_-_80 MHz_CH161_IP_ConnectionTest_", "5G_80MHz_CH161_ConnectionTest", 
     AP_5G, AP_5Gsuperhigh, AP_5GCH161, AP_5GWPASSIDConnect, ConnectionTest, Pingip],
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
                if run == 4:
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
