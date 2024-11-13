# -*- coding:utf-8 -*-
# name:----------Jyx
# time:----------2023.1.15
import time
from sys import *
from random import *
import subprocess

import libs.PSCP
from libs.PSCP import *

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
        global var

        # 创建依赖库
        def createLibs():
            pofile.mkdir("./libs/PSCP")
            try:
                with open("./libs/PSCP/__init__.py", "w", encoding="utf-8") as this:
                    this.write("""from sys import *
from random import *
import platform
import os

path = str(os.getcwd())

# check cpu
def cpuChecker(cpu):
    machine_cpu = platform.processor()
    print(machine_cpu)
    return machine_cpu

cpuChecker("i5")

# check Memory
def memoryChecker(max, mix):
    pass""")

                with open("./libs/PSCP/LICENSE", "w", encoding="utf-8") as this:
                    this.write("""Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.""")
            except FileNotFoundError:
                print("ERROR: Install Program ERROR")


        # 系统自检
        def check():
            print("Conda GNU/Linux Installer")
            # 自检(没用)
            print("checking your CPU ...")
            # time.sleep(10)
            # # 报喜讯
            success = bool(libs.PSCP.cpuChecker("Intel64", "Intel32"))
            if success:
                print("Your CPU can install Conda Linux!")
            else:
                return
            # 准备资源(没用)
            print("Preparing resources ...")
            time.sleep(5)
            # 完成
            print("Done!")
        check()
        # 创建用户信息配置文件
        pofile.mkdir("./usr/systemd/config")
        with open(file="./usr/systemd/config/user.properties", mode="w", encoding="utf-8") as this:
            pass # 不要动这行
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
            pofile.mkdir("./usr/systemd/config/")

        input_root_password_v = str(input("Would you like to set \"root\" user password?[Y/n] "))
        if input_root_password_v == "y" or input_root_password_v == "Y":
            time.sleep(3)
            try:
                with open("./usr/systemd/config/user.properties", mode="a", encoding="utf-8") as this:
                    this.write("Name=" + system_name + "\n")
                    this.write("Username=" + username + "\n")
            except FileNotFoundError:
                print("\033[91m\033[1mERROR:Create Config File ERROR: Can't find file\033[0m")

            input_root_password()
        elif input_root_password_v == "n" or input_root_password_v == "N":
            time.sleep(3)
            try:
                with open("./usr/systemd/config/user.properties", mode="a", encoding="utf-8") as this:
                    this.write("Name=" + system_name + "\n")
                    this.write("Username=" + username + "\n")
            except FileNotFoundError:
                print("\033[91m\033[1mERROR:Create Config File ERROR: Can't find file\033[0m")

            print("\033[0mUser not want to input, next step ...")
        else:
            print(f"\033[91m\033[1mInput ERROR: Unknown input: {input_root_password_v}")
        print("\033[0mSaving Settings ...")
        # 保存设置
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
                    if reboot1 == "y" or reboot == "Y":
                        return main()
                    elif reboot1 == "n" or reboot == "N":
                        print("User disagree, shutting down ...")
                        time.sleep(3)
                        return
                    else:
                        print("input error, Please try again ...")
                        return reboot()
                reboot()
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
        
    # 系统引导
    def boot():
        print("")
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