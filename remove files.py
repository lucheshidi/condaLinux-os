# -*- coding:utf-8 -*-
# name:----------Jyx
# time:----------2023.1.15
import pofile
import shutil
import time

def main():
    confirm = str(input("Confirm?[Y/n] "))
    if confirm == "y" or confirm == "Y":
        try:
            # 进度条功能
            import time

            for i in range(20):
                print("\r" + "■" * i, sep="", end="")
                time.sleep(0.35)
            shutil.rmtree("./usr/")
            print("Delete /usr/ and the tree ...")
            shutil.rmtree("./root/")
            print("Delete /root/ and the tree ...")
            shutil.rmtree("./home/")
            print("Delete /home/ and the tree ...")
            shutil.rmtree("./etc/")
            print("Delete /etc/ and the tree ...")
            shutil.rmtree("./dev/")
            print("Delete /dev/ and the tree ...")
            print("Delete success")
        except FileNotFoundError:
            print("\nFiles and folders is deleted!")
            time.sleep(3)

    else:
        print("exiting program ...")
        return

if __name__ == "__main__":
    main()