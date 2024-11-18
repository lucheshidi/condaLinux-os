from sys import *
from random import *
<<<<<<< HEAD
import subprocess
=======
from subprocess import *
>>>>>>> 22cc729e87fe7714565ee99ac764593f7b14c01b
import platform
import os
import shutil

def run_command(command):
    result = subprocess.run(command, shell=True, text=True)
    return result

<<<<<<< HEAD
# run_command("pip install --upgrade pip>")
# run_command("pip install psutil>")
# run_command("pip install shutil")
=======
run_command("python -m pip install --upgrade pip")
run_command("python -m pip install psutil")
>>>>>>> 22cc729e87fe7714565ee99ac764593f7b14c01b

import psutil

mem = psutil.virtual_memory()
path = str(os.getcwd())

# print ver
def printVer():
<<<<<<< HEAD
    # print("System Check Program v1.15.33")
    # print("Preparing to check ...")
=======
    print("System Check Program v1.15.33")
    print("Preparing to check ...")
>>>>>>> 22cc729e87fe7714565ee99ac764593f7b14c01b
    time.sleep()

# check cpu
def cpuChecker(best_cpu, worst_cpu):
    machine_cpu = platform.processor()
    if best_cpu in machine_cpu or worst_cpu in machine_cpu:
        return False
    else:
        return True

# check Memory
<<<<<<< HEAD
def memoryChecker(mix=2):
    total_memory = mem.total / (1024 ** 3)
    used_memory = mem.used / (1024 ** 3)
    free_memory = mem.available / (1024 ** 3)

    if mix <= free_memory:
        return True

    else:
        return False
=======
def memoryChecker(total, available):
    total_memory = mem.total / (1024 ** 3)
    used_memory = mem.used / (1024 ** 3)
    available_memory = mem.available / (1024 ** 3)
>>>>>>> 22cc729e87fe7714565ee99ac764593f7b14c01b

# check disk
def diskChecker(mix=10):

    # 定义 GB 的大小
    gb = 1024 ** 3

    # 获取磁盘使用情况
    total_b, used_b, free_b = shutil.disk_usage('E:')

    # 打印结果
    total = float(format(total_b / gb))
    used = float(format(used_b / gb))
    free = float(format(free_b / gb))

    if mix <=free:
        return True

    else:
        return False



diskChecker()