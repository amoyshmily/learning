

# 修复逍遥模拟器无法通过adb devices查看设备的问题

```
解决方案：替换adb.exe文件

具体步骤：将android sdk的platform-tools中复制adb.exe文件，复制到逍遥模拟器程序安装目录\\Microvirt\MEmu目录中，覆盖逍遥自带的adb.exe程序。

```