<<<<<<< HEAD
import os, platform, ctypes

def get_free_space_mb(folder):
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(folder), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024 / 1024
    else:
        st = os.statvfs(folder)
        return st.f_bavail * st.f_frsize / 1024 / 1024


if __name__ == '__main__':
    print(get_free_space_mb("D:"), 'GB')
=======
# -*- coding:utf-8 -*-
# name:----------Jyx
# time:----------2023.1.15

import SCM
>>>>>>> 22cc729e87fe7714565ee99ac764593f7b14c01b
