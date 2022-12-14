import os
devicename=str(os.system("adb devices -l"))
print(str(devicename).replace(" ",","))