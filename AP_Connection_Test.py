import configparser
from io import StringIO
from os import getcwd, makedirs
from os.path import dirname, abspath, isdir, isfile
from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from worker import sleep
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from ReportLog import LogTextBoxUpdate
from ReportLog import TestLoopBoxUpdate
from GlobalVar import *
from threading import Thread
from ReportLog import *
import TP_Link_Archer_AX20_AP
import ASUS_RT_AC87U_AP
import D_Link_DIR_X1560_AP
import NETGEAR_AX12_RAX120_AP
import ASUS_RT_AX88U_AP
from RouterSupportTable import *
from worker import Worker
from AutoBoxControl import ConnectAutoBox, AcControl
from Txt_To_Excel import TXTFile_To_ExcelFile

config = configparser.ConfigParser()
filepath = abspath(getcwd()) + '/config.ini'

AP_Fun = TP_Link_Archer_AX20
router = ""


def ProgrameControl():
    return


def AP_PingCheckLoop():
    LogTextBoxUpdate("Start test..." + '\n')
    sleep(10)
    LogTextBoxUpdate("Turn On device..." + '\n')
    sleep(20)
    TestLoop_Box.delete(1.0, END)
    Console_Box.delete(1.0, END)
    AP_Fun.GetDeviceID()
    AP_Fun.GetDeviceBrand()
    AP_Fun.GetDeviceName()
    AP_Fun.GetDeviceVersion()
    AP_Fun.AP_Login(AP_ID.get(), AP_PW.get())
    AP_Fun.AP_WiFiEnter()
    AP_Fun.AP_WIFIAction(ProgrameControl.AP_Type)
    raise_frame(btnAP_CheckStart)
    MenuShowOption()
    return


def BrowserRefresh():
    AP_Fun.BrowserPause()
    return


thread1 = Worker(AP_PingCheckLoop)
thread2 = Worker(BrowserRefresh)


def CheckStart():
    print('CheckStart')
    ConnectAutoBox()
    save_user_config()
    MenuHideOption()
    raise_frame(btnAP_CheckPause)
    ProgrameControl.CheckRunning = True
    try:
        if not ProgrameControl.CheckLoopThread.isAlive():
            thread1.start()
    except:
        thread1.start()
    return


def CheckStop():
    print('CheckStop')
    LogTextBoxUpdate("Stop test..." + '\n')
    ConnectAutoBox()
    TestLoop_Box.delete(1.0, END)
    MenuShowOption()
    raise_frame(btnAP_CheckStart)
    ProgrameControl.CheckRunning = False
    thread1.stop()
    thread2.stop()
    AP_Fun.SeleniumFinish()
    LogTextBoxUpdate("generate report..." + '\n')
    TXTFile_To_ExcelFile(File_Info.filePath)
    return


def CheckPause():
    LogTextBoxUpdate("Pause test loop..." + '\n')
    raise_frame(btnAP_CheckResume)
    thread1.pause()
    thread2.start()
    return


def CheckResume():
    LogTextBoxUpdate("Resume test loop..." + '\n')
    raise_frame(btnAP_CheckPause)
    thread2.stop()
    thread1.resume()
    return


def BrowseRreflash():
    sleep(10)
    AP_Fun.BrowserPause()


def raise_frame(frame):
    frame.tkraise()


def UserLogPathSet(DirPath):
    ProgrameControl.UserDirPath = DirPath
    return


def MenuHideOption():
    btn1['state'] = DISABLED
    AP_ID['state'] = DISABLED
    AP_PW['state'] = DISABLED
    comboAPBrand['state'] = DISABLED
    BrowserInfo.comboBrowser['state'] = DISABLED
    TestLoopInfo.Tframe4['state'] = DISABLED
    EthernetInfo.IP_Address['state'] = DISABLED
    EthernetInfo.AP_Webaddress['state'] = DISABLED
    WifiInfo.SSIDFrame24['state'] = DISABLED
    WifiInfo.PWFrame24['state'] = DISABLED
    WifiInfo.SSIDFrame5['state'] = DISABLED
    WifiInfo.PWFrame5['state'] = DISABLED


def MenuShowOption():
    btn1['state'] = NORMAL
    AP_ID['state'] = NORMAL
    AP_PW['state'] = NORMAL
    comboAPBrand['state'] = NORMAL
    BrowserInfo.comboBrowser['state'] = NORMAL
    TestLoopInfo.Tframe4['state'] = NORMAL
    EthernetInfo.IP_Address['state'] = NORMAL
    EthernetInfo.AP_Webaddress['state'] = NORMAL
    WifiInfo.SSIDFrame24['state'] = NORMAL
    WifiInfo.PWFrame24['state'] = NORMAL
    WifiInfo.SSIDFrame5['state'] = NORMAL
    WifiInfo.PWFrame5['state'] = NORMAL


def StopBtnHideOption():
    btn2['state'] = DISABLED


def StopBtnShowOption():
    btn2['state'] = NORMAL


def AdMenuHideOption():
    btn1['state'] = DISABLED


def AdMenuShowOption():
    btn1['state'] = NORMAL

def EnableSWbtn(childList):
    for child in childList:
        child.configure(state='normal')

def DisableSWbtn(childList):
    for child in childList:
        child.configure(state='disable')


def TextInfoUpdate():
    if len(LogTextBoxUpdate.list) > 0:
        Content = LogTextBoxUpdate()
        Console_Box.delete(1.0, END)
        Console_Box.insert('end', Content)
        Console_Box.see(END)
    window.after(1000, TextInfoUpdate)


def TestLoopUpdate():
    if len(TestLoopBoxUpdate.list) > 0:
        Content1 = TestLoopBoxUpdate()
        TestLoop_Box.delete(1.0, END)
        TestLoop_Box.insert('end', Content1)
    window.after(1000, TestLoopUpdate)


def UserLogPathSet(DirPath):
    ProgrameControl.UserDirPath = DirPath
    return


def Report():
    return


