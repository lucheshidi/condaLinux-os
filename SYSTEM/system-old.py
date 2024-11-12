# -*- coding:utf-8 -*-
# name:----------Jyx
# time:----------2023.1.15

from sys import *
from random import *
import subprocess

from openpyxl.packaging.manifest import Override


def run_command(command):
    result = subprocess.run(command, shell=True, text=True)
    return result

run_command("python -m pip install --upgrade pip>nul")
run_command("python -m pip install pofile>nul")

import pofile

# 系统安装
def install():
    print("System not setup! Launching setup program...")
    run_command("ping 127.0.0.1>nul")
    # 测试(没用)
    print("""condaLinux Setup Version 1.0
Test your computer ...""")
    run_command("ping 127.0.0.1>nul")
    print("Your computer can install condaLinux!")
    # Linux 安装三件套~
    name = str(input("Please input your computer name> "))
    username = str(input("Please input username> "))
    password = str(input("Please input password> "))
    print("saving configs ...")
    run_command("ping 127.0.0.1>nul")
    sp_password = str(input("Please input spur(SuperUser)'s password> "))
    # 开始安装
    pofile.mkdir("./usr/systemd/config/")
    with open("./usr/systemd/config/user.properties", "w", encoding="utf-8") as config:
        config.write(username + "\n")
        config.write(password + "\n")
        config.write(sp_password)
    print("Installing System ...")
    pofile.mkdir("./usr/Application/")
    pofile.mkdir(f"./home/{username}/")
    pofile.mkdir("./root/")
    # 设置install.conf
    try:
        with open("./install.conf", "w", encoding="utf-8") as create:
            # 创建install.json文件
            create.write("condaLinuxInstalled = True")
    except FileNotFoundError:
        print("ERROR: can't create install.conf")
    run_command("ping 127.0.0.1>nul")
    # 延个迟~
    print("System Install SUCCESS!")
    # 重启
    reboot = str(input("Would you like to reboot now?[Y/n] "))
    if reboot == "y" or reboot == "Y":
        return main()
    else:
        print("System will be shutdown NOW!")
        return

def boot():
    # 系统引导
    with open("./usr/systemd/config/user.properties", "w", encoding="utf-8") as conf:
        real_username = conf.readline(1)
        real_password = conf.readline(2)
        name = conf.readline(3)
        name = conf.strip("Name = ")
        root_password = conf.readline(4)
    print(name, " login:")
    test_username = str(input("username> "))
    def password_input():
        test_password = str(input("password> "))
    password_input()
    password_error = int(0)

    if test_username == real_username and test_password == real_password:
        # 普通登录
        system(false)
    elif test_username == "root" or test_username == "su" or test_username == "spur":
        # 尝试以 root 身份进入
        system(true)
    else: # 密码错误
        print("Login recorded")
        return password_input()
        password_error + 1
    if password_error == 5: # 密码错5次就关机
        print("password always recorded, shutting down ...")
        run_command("ping 127.0.0.1>nul")
        return

# 进入系统
def system(root):
    with open("./usr/systemd/config/user.properties", "w", encoding="utf-8") as conf:
        username = conf.readline(1)
        name = conf.readline(2)
        name = conf.strip("Name = ")
    if root == false:
        while True:
            run = str(input(f"{username}-&-{name}:[~]$ "))
    elif root == true:
        while True:
            run = str(input(f"root-&-{name}:[~]# "))

def main():
    try:
        with open("./install.conf", "r", encoding="utf-8") as installed:
            install1 = str(installed.read())
            if "True" in install1:
                boot()
    except FileNotFoundError:
        install()

if __name__ == "__main__":
    main()

main()