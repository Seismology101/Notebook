

import os
import time
from selenium import webdriver
import subprocess

driver= webdriver.Chrome() #  需要 下载 对应浏览器 驱动到 python 安装目录
driver.get("file:///Users/yinfu/code/1-Notebook/Notebook/book/_build/html/intro.html") # 刷新网址




print("Start : %s",time.ctime())
time.sleep(0.01)
os.system("jb build book")
driver.refresh()



while True:
    

    cc = subprocess.Popen(['git status -s'], shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE, cwd="./book")  
    oo = cc.stdout.read()
    out=oo.decode()
    out=out.split("\n")
    cc.wait()
    cc.stdout.close()

    print("out=",len(out))

    if len(out) != 1:
        print("Start : %s",time.ctime())
        time.sleep(0.01)
        os.system("jb build book")
        driver.refresh()
        os.system("git add .")
        os.system(' git commit -m "auto" ')
    else:
        continue