def APcallbackFunc(event):
    global router
    global AP_Fun
    print("<<ComboboxSelected>>", APcallbackFunc, comboAPBrand.get())
    ProgrameControl.AP_Type = comboAPBrand.get()
    router = comboAPBrand.get()
    value_24g.set(getRouterValue(router, "2.4G", 1))
    value_5g.set(getRouterValue(router, "5G", 1))
    value_6g.set(getRouterValue(router, "6G", 1))
    value_wpa.set(getRouterValue(router, "WPA", 1))
    value_wpa2.set(getRouterValue(router, "WPA2", 1))
    value_wpa3.set(getRouterValue(router, "WPA3", 1))
    value_80211g.set(getRouterValue(router, "2.4G-802.11g", 1))
    value_80211n.set(getRouterValue(router, "2.4G-802.11n", 1))
    value_80211gn.set(getRouterValue(router, "2.4G-802.11gn", 1))
    value_80211bgn.set(getRouterValue(router, "2.4G-802.11bgn", 1))
    value_80211bgnax.set(getRouterValue(router, "2.4G-802.11bgnax", 1))
    value_80211ax.set(getRouterValue(router, "2.4G-802.11ax", 1))
    value_80211n5G.set(getRouterValue(router, "5G-802.11n", 1))
    value_80211a.set(getRouterValue(router, "5G-802.11a", 1))
    value_80211ac.set(getRouterValue(router, "5G-802.11ac", 1))
    value_80211ax5G.set(getRouterValue(router, "5G-802.11ax", 1))
#MHz
    value_AutoMHz.set(getRouterValue(router, "Auto", 1))
    value_20MHz.set(getRouterValue(router, "20MHz", 1))
    value_40MHz.set(getRouterValue(router, "40MHz", 1))
    value_80MHz.set(getRouterValue(router, "80MHz", 1))
#2.4G CH
    value_24gAuto.set(getRouterValue(router, "2.4G-Auto", 1))
    value_CH1.set(getRouterValue(router, "CH1", 1))
    value_CH2.set(getRouterValue(router, "CH2", 1))
    value_CH3.set(getRouterValue(router, "CH3", 1))
    value_CH4.set(getRouterValue(router, "CH4", 1))
    value_CH5.set(getRouterValue(router, "CH5", 1))
    value_CH6.set(getRouterValue(router, "CH6", 1))
    value_CH7.set(getRouterValue(router, "CH7", 1))
    value_CH8.set(getRouterValue(router, "CH8", 1))
    value_CH9.set(getRouterValue(router, "CH9", 1))
    value_CH10.set(getRouterValue(router, "CH10", 1))
    value_CH11.set(getRouterValue(router, "CH11", 1))
    value_CH12.set(getRouterValue(router, "CH12", 1))
    value_CH13.set(getRouterValue(router, "CH13", 1))
#5G CH
    value_5gAuto.set(getRouterValue(router, "5G-Auto", 1))
    value_CH36.set(getRouterValue(router, "CH36", 1))
    value_CH40.set(getRouterValue(router, "CH40", 1))
    value_CH44.set(getRouterValue(router, "CH44", 1))
    value_CH48.set(getRouterValue(router, "CH48", 1))
    value_CH52.set(getRouterValue(router, "CH52", 1))
    value_CH56.set(getRouterValue(router, "CH56", 1))
    value_CH60.set(getRouterValue(router, "CH60", 1))
    value_CH64.set(getRouterValue(router, "CH64", 1))
    value_CH100.set(getRouterValue(router, "CH100", 1))
    value_CH104.set(getRouterValue(router, "CH104", 1))
    value_CH108.set(getRouterValue(router, "CH108", 1))
    value_CH112.set(getRouterValue(router, "CH112", 1))
    value_CH116.set(getRouterValue(router, "CH116", 1))
    value_CH120.set(getRouterValue(router, "CH120", 1))
    value_CH124.set(getRouterValue(router, "CH124", 1))
    value_CH128.set(getRouterValue(router, "CH128", 1))
    value_CH132.set(getRouterValue(router, "CH132", 1))
    value_CH136.set(getRouterValue(router, "CH136", 1))
    value_CH140.set(getRouterValue(router, "CH140", 1))
    value_CH144.set(getRouterValue(router, "CH144", 1))
    value_CH149.set(getRouterValue(router, "CH149", 1))
    value_CH153.set(getRouterValue(router, "CH153", 1))
    value_CH157.set(getRouterValue(router, "CH157", 1))
    value_CH161.set(getRouterValue(router, "CH161", 1))
    value_CH165.set(getRouterValue(router, "CH165", 1))
#Test Mode
    value_WifiTriggerOnOff.set(getRouterValue(router, "WifiTriggerOnOff", 1))
    value_DCTriggerOnOff.set(getRouterValue(router, "DCTriggerOnOff", 1))
    value_ACTriggerOnOff.set(getRouterValue(router, "ACTriggerOnOff", 1))
    value_APTriggerOnOff.set(getRouterValue(router, "APTriggerOnOff", 1))
    value_ConnectionTest.set(getRouterValue(router, "ConnectionTest", 1))

    if ProgrameControl.AP_Type == "TP_Link_Archer_AX20":
        AP_Fun = TP_Link_Archer_AX20_AP
    elif ProgrameControl.AP_Type == "D_Link_DIR_X1560":
        AP_Fun = D_Link_DIR_X1560_AP
    elif ProgrameControl.AP_Type == "ASUS_RT_AC87U":
        AP_Fun = ASUS_RT_AC87U_AP
    elif ProgrameControl.AP_Type == "NETGEAR_AX12_RAX120":
        AP_Fun = NETGEAR_AX12_RAX120_AP
    elif ProgrameControl.AP_Type == "ASUS_RT_AX88U":
        AP_Fun = ASUS_RT_AX88U_AP

APDict = {"ASUS_RT_AC87U": 'ASUS_RT_AC87U_AP',
          "D_Link_DIR_X1560": 'D_Link_DIR_X1560_AP',
          "TP_Link_Archer_AX20": 'TP_Link_Archer_AX20_AP',
          "NETGEAR_AX12_RAX120": 'NETGEAR_AX12_RAX120_AP',
          "ASUS_RT_AX88U":"ASUS_RT_AX88U_AP"
          }


def AP_Init():
    FileName = APDict[ProgrameControl.AP_Type] + '.py'


def BrowserCallbackFunc(event):
    print("<<ComboboxSelected>>", BrowserCallbackFunc, BrowserInfo.comboBrowser.get())
    ProgrameControl.Browser_Type = BrowserInfo.comboBrowser.get()


window = Tk()
path = StringVar()
window.after(1000, TextInfoUpdate)
window.after(1000, TestLoopUpdate)


def ExitTool():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()


window.protocol("WM_DELETE_WINDOW", ExitTool)


