
### PyQt5开发环境配置
```
（1）pyqt5库

命令行：
pip install pyqt5

使用豆瓣镜像：pip install -i https://pypi.doubanio.com/simple pyqt5

官网下载地址：https://pypi.org/project/PyQt5/#files

当前版本：5.13.2

简介：
Qt is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of 
modern desktop and mobile systems. These include location and positioning services, multimedia, NFC and 
Bluetooth connectivity, a Chromium based web browser, as well as traditional UI development.
PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension 
modules and enables Python to be used as an alternative application development language to C++ on all 
supported platforms including iOS and Android.
PyQt5 may also be embedded in C++ based applications to allow users of those applications to configure 
or enhance the functionality of those applications.

（2）pyqt5_tools

命令行：
pip install pyqt5-tools

官网下载地址：
https://pypi.org/project/pyqt5-tools/#files

当前版本：5.13.0.1.5

简介：
The PyQt5 wheels do not provide tools such as Qt Designer that were included in the old binary installers. 
This package aims to provide those in a separate package which is useful for developers while the official 
PyQt5 wheels stay focused on fulfilling the dependencies of PyQt5 applications.

```


### Pycharm扩展工具

> Designer扩展工具

```
第一步：打开Pycharm，点击新增扩展工具。菜单路径：File/Settings/Tools/External Tools/+

第二步：配置参数

name:QtDesigner
Description:QtDesigner
Program:D:\Programs\Anaconda3\Library\bin\designer.exe
Working directory: $ProjectFileDir$
备注：designer程序在anaconda中的目录是Anaconda3\Library\bin\designer.exe
```


> pyuic扩展工具

```
第一步：打开Pycharm，点击新增扩展工具。菜单路径：File/Settings/Tools/External Tools/+

第二步：配置参数

name:pyuic5
Description:pyuic5
Program:D:\Programs\Anaconda3\python.exe
Arguments: -m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
Working directory: $FileDir$

```


### .ui转换成.py
方法一：使用命令行
```
python -m PyQt5.uic.pyuic test.ui -o test.py

```

方法二：直接使用pyuic
```
命令程序所在路径：

\Anaconda3\pkgs\pyqt-5.9.2-py37h6538335_2\Library\bin
```



### GUI工程打包
```

pip install pyinstaller


pyinstaller -Fw XX.py

-w:不显示终端控制台
-F:将所有的依赖库打包成一个单独的文件

```