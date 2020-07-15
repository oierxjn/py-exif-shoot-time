#!/usr/bin/python
#! -*- coding: utf8 -*-
# 说明
#   快捷修改照片的拍摄时间
# 注意
#   1. 需要安装第三方包: pip install python-dateutil
# external
#   date       2020-07-15 15:56:21
#   face       (~￣▽￣)~
#   weather    Tiantai Cloudy 32℃
import os
import subprocess
from dateutil.parser import parse
from tkinter import *
import tkinter.filedialog

# ================ 公共类\方法 ================
def fetchUserDateTime():
    while True:
        print("请输入日期(20200202 12:00)")
        shootTime = input("：")
        try:
            shootTime = parse(shootTime)
            return shootTime
        except Exception as e:
            print("日期解析错误，请重新输入\n")
            continue
        return None
        
def fetchUserPicPaths(picExts):
    root = tkinter.Tk()
    root.withdraw()
    picExtsStr = " ".join(picExts)
    return tkinter.filedialog.askopenfilenames(initialdir=(os.path.expanduser("~\Downloads")), filetypes=[("All Files", picExtsStr), ("PNG", ".png"), ("JPEG", ".jpg .jpeg .jfif .jpe"), ("BMP", ".bmp"), ("TIFF", ".tiff .tif"), ("GIF", ".gif")])
    
def modifyShootTime(dateTime, filePathStr):
    print("\n\n")
    cmdStr = os.getcwd() + '/resources/exiftool.exe -overwrite_original -DateTimeOriginal="' + str(dateTime) + '" ' + filePathStr
    child = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sout, serr = child.communicate()
    print(sout)
    print(serr)
# ================ 公共类\方法 ================



    
# ================ 主逻辑 ================
if __name__=="__main__":
    # ---------------- 获取图片路径 ----------------
    picExts = [".png", ".jpg", ".jpeg", ".jfif", ".jpe", ".bmp", ".tiff", ".tif", ".gif"]
    print("您选择的文件是:")
    filePathStr = ''
    if len(sys.argv) > 1:
        for filePath in sys.argv[1:]:
            if not os.path.isfile(filePath):
                continue
            if not os.path.splitext(filePath)[1] in picExts:
                continue
            print("\t", filePath)
            filePathStr += '"' + filePath + '" '
            
    if len(filePathStr) == 0:
        filePaths = fetchUserPicPaths(picExts)
        if len(filePaths) == 0:
            print("您没有选择任何文件")
            exit(1)
        for i in range(0, len(filePaths)):
            filePath = filePaths[i]
            print("\t", filePath)
            filePathStr += '"' + filePath + '" '
    print("\n\n")
       
       
    # ---------------- 获取自定义日期 ----------------
    dateTime = fetchUserDateTime()
    print("您设定的日期是:\n\t", dateTime)
    print("\n\n确认参数后按任意键继续")
    os.system('pause>nul')
    
    
    # ---------------- 执行 ----------------
    modifyShootTime(dateTime, filePathStr)
    os.system('pause>nul')
# ================ 主逻辑 ================
