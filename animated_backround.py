import ctypes
import time
import os
import sys

folder="cat"
try:
    if os.path.exists(sys.argv[1]):
        folder=system.sys[1]
        print(folder)
except (IndexError):
        pass

print("running")
with open(f"frames/{folder}/config.txt",'r') as f:
    lines=f.readlines()
    try:
        interval=float(lines[0])
        number_of_files=int(lines[1])
        file_type=lines[2]
    except (ValueError,IndexError):
        print("config.txt error: not in right format. it needs to be time between frames for the first number,the number of the last image in the second, and the file type of the images in the third")
    except Exception as e:
        print(f"other error: {e}")

while True:
     for i in range(0,number_of_files+1):
         ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.abspath(f"frames/{folder}/{i}.{file_type}"), 0)
         time.sleep(interval)
         #print(i)