def toogleCheckButton(AP_Type, checkBoxName):
    if getRouterValue(AP_Type, checkBoxName, 1) == 0:
        setRouterValue(AP_Type, checkBoxName, 1)
    elif getRouterValue(AP_Type, checkBoxName, 1) == 1:
        setRouterValue(AP_Type, checkBoxName, 0)


value_24g = IntVar()
value_5g = IntVar()
value_6g = IntVar()
value_wpa = IntVar()
value_wpa2 = IntVar()
value_wpa3 = IntVar()
value_80211g = IntVar()
value_80211n = IntVar()
value_80211gn = IntVar()
value_80211bgn = IntVar()
value_80211bgnax = IntVar()
value_80211ax = IntVar()
value_80211n5G = IntVar()
value_80211a = IntVar()
value_80211ac = IntVar()
value_80211ax5G = IntVar()
value_AutoMHz = IntVar()
value_20MHz = IntVar()
value_40MHz = IntVar()
value_80MHz = IntVar()
value_24gAuto = IntVar()
value_CH1 = IntVar()
value_CH2 = IntVar()
value_CH3 = IntVar()
value_CH4 = IntVar()
value_CH5 = IntVar()
value_CH6 = IntVar()
value_CH7 = IntVar()
value_CH8 = IntVar()
value_CH9 = IntVar()
value_CH10 = IntVar()
value_CH11 = IntVar()
value_CH12 = IntVar()
value_CH13 = IntVar()
value_5gAuto = IntVar()
value_CH36 = IntVar()
value_CH40 = IntVar()
value_CH44 = IntVar()
value_CH48 = IntVar()
value_CH52 = IntVar()
value_CH56 = IntVar()
value_CH60 = IntVar()
value_CH64 = IntVar()
value_CH100 = IntVar()
value_CH104 = IntVar()
value_CH108 = IntVar()
value_CH112 = IntVar()
value_CH116 = IntVar()
value_CH120 = IntVar()
value_CH124 = IntVar()
value_CH128 = IntVar()
value_CH132 = IntVar()
value_CH136 = IntVar()
value_CH140 = IntVar()
value_CH144 = IntVar()
value_CH149 = IntVar()
value_CH153 = IntVar()
value_CH157 = IntVar()
value_CH161 = IntVar()
value_CH165 = IntVar()
value_WifiTriggerOnOff = IntVar()
value_DCTriggerOnOff = IntVar()
value_ACTriggerOnOff = IntVar()
value_APTriggerOnOff = IntVar()
value_ConnectionTest = IntVar()


def disable_event():
    pass


