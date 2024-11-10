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
            shutil.rmtree("./usr/")
            print("Delete /usr/ and the tree ...")
            shutil.rmtree("./root/")
            print("Delete /root/ and the tree ...")
            shutil.rmtree("./home/")
            print("Delete /home/ and the tree ...")
            shutil.rmtree("./etc/")
            print("Delete /etc/ and the tree ...")
            print("delete success")
        except FileNotFoundError:
            print("Files and folders is deleted!")
            time.sleep(3)

    else:
        print("exiting program ...")
        return

if __name__ == "__main__":
    main()