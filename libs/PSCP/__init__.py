from sys import *
from random import *
import platform
import os

path = str(os.getcwd())

# check cpu
def cpuChecker(best_cpu, worst_cpu):
    machine_cpu = platform.processor()
    print(machine_cpu)
    return machine_cpu

cpuChecker("i5")

# check Memory
def memoryChecker(max, mix):
    pass

# check disk
def diskChecker(max, mix):
    pass