def createNewWindow():
    demoWindow = Toplevel(window)
    demoWindow.title("Advanced Settings")
    demoWindow.geometry("")
    demoWindow.resizable(0, 0)
    demoWindow.configure(bg='#DCDCDC')

    Donebtn = Button(demoWindow, text="Done", bg="#A9A9A9", width=112, font="Arial 9 bold", relief="ridge",
                     command=lambda: [AdMenuShowOption(), demoWindow.destroy()])
    Donebtn.pack(fill="x")

    #demoWindow.rowconfigure(0, weight=1)
    #demoWindow.columnconfigure(0, weight=1)
    #scrollBar = Scrollbar(demoWindow)
    #scrollBar.pack(side=RIGHT, fill=Y)


    labelFrame_Brand = LabelFrame(demoWindow, text="Bands", bg="#DCDCDC", fg="#696969", font="flat 10 bold")
    labelFrame_Security = LabelFrame(demoWindow, text="Security", bg="#DCDCDC", fg="#696969", font="flat 10 bold")
    labelFrame_MHz = LabelFrame(demoWindow, text="MHz", bg="#DCDCDC", fg="#696969", font="flat 10 bold")
    labelFrame_24GMode = LabelFrame(demoWindow, text="2.4G Mode", bg="#DCDCDC", fg="#696969", font="flat 10 bold")
    labelFrame_24GCH = LabelFrame(demoWindow, text="2.4G CH", bg="#DCDCDC", fg="#696969", font="flat 10 bold")
    labelFrame_5GMode = LabelFrame(demoWindow, text="5G Mode", bg="#DCDCDC", fg="#696969", font="flat 10 bold")
    labelFrame_5GCH = LabelFrame(demoWindow, text="5G CH", bg="#DCDCDC", fg="#696969", font="flat 10 bold")
    labelFrame_TestMode = LabelFrame(demoWindow, text="Test Mode", bg="#DCDCDC", fg="#696969", font="flat 10 bold")

    checkButton_24g = Checkbutton(labelFrame_Brand, text="2.4G", variable=value_24g, onvalue=1, offvalue=0,
                                  bg="#DCDCDC", activebackground="#DCDCDC",
                                  command=lambda: [toogleCheckButton(router, checkButton_24g.cget("text"))])
    checkButton_5g = Checkbutton(labelFrame_Brand, text="5G", variable=value_5g, onvalue=1, offvalue=0, bg="#DCDCDC",
                                 activebackground="#DCDCDC",
                                 command=lambda: [toogleCheckButton(router, checkButton_5g.cget("text"))])
    checkButton_6g = Checkbutton(labelFrame_Brand, text="6G", variable=value_6g, onvalue=1, offvalue=0, bg="#DCDCDC",
                                 activebackground="#DCDCDC",
                                 command=lambda: [toogleCheckButton(router, checkButton_6g.cget("text"))])

    checkButton_wpa = Checkbutton(labelFrame_Security, text="WPA", variable=value_wpa, onvalue=1, offvalue=0,
                                  bg="#DCDCDC", activebackground="#DCDCDC",
                                  command=lambda: [toogleCheckButton(router, checkButton_wpa.cget("text"))])
    checkButton_wpa2 = Checkbutton(labelFrame_Security, text="WPA2", variable=value_wpa2, onvalue=1, offvalue=0,
                                   bg="#DCDCDC", activebackground="#DCDCDC",
                                   command=lambda: [toogleCheckButton(router, checkButton_wpa2.cget("text"))])
    checkButton_wpa3 = Checkbutton(labelFrame_Security, text="WPA3", variable=value_wpa3, onvalue=1, offvalue=0,
                                   bg="#DCDCDC", activebackground="#DCDCDC",
                                   command=lambda: [toogleCheckButton(router, checkButton_wpa3.cget("text"))])

    checkButton_80211g = Checkbutton(labelFrame_24GMode, text="2.4G-802.11g", variable=value_80211g, onvalue=1,
                                     offvalue=0,
                                     bg="#DCDCDC", activebackground="#DCDCDC",
                                     command=lambda: [toogleCheckButton(router, checkButton_80211g.cget("text"))])
    checkButton_80211n = Checkbutton(labelFrame_24GMode, text="2.4G-802.11n", variable=value_80211n, onvalue=1,
                                     offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                     command=lambda: [toogleCheckButton(router, checkButton_80211n.cget("text"))])
    checkButton_80211gn = Checkbutton(labelFrame_24GMode, text="2.4G-802.11gn", variable=value_80211gn, onvalue=1,
                                      offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                      command=lambda: [toogleCheckButton(router, checkButton_80211gn.cget("text"))])
    checkButton_80211bgn = Checkbutton(labelFrame_24GMode, text="2.4G-802.11bgn", variable=value_80211bgn, onvalue=1,
                                       offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                       command=lambda: [toogleCheckButton(router, checkButton_80211bgn.cget("text"))])
    checkButton_80211bgnax = Checkbutton(labelFrame_24GMode, text="2.4G-802.11bgnax", variable=value_80211bgnax,
                                         onvalue=1,
                                         offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                         command=lambda: [
                                             toogleCheckButton(router, checkButton_80211bgnax.cget("text"))])
    checkButton_80211ax = Checkbutton(labelFrame_24GMode, text="2.4G-802.11ax", variable=value_80211ax, onvalue=1,
                                      offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                      command=lambda: [toogleCheckButton(router, checkButton_80211ax.cget("text"))])

    checkButton_80211n5G = Checkbutton(labelFrame_5GMode, text="5G-802.11n", variable=value_80211n5G, onvalue=1,
                                       offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                       command=lambda: [toogleCheckButton(router, checkButton_80211n5G.cget("text"))])
    checkButton_80211a = Checkbutton(labelFrame_5GMode, text="5G-802.11a", variable=value_80211a, onvalue=1, offvalue=0,
                                     bg="#DCDCDC", activebackground="#DCDCDC",
                                     command=lambda: [toogleCheckButton(router, checkButton_80211a.cget("text"))])
    checkButton_80211ac = Checkbutton(labelFrame_5GMode, text="5G-802.11ac", variable=value_80211ac, onvalue=1,
                                      offvalue=0,
                                      bg="#DCDCDC", activebackground="#DCDCDC",
                                      command=lambda: [toogleCheckButton(router, checkButton_80211ac.cget("text"))])
    checkButton_80211ax5G = Checkbutton(labelFrame_5GMode, text="5G-802.11ax", variable=value_80211ax5G, onvalue=1,
                                        offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_80211ax5G.cget("text"))])

    checkButton_AutoMHz = Checkbutton(labelFrame_MHz, text="Auto", variable=value_AutoMHz, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_AutoMHz.cget("text"))])
    checkButton_20MHz = Checkbutton(labelFrame_MHz, text="20Mhz", variable=value_20MHz, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_20MHz.cget("text"))])
    checkButton_40MHz = Checkbutton(labelFrame_MHz, text="40Mhz", variable=value_40MHz, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_40MHz.cget("text"))])
    checkButton_80MHz = Checkbutton(labelFrame_MHz, text="80Mhz", variable=value_80MHz, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_80MHz.cget("text"))])

    checkButton_24gAuto = Checkbutton(labelFrame_24GCH, text="2.4G-Auto", variable=value_24gAuto, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_24gAuto.cget("text"))])
    checkButton_CH1 = Checkbutton(labelFrame_24GCH, text="CH1", variable=value_CH1, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH1.cget("text"))])
    checkButton_CH2 = Checkbutton(labelFrame_24GCH, text="CH2", variable=value_CH2, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH2.cget("text"))])
    checkButton_CH3 = Checkbutton(labelFrame_24GCH, text="CH3", variable=value_CH3, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH3.cget("text"))])
    checkButton_CH4 = Checkbutton(labelFrame_24GCH, text="CH4", variable=value_CH4, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH4.cget("text"))])
    checkButton_CH5 = Checkbutton(labelFrame_24GCH, text="CH5", variable=value_CH5, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH5.cget("text"))])
    checkButton_CH6 = Checkbutton(labelFrame_24GCH, text="CH6", variable=value_CH6, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH6.cget("text"))])
    checkButton_CH7 = Checkbutton(labelFrame_24GCH, text="CH7", variable=value_CH7, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH7.cget("text"))])
    checkButton_CH8 = Checkbutton(labelFrame_24GCH, text="CH8", variable=value_CH8, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH8.cget("text"))])
    checkButton_CH9 = Checkbutton(labelFrame_24GCH, text="CH9", variable=value_CH9, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH9.cget("text"))])
    checkButton_CH10 = Checkbutton(labelFrame_24GCH, text="CH10", variable=value_CH10, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH10.cget("text"))])
    checkButton_CH11 = Checkbutton(labelFrame_24GCH, text="CH11", variable=value_CH11, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH11.cget("text"))])
    checkButton_CH12 = Checkbutton(labelFrame_24GCH, text="CH12", variable=value_CH12, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH12.cget("text"))])
    checkButton_CH13 = Checkbutton(labelFrame_24GCH, text="CH13", variable=value_CH13, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH13.cget("text"))])

    checkButton_5gAuto = Checkbutton(labelFrame_5GCH, text="5G-Auto", variable=value_5gAuto, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_5gAuto.cget("text"))])    
    checkButton_CH36 = Checkbutton(labelFrame_5GCH, text="CH36", variable=value_CH36, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH36.cget("text"))])
    checkButton_CH40 = Checkbutton(labelFrame_5GCH, text="CH40", variable=value_CH40, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH40.cget("text"))])
    checkButton_CH44 = Checkbutton(labelFrame_5GCH, text="CH44", variable=value_CH44, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH44.cget("text"))])
    checkButton_CH48 = Checkbutton(labelFrame_5GCH, text="CH48", variable=value_CH48, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH48.cget("text"))])
    checkButton_CH52 = Checkbutton(labelFrame_5GCH, text="CH52", variable=value_CH52, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH52.cget("text"))])
    checkButton_CH56 = Checkbutton(labelFrame_5GCH, text="CH56", variable=value_CH56, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH56.cget("text"))])
    checkButton_CH60 = Checkbutton(labelFrame_5GCH, text="CH60", variable=value_CH60, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH60.cget("text"))])
    checkButton_CH64 = Checkbutton(labelFrame_5GCH, text="CH64", variable=value_CH64, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH64.cget("text"))])
    checkButton_CH100 = Checkbutton(labelFrame_5GCH, text="CH100", variable=value_CH100, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH100.cget("text"))])
    checkButton_CH104 = Checkbutton(labelFrame_5GCH, text="CH104", variable=value_CH104, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH104.cget("text"))])
    checkButton_CH108 = Checkbutton(labelFrame_5GCH, text="CH108", variable=value_CH108, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH108.cget("text"))])
    checkButton_CH112 = Checkbutton(labelFrame_5GCH, text="CH112", variable=value_CH112, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH112.cget("text"))])
    checkButton_CH116 = Checkbutton(labelFrame_5GCH, text="CH116", variable=value_CH116, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH116.cget("text"))])
    checkButton_CH120 = Checkbutton(labelFrame_5GCH, text="CH120", variable=value_CH120, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH120.cget("text"))])
    checkButton_CH124 = Checkbutton(labelFrame_5GCH, text="CH124", variable=value_CH124, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH124.cget("text"))])
    checkButton_CH128 = Checkbutton(labelFrame_5GCH, text="CH128", variable=value_CH128, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH128.cget("text"))])
    checkButton_CH132 = Checkbutton(labelFrame_5GCH, text="CH132", variable=value_CH132, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH132.cget("text"))])
    checkButton_CH136 = Checkbutton(labelFrame_5GCH, text="CH136", variable=value_CH136, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH136.cget("text"))])
    checkButton_CH140 = Checkbutton(labelFrame_5GCH, text="CH140", variable=value_CH140, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH140.cget("text"))])
    checkButton_CH144 = Checkbutton(labelFrame_5GCH, text="CH144", variable=value_CH144, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH144.cget("text"))])
    checkButton_CH149 = Checkbutton(labelFrame_5GCH, text="CH149", variable=value_CH149, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH149.cget("text"))])
    checkButton_CH153 = Checkbutton(labelFrame_5GCH, text="CH153", variable=value_CH153, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH153.cget("text"))])
    checkButton_CH157 = Checkbutton(labelFrame_5GCH, text="CH157", variable=value_CH157, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH157.cget("text"))])
    checkButton_CH161 = Checkbutton(labelFrame_5GCH, text="CH161", variable=value_CH161, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH161.cget("text"))])
    checkButton_CH165 = Checkbutton(labelFrame_5GCH, text="CH165", variable=value_CH165, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_CH165.cget("text"))])

    checkButton_WifiTriggerOnOff = Checkbutton(labelFrame_TestMode, text="WifiTriggerOnOff", variable=value_WifiTriggerOnOff, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_WifiTriggerOnOff.cget("text"))])
    checkButton_DCTriggerOnOff = Checkbutton(labelFrame_TestMode, text="DCTriggerOnOff", variable=value_DCTriggerOnOff, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_DCTriggerOnOff.cget("text"))])
    checkButton_ACTriggerOnOff = Checkbutton(labelFrame_TestMode, text="ACTriggerOnOff", variable=value_ACTriggerOnOff, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_ACTriggerOnOff.cget("text"))])
    checkButton_APTriggerOnOff = Checkbutton(labelFrame_TestMode, text="APTriggerOnOff", variable=value_APTriggerOnOff, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_APTriggerOnOff.cget("text"))])
    checkButton_ConnectionTest = Checkbutton(labelFrame_TestMode, text="ConnectionTest", variable=value_ConnectionTest, onvalue=1, offvalue=0, bg="#DCDCDC", activebackground="#DCDCDC",
                                        command=lambda: [toogleCheckButton(router, checkButton_ConnectionTest.cget("text"))])

    labelFrame_Brand.pack(side=LEFT, fill=BOTH, padx=5, pady=10)
    labelFrame_Security.pack(side=LEFT, fill=BOTH, padx=5, pady=10)
    labelFrame_MHz.pack(side=LEFT, fill=BOTH, padx=5, pady=10)
    labelFrame_24GMode.pack(side=LEFT, fill=BOTH, padx=5, pady=10)
    labelFrame_24GCH.pack(side=LEFT, fill=BOTH, padx=5, pady=10)
    labelFrame_5GMode.pack(side=LEFT, fill=BOTH, padx=5, pady=10)
    labelFrame_5GCH.pack(side=LEFT, fill=BOTH, padx=5, pady=10)
    labelFrame_TestMode.pack(side=LEFT, fill=BOTH, padx=5, pady=10)

    if getRouterValue(router, "2.4G", 0) == 0:
        checkButton_24g.grid_forget()
    else:
        checkButton_24g.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "5G", 0) == 0:
        checkButton_5g.grid_forget()
    else:
        checkButton_5g.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "6G", 0) == 0:
        checkButton_6g.grid_forget()
    else:
        checkButton_6g.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "WPA", 0) == 0:
        checkButton_wpa.grid_forget()
    else:
        checkButton_wpa.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "WPA2", 0) == 0:
        checkButton_wpa2.grid_forget()
    else:
        checkButton_wpa2.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "WPA3", 0) == 0:
        checkButton_wpa3.grid_forget()
    else:
        checkButton_wpa3.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "2.4G-802.11g", 0) == 0:
        checkButton_80211g.grid_forget()
    else:
        checkButton_80211g.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "2.4G-802.11n", 0) == 0:
        checkButton_80211n.grid_forget()
    else:
        checkButton_80211n.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "2.4G-802.11gn", 0) == 0:
        checkButton_80211gn.grid_forget()
    else:
        checkButton_80211gn.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "2.4G-802.11bgn", 0) == 0:
        checkButton_80211bgn.grid_forget()
    else:
        checkButton_80211bgn.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "2.4G-802.11bgnax", 0) == 0:
        checkButton_80211bgnax.grid_forget()
    else:
        checkButton_80211bgnax.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "2.4G-802.11ax", 0) == 0:
        checkButton_80211ax.grid_forget()
    else:
        checkButton_80211ax.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "5G-802.11n", 0) == 0:
        checkButton_80211n5G.grid_forget()
    else:
        checkButton_80211n5G.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "5G-802.11a", 0) == 0:
        checkButton_80211a.grid_forget()
    else:
        checkButton_80211a.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "5G-802.11ac", 0) == 0:
        checkButton_80211ac.grid_forget()
    else:
        checkButton_80211ac.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "5G-802.11ax", 0) == 0:
        checkButton_80211ax5G.grid_forget()
    else:
        checkButton_80211ax5G.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "Auto", 0) == 0:
        checkButton_AutoMHz.grid_forget()
    else:
        checkButton_AutoMHz.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "20MHz", 0) == 0:
        checkButton_20MHz.grid_forget()
    else:
        checkButton_20MHz.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "40MHz", 0) == 0:
        checkButton_40MHz.grid_forget()
    else:
        checkButton_40MHz.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "80MHz", 0) == 0:
        checkButton_80MHz.grid_forget()
    else:
        checkButton_80MHz.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "2.4G-Auto", 0) == 0:
        checkButton_24gAuto.grid_forget()
    else:
        checkButton_24gAuto.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH1", 0) == 0:
        checkButton_CH1.grid_forget()
    else:
        checkButton_CH1.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH2", 0) == 0:
        checkButton_CH2.grid_forget()
    else:
        checkButton_CH2.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH3", 0) == 0:
        checkButton_CH3.grid_forget()
    else:
        checkButton_CH3.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH4", 0) == 0:
        checkButton_CH4.grid_forget()
    else:
        checkButton_CH4.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH5", 0) == 0:
        checkButton_CH5.grid_forget()
    else:
        checkButton_CH5.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH6", 0) == 0:
        checkButton_CH6.grid_forget()
    else:
        checkButton_CH6.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH7", 0) == 0:
        checkButton_CH7.grid_forget()
    else:
        checkButton_CH7.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH8", 0) == 0:
        checkButton_CH8.grid_forget()
    else:
        checkButton_CH8.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH9", 0) == 0:
        checkButton_CH9.grid_forget()
    else:
        checkButton_CH9.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH10", 0) == 0:
        checkButton_CH10.grid_forget()
    else:
        checkButton_CH10.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH11", 0) == 0:
        checkButton_CH11.grid_forget()
    else:
        checkButton_CH11.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH12", 0) == 0:
        checkButton_CH12.grid_forget()
    else:
        checkButton_CH12.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH13", 0) == 0:
        checkButton_CH13.grid_forget()
    else:
        checkButton_CH13.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "5G-Auto", 0) == 0:
        checkButton_5gAuto.grid_forget()
    else:
        checkButton_5gAuto.grid(row=0, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH36", 0) == 0:
        checkButton_CH36.grid_forget()
    else:
        checkButton_CH36.grid(row=1, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH40", 0) == 0:
        checkButton_CH40.grid_forget()
    else:
        checkButton_CH40.grid(row=2, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH44", 0) == 0:
        checkButton_CH44.grid_forget()
    else:
        checkButton_CH44.grid(row=3, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH48", 0) == 0:
        checkButton_CH48.grid_forget()
    else:
        checkButton_CH48.grid(row=4, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH52", 0) == 0:
        checkButton_CH52.grid_forget()
    else:
        checkButton_CH52.grid(row=5, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH56", 0) == 0:
        checkButton_CH56.grid_forget()
    else:
        checkButton_CH56.grid(row=6, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH60", 0) == 0:
        checkButton_CH60.grid_forget()
    else:
        checkButton_CH60.grid(row=7, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH64", 0) == 0:
        checkButton_CH64.grid_forget()
    else:
        checkButton_CH64.grid(row=8, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH100", 0) == 0:
        checkButton_CH100.grid_forget()
    else:
        checkButton_CH100.grid(row=9, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH104", 0) == 0:
        checkButton_CH104.grid_forget()
    else:
        checkButton_CH104.grid(row=10, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH108", 0) == 0:
        checkButton_CH108.grid_forget()
    else:
        checkButton_CH108.grid(row=11, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH112", 0) == 0:
        checkButton_CH112.grid_forget()
    else:
        checkButton_CH112.grid(row=12, column=0, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH116", 0) == 0:
        checkButton_CH116.grid_forget()
    else:
        checkButton_CH116.grid(row=0, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH120", 0) == 0:
        checkButton_CH120.grid_forget()
    else:
        checkButton_CH120.grid(row=1, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH124", 0) == 0:
        checkButton_CH124.grid_forget()
    else:
        checkButton_CH124.grid(row=2, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH128", 0) == 0:
        checkButton_CH128.grid_forget()
    else:
        checkButton_CH128.grid(row=3, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH132", 0) == 0:
        checkButton_CH132.grid_forget()
    else:
        checkButton_CH132.grid(row=4, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH136", 0) == 0:
        checkButton_CH136.grid_forget()
    else:
        checkButton_CH136.grid(row=5, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH140", 0) == 0:
        checkButton_CH140.grid_forget()
    else:
        checkButton_CH140.grid(row=6, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH144", 0) == 0:
        checkButton_CH144.grid_forget()
    else:
        checkButton_CH144.grid(row=7, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH149", 0) == 0:
        checkButton_CH149.grid_forget()
    else:
        checkButton_CH149.grid(row=8, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH153", 0) == 0:
        checkButton_CH153.grid_forget()
    else:
        checkButton_CH153.grid(row=9, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH157", 0) == 0:
        checkButton_CH157.grid_forget()
    else:
        checkButton_CH157.grid(row=10, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH161", 0) == 0:
        checkButton_CH161.grid_forget()
    else:
        checkButton_CH161.grid(row=11, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "CH165", 0) == 0:
        checkButton_CH165.grid_forget()
    else:
        checkButton_CH165.grid(row=12, column=1, ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "WifiTriggerOnOff", 0) == 0:
        checkButton_WifiTriggerOnOff.grid_forget()
    else:
        checkButton_WifiTriggerOnOff.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "DCTriggerOnOff", 0) == 0:
        checkButton_DCTriggerOnOff.grid_forget()
    else:
        checkButton_DCTriggerOnOff.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "ACTriggerOnOff", 0) == 0:
        checkButton_ACTriggerOnOff.grid_forget()
    else:
        checkButton_ACTriggerOnOff.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "APTriggerOnOff", 0) == 0:
        checkButton_APTriggerOnOff.grid_forget()
    else:
        checkButton_APTriggerOnOff.grid(ipadx=5, pady=3, sticky=W + N)

    if getRouterValue(router, "ConnectionTest", 0) == 0:
        checkButton_ConnectionTest.grid_forget()
    else:
        checkButton_ConnectionTest.grid(ipadx=5, pady=3, sticky=W + N)

    demoWindow.protocol("WM_DELETE_WINDOW", disable_event)
    demoWindow.mainloop()


variable = StringVar()

btnAP_CheckPause = Frame(window)
btnAP_CheckResume = Frame(window)
btnAP_CheckStart = Frame(window)

# Title
window.title("Wi-Fi Test_v1.08")
# Frame size
window.geometry('900x425')
# Fixed size
window.resizable(0, 0)
# BG Color
window.configure(bg='#DCDCDC')

# Title
label1 = Label(window, text="TPV", relief="flat", fg="blue", bg="#DCDCDC",
               height=1, width=5, font="Arial 26 bold")
label2 = Label(window, text="Wi-Fi Compatibility Auto Test", fg="White", bg="#DCDCDC",
               height=1, width=30, font="Arial 25 bold")
label3 = Label(window, text="Loop Number:", bg="#DCDCDC",
               height=1, width=20, font="Arial 10 bold")

label1.place(x=15, y=10)
label2.place(x=190, y=22)
label3.place(x=712, y=57)

# AP Select List
fm5 = Frame(width=835, height=50, relief=GROOVE, borderwidth=2, bg="#DCDCDC")
labelTop = Label(window, text="AP Brand:", bg="#DCDCDC")
comboAPBrand = ttk.Combobox(window,
                            values=["ASUS_RT_AC87U", "ASUS_RT_AX88U", "D_Link_DIR_X1560", "TP_Link_Archer_AX20", "NETGEAR_AX12_RAX120"],
                            state="readonly", width=24)
labelTop.place(x=45, y=135)
comboAPBrand.place(x=115, y=135)
comboAPBrand.current(0)
ProgrameControl.AP_Type = comboAPBrand.get()
comboAPBrand.bind("<<ComboboxSelected>>", APcallbackFunc)
print(ProgrameControl.AP_Type)
fm5.place(x=35, y=120)

# Browser Slect List
labelTop1 = Label(window, text="Open Browser:", bg="#DCDCDC")
BrowserInfo.comboBrowser = ttk.Combobox(window, values=["Chrome", "Firefox"],
                                        state="readonly", width=25)
labelTop1.place(x=315, y=135)
BrowserInfo.comboBrowser.place(x=410, y=135)
BrowserInfo.comboBrowser.current(0)
ProgrameControl.Browser_Type = BrowserInfo.comboBrowser.get()
BrowserInfo.comboBrowser.bind("<<ComboboxSelected>>", BrowserCallbackFunc)

# Button
for BTNframe in (btnAP_CheckStart, btnAP_CheckResume, btnAP_CheckPause):
    BTNframe.place(x=467, y=85)
for child in BTNframe.winfo_children():
    child.configure(state='enable')

Button(btnAP_CheckStart, text='Satrt', bg="#3CB371", width=16, font="flat 9 bold", relief="ridge", padx=4,
       command=lambda: [EnableSWbtn(BTNframe.winfo_children()), StopBtnShowOption(), CheckStart()]).pack()
Button(btnAP_CheckResume, text='Resume', bg="#5F9EA0", width=16, font="flat 9 bold", relief="ridge", padx=4,
       command=lambda: [CheckResume()]).pack()
Button(btnAP_CheckPause, text='Pause', bg="#FFD700", width=16, font="flat 9 bold", relief="ridge", padx=4,
       command=lambda: [CheckPause()]).pack()


btn1 = Button(window, text="Advanced Settings", bg="#A9A9A9", width=16, font="flat 9 bold", relief="ridge",
              command=lambda: [AdMenuHideOption(), createNewWindow()])
btn1.place(x=747, y=85)

btn2 = Button(window, text='Stop', bg="#FF7093", width=16, font="flat 9 bold", relief="ridge", padx=4,
              state=DISABLED, command=lambda: [DisableSWbtn(BTNframe.winfo_children()), StopBtnHideOption(), CheckStop()])
btn2.place(x=607, y=85)


# Test loop Frame
label = Label(window, text="Test Loop:", bg="#DCDCDC")
label.place(x=620, y=135)
TestLoopInfo.Tframe4 = Entry(window, width=23)
TestLoopInfo.Tframe4.place(x=690, y=135)

# ID & PW Frame
fm1 = Frame(width=270, height=70, relief=GROOVE, borderwidth=2, bg="#DCDCDC")
label = Label(window, text="AP Login", fg="#696969", bg="#DCDCDC", font="flat 12 bold")
Tframe1 = Label(window, text="ID :", bg="#DCDCDC")
Tframe2 = Label(window, text=",  PW :", bg="#DCDCDC")
AP_ID = Entry(window, width=10)
AP_PW = Entry(window, width=10)
# Remi修改
# AP_PW = Entry(window, show="*", width=10)
# Remi修改
label.place(x=50, y=189)
Tframe1.place(x=50, y=220)
Tframe2.place(x=160, y=220)
AP_ID.place(x=80, y=220)
AP_PW.place(x=210, y=220)
fm1.place(x=35, y=180)

# Text frame - IP address
fm2 = Frame(width=170, height=70, relief=GROOVE, borderwidth=2, bg="#DCDCDC")
label = Label(window, text="TV Ethernet", fg="#696969", bg="#DCDCDC", font="Arial 12 bold")
Tframe = Label(window, text="IP :", bg="#DCDCDC")
EthernetInfo.IP_Address = Entry(window, width=15)
label.place(x=330, y=189)
Tframe.place(x=330, y=220)
EthernetInfo.IP_Address.place(x=360, y=220)
fm2.place(x=315, y=180)

# Text frame - AP test
fm3 = Frame(width=375, height=70, relief=GROOVE, borderwidth=2, bg="#DCDCDC")
label = Label(window, text="Web Address", fg="#696969", bg="#DCDCDC", font="Arial 12 bold")
EthernetInfo.AP_Webaddress = Entry(window, width=48)
fm3.place(x=495, y=180)
label.place(x=510, y=189)
EthernetInfo.AP_Webaddress.place(x=510, y=220)

# SSID & PWP frame
fm4 = Frame(width=835, height=70, relief=GROOVE, borderwidth=2, bg="#DCDCDC")
label1 = Label(window, text="2.4G Wi-Fi", fg="#696969", bg="#DCDCDC", font="Arial 12 bold")
Tframe1 = Label(window, text="SSID :", bg="#DCDCDC")
WifiInfo.SSIDFrame24 = Entry(window, width=17)
Tframe2 = Label(window, text="PW :", bg="#DCDCDC")
WifiInfo.PWFrame24 = Entry(window, width=17)
label2 = Label(window, text="5G Wi-Fi", fg="#696969", bg="#DCDCDC", font="Arial 12 bold")
Tframe3 = Label(window, text="SSID :", bg="#DCDCDC")
WifiInfo.SSIDFrame5 = Entry(window, width=17)
Tframe4 = Label(window, text="PW :", bg="#DCDCDC")
WifiInfo.PWFrame5 = Entry(window, width=17)

label1.place(x=50, y=269)
Tframe1.place(x=50, y=297)
WifiInfo.SSIDFrame24.place(x=100, y=297)
Tframe2.place(x=250, y=297)
WifiInfo.PWFrame24.place(x=290, y=297)
label2.place(x=488, y=269)
Tframe3.place(x=488, y=297)
WifiInfo.SSIDFrame5.place(x=538, y=297)
Tframe4.place(x=688, y=297)
WifiInfo.PWFrame5.place(x=728, y=297)
fm4.place(x=35, y=260)

# Test Loop frame
TestLoop_Box = Text(window, height=1, width=4, font="Arial 12 bold", fg='red', bg="#DCDCDC", relief="flat")
TestLoop_Box.place(x=847, y=57)

# Console frame - show log frame
scrolW = 116
scrolH = 5
Console_Box = scrolledtext.ScrolledText(window, width=scrolW, height=scrolH, font=('consolas', 9), fg='white',
                                        bg='black')
Console_Box.place(x=35, y=340)


def create_user_config():
    config['ap_brand'] = {'value': ''}
    config['ap_id'] = {'value': ''}
    config['ap_password'] = {'value': ''}
    config['open_browser'] = {'value': ''}
    config['testinfo_check'] = {'value': 'True', 'test_loop': ''}
    config['ethernet_check'] = {'value': 'True', 'ip': ''}
    config['Web_check'] = {'value': 'True', 'Web_address': ''}
    config['2.4G_WiFi_SSID'] = {'value': 'True', '2.4G_SSID': ''}
    config['2.4G_WiFi_PW'] = {'value': 'True', '2.4G_PW': ''}
    config['5G_WiFi_SSID'] = {'value': 'True', '5G_SSID': ''}
    config['5G_WiFi_PW'] = {'value': 'True', '5G_PW': ''}
    config['ReportPath'] = {'UserPath': '', 'UserReprotPath': ''}
    # ap_brand
    config.set('ap_brand', 'value', 'TP_Link_Archer_AX20')
    # Browser
    config.set('open_browser', 'value', 'Chrome')
    # Test_Loop
    config.set('testinfo_check', 'test_loop', '1')
    # ethernet_ip
    config.set('ethernet_check', 'ip', '192.168.100.500')
    # open_browser
    config.set('Web_check', 'Web_address', 'http://192.168.100.1/info/Login.html')
    # 2.4g_ssid
    config.set('2.4G_WiFi_SSID', '2.4g_ssid', 'WIFI_Test')
    # 2.4g_pw
    config.set('2.4G_WiFi_PW', '2.4g_pw', '88888888')
    # 5g_ssid
    config.set('5G_WiFi_SSID', '5g_ssid', 'WIFI_Test_5G')
    # 5g_pw
    config.set('5G_WiFi_PW', '5g_pw', '88888888')

    with open(filepath, 'w') as configfile:
        config.write(configfile)


def load_user_config():
    config.read(filepath)
    # ap_brand
    comboAPBrand.set(config.get('ap_brand', 'value'))
    AP_ID.insert(0, config.get('ap_id', 'value'))
    AP_PW.insert(0, config.get('ap_password', 'value'))
    # Browser
    BrowserInfo.comboBrowser.set(config.get('open_browser', 'value'))
    # TestInfo_check
    TestLoopInfo.Tframe4.insert(0, config.get('testinfo_check', 'test_loop'))
    # ethernet_check
    EthernetInfo.IP_Address.insert(0, config.get('ethernet_check', 'ip'))
    # Web_check
    EthernetInfo.AP_Webaddress.insert(0, config.get('Web_check', 'Web_address'))
    # 2.4G&5G_SSID/PW_check
    WifiInfo.SSIDFrame24.insert(0, config.get('2.4G_WiFi_SSID', '2.4g_ssid'))
    WifiInfo.PWFrame24.insert(0, config.get('2.4G_WiFi_PW', '2.4g_pw'))
    WifiInfo.SSIDFrame5.insert(0, config.get('5G_WiFi_SSID', '5g_ssid'))
    WifiInfo.PWFrame5.insert(0, config.get('5G_WiFi_PW', '5g_pw'))

    APcallbackFunc(None)


def save_user_config():
    # ap_brand
    config.set('ap_brand', 'value', str(comboAPBrand.get()))
    config.set('ap_id', 'value', AP_ID.get())
    config.set('ap_password', 'value', AP_PW.get())
    # Browser
    config.set('open_browser', 'value', str(BrowserInfo.comboBrowser.get()))
    # TestInfo_check
    config.set('testinfo_check', 'test_loop', str(TestLoopInfo.Tframe4.get()))
    # ethernet_check
    config.set('ethernet_check', 'ip', str(EthernetInfo.IP_Address.get()))
    config.set('Web_check', 'Web_address', str(EthernetInfo.AP_Webaddress.get()))
    # 2.4G&5G_SSID/PW
    config.set('2.4G_WiFi_SSID', '2.4g_ssid', str(WifiInfo.SSIDFrame24.get()))
    config.set('2.4G_WiFi_PW', '2.4g_pw', str(WifiInfo.PWFrame24.get()))
    config.set('5G_WiFi_SSID', '5g_ssid', str(WifiInfo.SSIDFrame5.get()))
    config.set('5G_WiFi_PW', '5g_pw', str(WifiInfo.PWFrame5.get()))

    with open(filepath, 'w') as configfile:
        config.write(configfile)


if isfile(filepath):
    load_user_config()
else:
    create_user_config()
    load_user_config()

window.mainloop()
