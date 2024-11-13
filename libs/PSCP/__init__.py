from sys import *
from random import *
from subprocess import *
import platform
import os

def run_command(command):
    result = subprocess.run(command, shell=True, text=True)
    return result

run_command("python -m pip install --upgrade pip")
run_command("python -m pip install psutil")

import psutil

mem = psutil.virtual_memory()
path = str(os.getcwd())

# print ver
def printVer():
    print("System Check Program v1.15.33")
    print("Preparing to check ...")
    time.sleep()

# check cpu
def cpuChecker(best_cpu, worst_cpu):
    machine_cpu = platform.processor()
    if best_cpu in machine_cpu or worst_cpu in machine_cpu:
        return False
    else:
        return True

# check Memory
def memoryChecker(total, available):
    total_memory = mem.total / (1024 ** 3)
    used_memory = mem.used / (1024 ** 3)
    available_memory = mem.available / (1024 ** 3)

# check disk
def diskChecker(max, mix):
    pass