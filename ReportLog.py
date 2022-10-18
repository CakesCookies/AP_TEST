from time import asctime as time_asctime
from time import localtime as time_localtime
from time import time as time_time


def LogTextBoxUpdate(newStr=""):
    if newStr != "":
        if len(LogTextBoxUpdate.list) < 168:
            LogTextBoxUpdate.list.append(newStr)
        else:
            LogTextBoxUpdate.list.pop(0)
            LogTextBoxUpdate.list.append(newStr)
    LogContent = "".join(LogTextBoxUpdate.list)
    return LogContent

def TestLoopBoxUpdate(newStr=""):
    if newStr != "":
        if len(TestLoopBoxUpdate.list) < 1:
            TestLoopBoxUpdate.list.append(newStr)
        else:
            TestLoopBoxUpdate.list.pop(0)
            TestLoopBoxUpdate.list.append(newStr)
    LogContent1 = "".join(TestLoopBoxUpdate.list)
    return LogContent1

def LogTextBoxClear():
    LogTextBoxUpdate.list = []

def  TestLoopBoxClear():
    TestLoopBoxUpdate.list = []

LogTextBoxUpdate.list = []
TestLoopBoxUpdate.list = []