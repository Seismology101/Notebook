#!/Users/yinfu/opt/miniconda3/bin python3
# -*- coding: utf-8 -*-
"""
Use jupyter-book generate html automatically.
    1. Download Chrome-driver Plug-in for selenium package from https://chromedriver.chromium.org/
    2. Run this script 

@Author: Fu Yin || Fri Jul 22 21:59:08 2022
"""

import os
import time
import subprocess
from selenium import webdriver


#%% Functions
def jb_build(driver, cwd_path):
    print("Start:", time.ctime())
    os.system(f"jb build {cwd_path}")
    driver.refresh()


def git_status(cwd_path):
    cmd_git = subprocess.Popen(['git status -s'], shell = True, \
        stdin = subprocess.PIPE, stdout = subprocess.PIPE, cwd = cwd_path)  
    cmd_out_raw = cmd_git.stdout.read()
    cmd_git.wait()
    cmd_git.stdout.close()
    cmd_out = cmd_out_raw.decode()
    out = cmd_out.split("\n")
    return out


def git_commit():
    os.system(""" git add . """)
    os.system(""" git commit -m "auto" """)


def main():
    driver= webdriver.Chrome()
    driver.get(url)
    os.system("git switch dev")
    jb_build(driver, cwd_path)
    while True:
        time.sleep(sleep_time)
        out = git_status(cwd_path) 
        if len(out) != 1:
            print("Change number = ", len(out))
            jb_build(driver, cwd_path)
            git_commit()
        else:
            print("No change and continue...")
            continue



#%% Main
url = "file:///Users/yinfu/code/1-Notebook/Notebook/book/_build/html/intro.html"
cwd_path = "./book"
sleep_time = 0.1 # unit/s

if __name__ == '__main__':
    main()

