import os
import subprocess
import time

os.chdir(r"your adb drivers path")
os.system("adb tcpip 5555")
os.system("adb connect 'your android tv ip'")

time.sleep(3)
subprocess.call(r"you scrcpy.exe path")
