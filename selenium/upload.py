import time
import win32gui
import win32con
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

def upload_file(filepath):
    # 一级窗口
    dialog=win32gui.FindWindow("#32770","打开")
    #找到窗口二级元素
    ComboBoxEx32=win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
    #三级元素
    combox=win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)
    # EDIT元素
    edit=win32gui.FindWindowEx(combox,0,"Edit",None)
    #打开按钮元素
    button=win32gui.FindWindowEx(dialog,0,"Button",None)
    #edit 中输入文件全名称（完整路径）
    #"E:\testimg\QQ1.jpg" 设置为参数
    win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filepath)
    #点击打开按钮提交
    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)

driver =webdriver.Chrome()
# driver.maximize_window() #最大化打开chrome
driver.get("file:///G:/projects/PYTHON-python-study/selenium/5.html")



# driver.find_element_by_xpath('//input[@placeholder="帐号"]').send_keys(username)
# driver.find_element_by_xpath('//input[@placeholder="密码"]').send_keys(password)

# 点击上传文件按钮
# x= driver.find_element_by_xpath('//input[@id="file"]') #此处抓取不到，超时报错
x= driver.find_element_by_id("kevin")

ActionChains(driver).move_to_element(x).click(x).perform()

time.sleep(2)




# 点击文件上传，弹窗出现窗口
# 出现弹窗窗口,使用upload 方法
filepath = "E:\\outFile.doc"
upload_file(filepath)