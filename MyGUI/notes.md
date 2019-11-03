#### 在Pycharm中添加Designer扩展工具

```
第一步：打开Pycharm，点击新增扩展工具。菜单路径：File/Settings/Tools/External Tools/+

第二步：配置参数

name:QtDesigner
Description:QtDesigner
Program:D:\Programs\Anaconda3\Library\bin\designer.exe
Working directory: $ProjectFileDir$
备注：designer程序在anaconda中的目录是Anaconda3\Library\bin\designer.exe
```


#### 在pycharm中配置pyuic扩展工具

```
第一步：打开Pycharm，点击新增扩展工具。菜单路径：File/Settings/Tools/External Tools/+

第二步：配置参数

name:pyuic5
Description:pyuic5
Program:D:\Programs\Anaconda3\python.exe
Arguments: -m PyQt5.uic.pyuic $FileName$ -o $FileNameWithoutExtension$.py
Working directory: $FileDir$

```


#### .ui转换成.py
方法一：使用命令行
```
python -m PyQt5.uic.pyuic test.ui -o test.py

```

方法二：直接使用pyuic
```
命令程序所在路径：

\Anaconda3\pkgs\pyqt-5.9.2-py37h6538335_2\Library\bin
```
