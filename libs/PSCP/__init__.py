from sys import *
from random import *
import subprocess
import platform
import os
import shutil

def run_command(command):
    result = subprocess.run(command, shell=True, text=True)
    return result

# run_command("pip install --upgrade pip>")
# run_command("pip install psutil>")
# run_command("pip install shutil")

import psutil

mem = psutil.virtual_memory()
path = str(os.getcwd())

# print ver
def printVer():
    # print("System Check Program v1.15.33")
    # print("Preparing to check ...")
    time.sleep()

# check cpu
def cpuChecker(best_cpu, worst_cpu):
    machine_cpu = platform.processor()
    if best_cpu in machine_cpu or worst_cpu in machine_cpu:
        return False
    else:
        return True

# check Memory
def memoryChecker(mix=2):
    total_memory = mem.total / (1024 ** 3)
    used_memory = mem.used / (1024 ** 3)
    free_memory = mem.available / (1024 ** 3)

    if mix <= free_memory:
        return True

    else:
        return False

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