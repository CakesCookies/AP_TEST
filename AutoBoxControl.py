import os
from clr import System
import serial
import serial.tools.list_ports

# 我又進來了

def AutoBox():
    # print('Search...')
    ports = serial.tools.list_ports.comports(include_links=False)
    if ports:
        for port in ports:
            # print('location',port.location)
            # print('vid',port.vid)
            # print('pid',port.pid)
            locationStr = str(port.location)
            if locationStr.find(".5") != -1 and port.vid == 1659 and port.pid == 8963:
                # print('1. AutoBox port is:', port.device)
                Comport = port.device
                Version = '2'
                break
            elif locationStr.find(".3") != -1 and port.vid == 1659 and port.pid == 8963:
                # print('2. AutoBox port is:', port.device)
                Comport = port.device
                Version = '1'
                break
        return Comport, Version


# define dll
dll_GPIO = System.Reflection.Assembly.LoadFile(os.path.abspath(os.getcwd()) + '/GPIO.dll')
dll_BlueRatLibrary = System.Reflection.Assembly.LoadFile(os.path.abspath(os.getcwd()) + '/BlueRatLibrary.dll')

# define class
class_GpioControl = dll_GPIO.GetType('GPIO.Gpio_Control')
call_GpioControl = System.Activator.CreateInstance(class_GpioControl)


def ConnectAutoBox():
    if AutoBox():
        AutoBoxInfo = AutoBox()
        if AutoBoxInfo[1] == '1':
            call_GpioControl.Connect_SerialPort(AutoBoxInfo[0])
        elif AutoBoxInfo[1] == '2':
            call_GpioControl.Connect_AutoBox2(AutoBoxInfo[0])


def AcControl(Ac, Switch):
    if Ac == 'ac1':
        if Switch == 'on':
            call_GpioControl.Set_GP0_To_1()
            # print('ac1_on')
        elif Switch == 'off':
            call_GpioControl.Set_GP0_To_0()
            # print('ac1_off')
    elif Ac == 'ac2':
        if Switch == 'on':
            call_GpioControl.Set_GP1_To_1()
            # print('ac2_on')
        elif Switch == 'off':
            call_GpioControl.Set_GP1_To_0()
            # print('ac2_off')
