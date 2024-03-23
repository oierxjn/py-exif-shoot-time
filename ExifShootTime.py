#!/usr/bin/python
#! -*- coding: utf8 -*-
# 说明
#   快捷修改照片的拍摄时间
# 注意
#   1. 需要安装第三方包: pip install python-dateutil
#   2. 需要安装第三方包: pip install pypiwin32
# external
#   date       2020-07-15 15:56:21
#   face       (~￣▽￣)~
#   weather    Tiantai Cloudy 32℃
import os,sys
import subprocess
from dateutil.parser import parse
from tkinter import *
import tkinter.filedialog
import win32gui,win32con

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
    return tkinter.filedialog.askopenfilenames(initialdir=(os.path.expanduser(r"~\Downloads")), filetypes=[("All Files", picExtsStr), ("PNG", ".png"), ("JPEG", ".jpg .jpeg .jfif .jpe"), ("BMP", ".bmp"), ("TIFF", ".tiff .tif"), ("GIF", ".gif")])    
    
def modifyShootTime(dateTime, filePathStr):
    print("\n\n")
    cmdStr = os.getcwd() + '/resources/exiftool.exe" -overwrite_original -DateTimeOriginal="' + str(dateTime) + '" ' + filePathStr
    cmdStr = '"'+cmdStr
    child = subprocess.Popen(cmdStr, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    sout, serr = child.communicate()
#     print(cmdStr)
    print("运行信息：",sout)
    print("错误信息：",serr)
    
def setFocus(title):
    if title == None:
        return
#     def callback (hwnd, hwnds):
#         if win32gui.IsWindow(hwnd) and win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
#             if win32gui.GetWindowText(hwnd) == title:
#                 win32gui.SetForegroundWindow(hwnd)
#                 return 
#     win32gui.EnumWindows(callback, [])
    hwnd = win32gui.FindWindow(None, title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(hwnd)
    else:
        print("未找到指定的控制台窗口，请手动点击窗口")
# ================ 公共类\方法 ================



    
# ================ 主逻辑 ================
if __name__=="__main__":
    title = "快捷修改照片的拍摄时间"
    os.system("title " + title)


    # ---------------- 获取图片路径 ----------------
    picExts = [".png", ".jpg", ".jpeg", ".jfif", ".jpe", ".bmp", ".tiff", ".tif", ".gif"]
    print("您选择的文件是:")
    filePathStr_list = []
    block_size=100
    if len(sys.argv) > 1:
        list_cnt=0
        file_cnt=0
        filePathStr_list.append('')
        for filePath in sys.argv[1:]:
            if not os.path.isfile(filePath):
                continue
            if not os.path.splitext(filePath)[1] in picExts:
                continue
            print("\t", filePath)
            filePathStr_list[list_cnt] += '"' + filePath + '" '
            file_cnt+=1
            if file_cnt==block_size:
                filePathStr_list.append('')
                list_cnt+=1
                file_cnt=0
            
    if len(filePathStr_list) == 0:
        filePaths = fetchUserPicPaths(picExts)
        if len(filePaths) == 0:
            print("您没有选择任何文件")
            print("任意键退出")
            exit(1)
        list_cnt=0
        file_cnt=0
        filePathStr_list.append('')
        for i in range(0, len(filePaths)):
            filePath = filePaths[i]
            print("\t", filePath)
            filePathStr_list[list_cnt] += '"' + filePath + '" '
            file_cnt+=1
            if file_cnt==block_size:
                filePathStr_list.append('')
                list_cnt+=1
                file_cnt=0
                
    setFocus(title)
    print("\n\n")
    
       
    # ---------------- 获取自定义日期 ----------------
    dateTime = fetchUserDateTime()
    print("您设定的日期是:\n\t", dateTime)
    print("\n\n确认参数后按任意键开始任务")
    os.system('pause>nul')
    print("\n\n任务进行中\n\n")
    
    # ---------------- 分块执行 ----------------
    list_cnt=1
    list_number=len(filePathStr_list)
    for filePathStr in filePathStr_list:
#         print(filePathStr)
        modifyShootTime(dateTime, filePathStr)
        print("第",list_cnt,"/",list_number,"分块完成")
        list_cnt+=1
    
    # ---------------- 结束 ----------------
    print("\n\n任务完成\n\n任意键退出")
    os.system('pause>nul')
# ================ 主逻辑 ================
