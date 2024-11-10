# -*- coding:utf-8 -*-
# name:----------Jyx
# time:----------2023.1.15
import time
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

    testSystemInstalled()

    # 系统安装程序
    def InstallSystem():
        def check():
            print("Conda GNU/Linux Installer")
            # 自检(没用)
            print("checking your CPU ...")
            time.sleep(10)
            # 报喜讯
            print("Your CPU can install Conda Linux!")
            # 准备资源(没用)
            print("Preparing resources ...")
            time.sleep(5)
            # 完成
            print("Done!")
        check()
        # 延迟
        time.sleep(3)
        # 名字和密码
        system_name = str(input("\033[1mPick a name: \033[0m"))
        username = str(input("\033[1mPlease input a username: \033[0m"))
        password = str(input("\033[1mPlease input a password: \033[0m"))
        Verify_password = str(input("\033[1mVerify: "))
        if password != Verify_password: # 密码不对
            print("\033[91m\033[1mERROR: Password Error: password and verify not the same!\033[0m")
            return check()
        def input_root_password():
            root_password = str(input("\033[1mPlease input a password for root: "))
            Verify_root_password = str(input("\033[1mVerify: "))
            if root_password != Verify_root_password:  # 梅开二度
                print("\033[91m\033[1mERROR: Password Error: password and verify not the same!\033[0m")
                return check()

        input_root_password_v = str(input("Would you like to set \"root\" user password?[Y/n] "))
        if input_root_password_v == "y" or input_root_password_v == "Y":
            input_root_password()
        elif input_root_password_v == "n" or input_root_password_v == "N":
            print("User not want to input, next step ...")
        else:
            print(f"Input ERROR: Unknown input: {input_root_password_v}")
        print("\033[0mSaving Settings ...")
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

        def doInstallNow():
            doInstall = str(input("\033[0mWould you like to install system now ?[Y/n] "))
            # 是否现在安装系统
            if doInstall == "n" or doInstall == "N":
                print("User closed, shutting down...")
                time.sleep(2)
                return
            elif doInstall == "y" or doInstall == "Y":
                print("SYSTEM WILL BE INSTALL NOW!")
                time.sleep(5)
                print("Create Files ...")
                # 创建文件夹和文件
                pofile.mkdir("./usr/Application/")
                pofile.mkdir("./home/" + username + "/")
                pofile.mkdir("./root/")
                pofile.mkdir("./etc/services")
                pofile.mkdir("./etc/network/")
                network_config = open("./etc/network/network.conf", "w", encoding="utf-8")
                pass # 创建文件
                network_config.close()
                pofile.mkdir("./dev/")
                print("System Install SUCCESS!")
                time.sleep(1)
                def reboot():
                    reboot1 = str(input("Would you like to reboot now? [Y/n] "))
                reboot()
                if reboot1 == "y" or reboot == "Y":
                    return main()
                elif reboot1 == "n" or reboot == "N":
                    print("User disagree, shutting down ...")
                    time.sleep(3)
                    return
                else:
                    print("input error, Please try again ...")
                    return reboot()
            else:
                print("input error, Please try again ...")
                return doInstallNow()
        doInstallNow()
    InstallSystem()

# 系统启动
def system():
    try:
        with open("./usr/systemd/config/user.properties", "r", encoding="utf-8") as this:
            # 解析各行
            content = this.readlines()
            name = content[0].strip().split("=")[1] if "Name=" in content[0] else ""
            username = content[1].strip().split("=")[1] if "Username=" in content[1] else ""
            password = content[2].strip().split("=")[1] if "Username.password=" in content[2] else ""
            root_password = content[3].strip().split("=")[1] if "Root.password=" in content[3] else ""

            # 输出检查
            # print("Name:", name)
            # print("Username:", username)
            # print("Password:", password)
            # print("Root Password:", root_password)
    except FileNotFoundError:
        print("ERROR: File Not Found")

    def SYSTEM(root = False):
        if not root:
            while True:
                command = str(input(f"{username}-%-{name}:[~]-$ "))
                if command == "shutdown":
                    return
                elif command == "exit":
                    return boot()
        elif root:
            while True:
                command = str(input(f"root-%-{name}:[~]-# "))
                if command == "shutdown":
                    return
                elif command == "exit":
                    return boot()
        else:
            print("SYSTEM ERROR")
            time.sleep(1)
            return
    def boot():
        print("condaLinux system tty1")
        test_username = str(input(name + " login: "))
        test_password = str(input("Password: "))
        # 错误次数
        error = int(0)

        if test_username == username and test_password == password:
            SYSTEM(root=False)
        elif test_username != username or test_password != password:
            print("ERROR, try again ...")
            error += 1
            if error == 10:
                print("Can't Login, shutting down ...")
                time.sleep(3)
                return
        elif test_username == "root" and test_password == root_password:
            SYSTEM(root = True)
    boot()

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