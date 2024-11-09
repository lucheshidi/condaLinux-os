# -*- coding:utf-8 -*-
# name:----------Jyx
# time:----------2023.1.15

from sys import *
from random import *
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, text=True)
    return result

run_command("python -m pip install --upgrade pip>nul")
run_command("python -m pip install pofile>nul")

import pofile


# 系统安装
def install():
    def testSystemInstalled():
        try:
            with open("./usr/systemd/configs/installed.conf") as one:
                pass # 检测系统文件
        except FileNotFoundError:
            print("System Not Installed! Launching Install Program!")

    # 系统安装程序
    def InstallSystem():
        def check():
            print("Conda GNU/Linux Installer")
            # 自检(没用)
            print("checking your CPU ...")
            run_command("ping 127.0.0.1>nul")
            # 报喜讯
            print("Your CPU can install Conda Linux!")
            # 准备资源(没用)
            print("Preparing resources ...")
            run_command("ping 127.0.0.1>nul")
            # 完成
            print("Done!")
        check()
        # 延迟
        run_command("ping 127.0.0.1>nul")
        # 名字和密码
        system_name = str(input("\033[1mPick a name: \033[0m"))
        username = str(input("\033[1mPlease input a username: \033[0m"))
        password = str(input("\033[1mPlease input a password: \033[0m"))
        Verify_password = str(input("\033[1mVerify: "))
        if password != Verify_password: # 密码不对
            print("\033[91m\033[1mERROR: Password Error: password and verify not the same!\033[0m")
            return check()
        root_password = str(input("\033[1mPlease input a password for root: "))
        Verify_root_password = str(input("\033[1mVerify: "))
        if root_password != Verify_root_password: # 梅开二度
            print("\033[91m\033[1mERROR: Password Error: password and verify not the same!\033[0m")
            return check()
        print("Saving Settings ...")
        # 保存设置
        run_command("ping 127.0.0.1>nul")
        pofile.mkdir("./usr/systemd/config/")
        try:
            with open("./usr/systemd/config/user.properties", "w", encoding="utf-8") as this:
                this.write("Name=" + system_name + "\n")
                this.write("Username=" + username + "\n")
                this.write("Username.password=" + password + "\n")
                this.write("Root.password=" + root_password + "\n")
        except FileNotFoundError:
            print("\033[91m\033[1mERROR:Create Config File ERROR: Can't find file\033[0m")

        doInstall = str(input("Would you like to "))



    InstallSystem()

# 系统启动
def system():
    with open("./usr/systemd/config/user.properties", "r", encoding="utf-8") as this:
        pass
    def boot():
        print("condaLinux ")

    boot()
    def SYSTEM():
        pass

    SYSTEM()

# 主函数
def main():
    try:
        with open("./usr/systemd/config/user.properties", "r", encoding="utf-8") as conf:
            print("Launching Installed System ...")
            system()
    except FileNotFoundError:
        install()

if __name__ == "__main__":
    main()