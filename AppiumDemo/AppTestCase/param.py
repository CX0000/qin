import os

PlatformName="Android"
PlatformVersion=str(os.system('adb -s 127.0.0.1:62001 shell getprop ro.build.version.release'))
DeviceName="127.0.0.1:62001"
App="C:\\Users\\apple\\Desktop\\xueqiu.apk"
NoReset=True
AppPackage="com.xueqiu.android"
AppActivity=".main.view.MainActivity"