# 一、简介

#### 定义
```
Python是一种面向对象、解释型、弱类型的脚本语言。
```

#### 常用内置方法
```
help()：查看说明文档
help(list)


dir()

print('cifer', 18, end='')

```

# 二、变量

#### 注释
解释程序某些部分的作用和功能，给人看的。
> 单行注释
```
# 单行注释以#号开头
```

> 多行注释
```
'''
多行注释就是一次性将程序中
的多行代码注释掉
'''

"""
可以用三个单引号，也可以
使用三个双引号。
"""
```


#### 变量

> 释义
```
变量就像一个小容器，用来存放程序中的数据。
python中的变量特点：直接赋值、动态改变。
```


> 变量VS常量
```
常量一旦保存某个数据后，该数据不能发生改变。变量保存的数据则可以多次发生改变。
```

> 赋值
```
使用=号进行变量赋值。例如 a = 1, msg="Hello world!"
```

> 命名规则
```
python需要使用标识符给变量命名。规则：
1.必须以字母、下划线开头，后面可以跟任意数目的字母、文字、数字和下划线。
2.区分大小写
3.不能使用关键字，如type,None,pass,with等
```


# 三、数据类型（6种）

```
Python3 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。


【序列Sequence】
一种包含多项数据的数据结构，序列的元素按照顺序排列，并且可以通过索引进行访问。常见的
序列有字符串、元祖、列表等。

# 序列封包
程序将多个值，赋值给一个变量时，Python会自动将多个值封装成元祖。
注意：封包后的变量的数据类型一定是元祖。
num = 10, 20, 30
print(type(num))    # <class 'tuple'>


# 序列解包
程序将序列（元祖/列表）直接赋值给多个变量，此时序列的各个元素就会被一次赋值给每个变量。要求序列的
元素个数与变量个数完全相同。
tup = (10, 20, 30)      # 解包支持分解元祖
a, b, c = tup  
print(c)    # 30

li = ['a', 'b', 'c']    # 解包支持分解列表
x, y, z = li
print(y)

# 利用封包和解包机制进行批量赋值
x, y, z = 1, 2, 3
过程等同于：
my_tup = 1, 2, 3    # (1, 2, 3)
x, y, z = my_tup    # x=1,y=2,z=3


# 部分解包
在序列解包时，也可以只解出部分元素，包内剩下的元素当做一个整体列表保存。具体做法是在
变量之前添加星号*，则代表该变量时一个列表，就能保存多个元素。
注意：部分解包后的整体变量部分的数据类型一定是列表。
tup = (1, 2, 3, 4, 5, 6, 7, 8)
x, y, *z = tup
print(x)    # 1
print(y)    # 2
print(z)    # [3, 4, 5, 6, 7, 8]

li = ['I', 'l', 'o', 'v', 'e', 'U']
a, *b, c = li
print(a)    # I
print(b)    # ['l', 'o', 'v', 'e']
print(c)    # U


【区间range】

range()：可创建一个整数列表

语法：range(start, stop, step)
start：计数从start开始，默认是从0开始，允许是负数。例如range(5)等价于range(0,5)；
stop：计数到stop为止，但不包括stop自身，允许是负数。例如：range(0,3)表示[0,1,2]，不包含3；
step：步长，默认为1。例如range(0,3)等价于range(0,3,1)

示例1
data = range(10)
print(type(data))   # <class 'range'>
print([x for x in data])    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

示例2
data = range(2, 10, 2)
print([x for x in data])    # [2, 4, 6, 8]

示例3
data = range(-10, 2, 3)
print([x for x in data])    # [-10, -7, -4, -1]

示例4
s = 'Python'
for i in range(len(s)):
	print(s[i])
	
>>>
P
y
t
h
o
n

```

## 3.1 Number 数字

```
Python3 支持 int、float、bool、complex（复数）。
```


#### 整型 int


> 整型的4种表示形式
```
1.十进制形式：如0~9
2.二进制形式：以0b或0B开头的整数。
3.八进制形式：以0o或0O开头的整数。
4.十六进制形式：以0x或0X开头的整数（其中10~15分别以a~f表示，不区分大小写）
```

> 分隔符
```
Python 3 允许为了提高可读性，允许给数值(包括浮点数)增加下划线作为分隔符，不会影响数值本身。
例如：million = 1_000_000
```


#### 浮点型 float

用于保存带小数的数值。


> 浮点数的2种表示形式
```
1.十进制形式：例如3.14
2.科学计数法：如5.12e2等同于5.12×10²。
```


#### 布尔型 bool
```
True/False

```


#### 复数 complex
```
太过深奥，略过
```

## 3.2 String 字符串

> 定义
```
使用单引号或者双引号包围的一串字符。

例如：'hello'和"I'm fine"都是字符串。
```

> 转义
```
Python中使用反斜杠\将字符串中的特殊字符进行转义。
例如：msg = 'I\'m a student'

还可以转义换行符。
例如：
worlds = 'There are so many \
    stories that I want to \
    share with you.
    '
    
常见的转义字符：
\b表示：退格符
\n表示：换行符
\r表示：回车符
\t表示：制表符
\"表示：双引号
\'表示：单引号
\\表示：反斜杠


```

> 原始字符串
```
由于反斜杠\自身拥有特殊意义，一旦字符串中必须使用\时，必须对其进行转义。

例如Windows系统的路径C:\windows\System32，转义后的普通写法是：path = 'C:\\windows\\System32'。
但是这种处理方式显得非常繁琐。

原始字符串以r开头，原始字符串不会把反斜杠当成特殊字符。
上述路径可以写为 path = r'C:\\windows\\System32'

```

> 拼接
```
1. 字符串和字符串拼接
Python3允许使用加号+作为字符串之间的拼接运算符。
msg = 'hello' + 'world'
print(msg)

2. 字符串和数值拼接
Python3不允许直接拼接字符串和数值，必须将数值转换成字符串后才可以执行拼接操作。可以通过str()
或者repr()函数来将数值转成字符串。
s = 'my score is '
n = 100
msg1 = s + str(n)
msg2 = s + repr(n)
```

> 长字符串
```
如果将多行注释形式的内容赋值给变量，那么就是一个长字符串，并且不会被解释器忽略。多行文本中
记得及时添加转义符\对换行符进行转义。

例如：
worlds = 'There are so many \
    stories that I want to \
    share with you.
    '
```

> 格式化
```
1. 占位符 %

转换说明符：
d,i：    转换为带符号的十进制形式的整数
o：      转换为带符号的八进制形式的整数
x,X：    转换为带符号的十六进制形式的整数
e,E：    转化为科学计数法表示的浮点数
f,F：    转化为十进制形式的浮点数
g：      智能选择使用f或者e格式
G：      智能选择使用F或者E格式
C：      转换为单字符（只接受整数或单字符字符串）
r：      使用repr()将变量或表达式转换为字符串
s：      使用str()将变量转换为字符串

宽度：在占位符中添加数字n可以指定转换后的最小宽度为n。默认对齐方式是右对齐，默认左侧补位方式是空格。
例如：'%6d' % 10 表示 “    10”

标志：
-：指定转换结果的对齐方式为左对齐，指定后左侧补位失效。
+：表示数值一定带着符号（正数带正号“+”，负数带负号“-”）
0：表示数值的补位方式是0，仅对左侧有效。

示例：
num = 99
s1 = '得分: %06d 分' % num # 最小宽度6，补位0
s2 = '得分: %+06d 分' % num # 最小宽度6，显示正负号，补位0
s3 = '得分: %-6d 分' % num # 最小宽度6，左对齐
s4 = '我%-6s你' % '爱'

>>>
得分: 000099 分
得分: +00099 分
得分: 99     分
我爱     你

精度：
对于转换浮点数，允许指定小数点后的数字位数。如果转换的是字符串，则允许指定换换后最大的字符数。这个
标志称为精度值。精度标志被放置在最小宽度之后，中间用点号.隔开。

value = 3.1415926
s1 = '最小宽度8，保留3位小数：%8.2f' % value
s2 = '最小宽度6，只保留3个字符：%6.3s' % '我爱你Python'

>>>
最小宽度8，保留3位小数：    3.14
最小宽度6，只保留3个字符：   我爱你

# 使用字典来批量格式化
msg = '姓名：%(name)s , 年龄：%(age)d , 体重：%(weight).1f 公斤'
cifer = {'age': 18, 'name': 'cifer', 'weight': 66.5}
print(msg % cifer)  # 姓名：cifer , 年龄：18 , 体重：66.5 公斤


2. 函数 format()
```


> 操作
```
1.索引
字符串本质上就是由多个字符组成，因此可以通过索引来操作字符串。字符串直接在方括号[]中
使用一个索引即可获得对应的单个字符，格式为s[m]。

索引支持正序和逆序。正序时索引值为正数，从0开始；逆序时索引值为负数，从-1开始。


2.切片
在方括号中使用两个索引来获取字符串中的一段字符，格式为s[m:n]。其中n要大于m，否则获取为空字符。
s = 'hello world'
s1 = s[2:6]     # llo 
s2 = s[-3:-1]   # rl



切片时允许省略起始索引或结束索引。如果省略起始索引，默认起始位置为字符串的开头；
如果省略结束索引，默认结束位置为字符串的结尾。
s = 'hello world'

s1 = s[2:]  # llo world
s2 = s[:-2] # hello wor
s3 = s[:]   # hello world


3.成员检测
支持使用in运算符判断字符串是否包含某个字符或者子串。
s = 'hello world'

flag1 = 'x' in s        # False
flag2 = 'hello' in s    # True


4.长度
使用Python内置函数len()获取字符串长度。
s = 'hello world'
l = len(s)      # 11

5.极值
使用Python内置函数max()和min()函数即可获取字符串中的最大字符和最小字符。

s1 = 'hello world'
s2 = '1234'

print(max(s1))  # w
print(max(s2))  # 4

6.大小写
title():将每个单词的首字母转成大写，其他字母不变。
upper():将整个字符串转成大写。
lower():将整个字符串改成小写。

s = 'hello world WOW'

print(s.title())    # Hello World Wow
print(s.upper())    # HELLO WORLD WOW
print(s.lower())    # hello world wow

7.删除空白
strip():返回删除字符串前后空白的新字符串。
lstrip():返回删除字符串左侧空白之后的新字符串。
rstrip():返回删除字符串右侧空白之后的新字符串。


8.查找
startswith():判断字符串是否以指定的子串开头。
endswith():判断字符串是否以指定的子串结尾。
find():查找指定子串在字符串中出现的位置索引。如果没有找到子串，则返回-1。
index():查找指定子串在字符串中出现的位置索引。如果没有找到子串，则引发ValueError错误。

9.替换
replace():使用指定子串来替换字符串中指定字符。
translate():使用指定的翻译映射表对字符串执行替换。

注意：翻译映射表不能直接使用字符本身，必须使用字符的编码。
maketrans():快速创建翻译映射表。
table = str.maketrans('hel', '123')
print(table)    # {97: 49, 98: 50, 99: 51}

s = 'hello world'
print(s.translate(table))   # 1233o wor3d

10.分割
split():将字符串按照指定的分割符进行分割，返回成多个子串组成的列表。

示例：
s = 'hello,world'
li = s.split(',')   # ['hello', 'world']

11.拼接
join():使用连接符，将迭代对象中的字符串拼接成一个字符串。

示例：
s1 = ','.join('hello')  # h,e,l,l,o

s2 = ','.join(['hello', 'world'])   # hello,world
``` 

## 3.3 Tuple 元祖 ()

> 定义
```
有序，允许重复，元素不可变。元素的数据类型支持数字、字符串和序列等，支持嵌套。是序列的一种形式。
```

> 实例化
```
创建元祖时使用圆括号（小括号），并在括号中列出元祖的元素。元素之间用英文逗号隔开。
t1 = (1,)      # <class 'tuple'>
注意：哪怕只有一个元素的元祖也必须加上逗号。

t2 = (1, 1, 2, 'Hello World')   # <class 'tuple'>

# 封包
t3 = 1, 2, 3    # 利用封包机制    <class 'tuple'>

# 嵌套
t4 = (1, 1, 2, (3, 2, 1), 'Hi')  # <class 'tuple'>

# 转换函数
li = [1, 2, 3]
t5 = tuple(li)  # (1, 2, 3)

t6 = tuple(range(0, 10))    # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


反例：
t0 = (1)    # 这种写法跟t2 = 1 是一样的效果。
print(type(t0)) # <class 'int'>
```

> 访问
```
（1） 访问单个元素
语法：[index]，返回元素值。

元祖可以通过索引来访问元素。索引值默认从0开始，第一个元素的索引值是2，以此类推；索引支持
负数，倒数第一个元素的索引值为-1，倒数第二个元素的索引值是-2，以此类推。

元祖的元素相当于常量，只能使用它的值，不能对它重新赋值。

my_tuple = (0,99,'hello', 'world')
print(my_tuple[1])      # 99
print(my_tuple[-1])     # world


（2） 访问多个元素：切片
完整语法：[start:end:step]，返回一个元祖。

语法中的start和end两个索引值都可以使用正数或者负数，表示收集从start索引的元素开始（包含），直到
end索引的元素结束（不包含）的所有元素。step表示步长（间隔），使用负数无意义。

my_tuple = (0, 'hello', 'world', 99, 'cifer', 'python', 'java')

tup1 = my_tuple[2:4]    # 获取索引从2到4（不含）的所有元素 ('world', 99)
tup2 = my_tuple[-4:-2]  # 获取索引从-4到-2（不含）的所有元素 (99, 'cifer')
tup3 = my_tuple[2:5:2]  # 获取索引从2到5（不含）且间隔为2的所有元素 ('world', 'cifer')

```

> 算术运算
```
（1）加法 ()+()
元祖支持加法运算，加法的和是两个元祖所包含元素的合集。

tup1 = (1,2,3)
tup2 = (3, 'hi', 'python')
tup3 = tup1+tup2    # (1, 2, 3, 3, 'hi', 'python')

（2）乘法 ()*N
元祖可以乘以倍数N（整数），意义就是把她们包含的元素重复N次。

```

> 成员检测
```
使用in运算符来判断元祖是否包含某个元素。

tup = (1, 2, 3, 3, 'hi', 'python')
flag1 = 'python' in tup     # True
flag2 = 'java' in tup      # False
```

> 统计
```
元素要求：元素必须是相同数据类型并且可以比较大小，否则会报错。支持对数字和字符串的比较。
如果比较的是字符串，则依次按照字符串中的每个字符对应的编码来比较字符串的大小。

tup1 = (1, 2, 3, 3, 99, -2)  # 元素一律为数字
tup2 = ('A', 'Hi', 'HI', 'world')   # 元素一律为字符串
tup3 = ('我', '爱', '你')
tup4 = ('我爱你'）

（1）个数 len()
num = len(tup1)  # 6

(2)最大值 max()
max1 = max(tup1)  # 99
max2 = max(tup2)    # world
max3 = max(tup3)    # 爱
max4 = max(tup4)    # 爱

（3）最小值 min()
min1 = min(tup1)  # -2
min2 = min(tup2) # A
min3 = min(tup3)    # 你
min4 = min(tup4)    # 你

```

## 3.4 List 列表 []

> 定义
```
有序，允许重复，元素可变。是序列的一种。
```

> 实例化
```
# 直接赋值
L1 = [1, 2, 3, 'Hello', (1,2,3), ['a', 'b', 'c'], '列表']

# 函数
L2 = list(range(0,10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

tup = (1, 2, 3)
L3 = list(tup)  # [1, 2, 3]

L4 = list(i for i in range(0, 10, 2))   # [0, 2, 4, 6, 8]

```

> 访问
```
跟元祖一样。支持索引和切片。
```

> 算术运算
```
跟元祖一样。支持加法和乘法（倍数）。
```

> 成员检测
```
跟元祖一致。使用in运算符判断是否包含。
```

> 统计
```
跟元祖一致。支持len()函数求个数,max()函数求最大值，min()函数求最小值。
```

> 增删改查
```
（1）增
append()方法：单个添加。支持传入单个值，也可以接收元祖和列表对象，会把传入的元素当做一个整体
追加到列表的最后面。

L = [1, 2, 3]
L.append(99)    # [1, 2, 3, 99]
L.append(['a', 'b', 'c'])   # [1, 2, 3, 99, ['a', 'b', 'c']]
L.append(('x', 'y'))    # [1, 2, 3, 99, ['a', 'b', 'c'], ('x', 'y')]

extend()方法：批量追加。仅支持元素集，不支持单个值。此时不会把元素集当成给一个整体，
会追加元素集中的元素。
L = [1, 2]
L.extend(range(4,7))    # [1, 2, 4, 5, 6]
L.extend(['a', 'b'])    # [1, 2, 4, 5, 6, 'a', 'b']
L.extend(('X', 'Y'))    # [1, 2, 4, 5, 6, 'a', 'b', 'X', 'Y']
L.extend({'爱江山','爱美人'})   # [1, 2, 4, 5, 6, 'a', 'b', 'X', 'Y', '爱江山', '爱美人']

insert()方法：插入。在列表的指定位置追加元素。

（2）删
del()方法：支持单个删除，也支持批量删除。

L = [1, 2, 3, 'a', 'b', 'c', '中国','废青']
del(L[-1])
print(L)    # [1, 2, 3, 'a', 'b', 'c', '中国']
del(L[2:6:2])
print(L)    # [1, 2, 'a', 'c', '中国']

remove()方法：根据元素本身来删除，并且只删除第一个找到的元素。如果需要删除的元素不存在，则会
引发ValueError错误。
L = [1, 'a', 'a', 'b']
L.remove('a')
print(L)    # [1, 'a', 'b']

clear()：删除所有全部，清空列表。
L = [1, 'a', 'a', 'b']
L.clear()
print(L)    # []

（3）改
列表的元素相当于变量，因此对其中元素的赋值即为修改元素。

（4）查
等同于访问元素。

```

> 常用方法
```
# count():统计某个元素在列表中出现的次数。

# index():获取某个元素在列表中的索引位置。
如果元素不存在，则引起ValueError错误。

# pop():末尾元素出栈，实现先入后出FILO。

# reverse():将列表元素顺序反转。

# sort():将列表元素排序。
默认从小到大排列。对于字符，则按字符串包含的字符的编码从小到大排列。
sort()支持使用关键字参数key和reverse来执行特定排序。其中key参数值为比较函数对象，reverse
参数值为布尔值，True代表反转（由大到小），False表示不反转（默认由小到大）。

L = ['Java', 'Python', 'R', 'Swift', 'Go', 'Ruby']
L.sort()    
print(L)    # ['Go', 'Java', 'Python', 'R', 'Ruby', 'Swift']
L.sort(key=len, reverse=True)
print(L)    # ['Python', 'Swift', 'Java', 'Ruby', 'Go', 'R']

```

## 3.5 Set 集合 {}
> 定义
```
无序的，不重复元素集合。适用于数据集的逻辑运算。
```

> 实例化
```
# 直接赋值
set1 = {1, 2, 3}
print(type(set1))   # <class 'set'>
注意：不要直接用{}，因为空的花括号表示空的字典。

# 函数
set2 = set()   # 空集合

set3 = set('hello')
print(type(set3))   # <class 'set'>
print(set3)     # {'o', 'e', 'h', 'l'}

set4 = set([1, 2, 'Python'])
print(set4)     # {1, 2, 'Python'}

# 推导式
set5 = {x for x in range(5)}
print(set5) # {0, 1, 2, 3, 4}

set6 = {s for s in 'hello'}
print(set6) # {'e', 'l', 'o', 'h'}
```

> 算术运算
```
set1 = set('python')
set2 = set('php')
print(set1)     # {'n', 'o', 'p', 'y', 't', 'h'}
print(set2)     # {'p', 'h'}

# 差集==减法 A-B 等价于 A.difference(B)
获取一个集合包含而另一个集合不包含的元素集合
print(set1 - set2)  # {'n', 'y', 'o', 't'}

# 并集==加法 A | B 等价于 A.union(B)，支持多个参数
获取两个集合中包含的所有元素的集合
print(set1 | set2)  # {'o', 'p', 'h', 'y', 'n', 't'}

# 交集==求同 A & B 等价于 A.intersection(B)，支持多个参数
获取两个集合都包含的相同元素的集合
print(set1 & set2)  # {'h', 'p'}

# 异集==存异 A ^ B 等价于 A.symmetric_difference(B)
获取两个集合中互相不相同的所有元素的集合
print(set1 ^ set2)  # {'n', 'y', 'o', 't'}
```

> 成员检测
```
跟元祖、列表一致。使用in运算符判断是否包含。

示例1
set1 = {1, 'hello', 'python'}
print('python' in set1) # True
```


> 增删改查
```
# 增
add():向集合中增加元素，无返回值。

示例1
set1 = {'Python', 'Java'}
set1.add('Go')
print(set1) # {'Java', 'Python', 'Go'}

update(): 用于修改当前集合，无返回值。可以添加新的元素或集合到当前集合中，
如果添加的元素在集合中已存在，则该元素只会出现一次，重复的会忽略。

示例2
set1 = {'Python', 'Java'}
set1.update(['Python', 'Go'])
print(set1) # {'Python', 'Go', 'Java'}

示例3
set1 = {'Python', 'Java'}
set1.update(['Python', 'Go'], ('C', 'Ruby'))
print(set1) # {'Python', 'C', 'Java', 'Go', 'Ruby'}

# 删
discard():用于移除指定的集合元素，无返回值。在移除一个不存在的元素时不会报错。

示例4
set1 = {'Python', 'Java', 'Go'}
set1.discard('Go')      # {'Java', 'Python'}
print(set1)     # {'Java', 'Python'}
set1.discard('C++')
print(set1)     # {'Java', 'Python'}

remove():用于移除集合中的指定元素，无返回值。在移除一个不存在的元素时会报错KeyError。

示例5
set1 = {'Python', 'Java', 'Go'}
set1.remove('Go')
print(set1)     # {'Java', 'Python'}
set1.remove('C++')	# 引发KeyError

clear():用于移除集合中的所有元素。

示例6
set1 = {'Python', 'Java', 'Go'}
set1.clear()
print(set1)     # set()

pop():用于随机弹出一个元素，返回被弹出的元素对象。

示例7
set1 = {'Python', 'Java', 'Go'}
for i in range(3):
	print(set1.pop())
	print(set1)

>>>
Python
{'Go', 'Java'}
Go
{'Java'}
Java
set()

# 改
集合不支持修改既有元素。

# 查
集合不支持访问某个指定元素的操作，只支持遍历。
```

> 常用方法：
```
# copy():用于拷贝一个集合，无返回值。

示例1
set1 = {'Python', 'Java'}
set2 = set1.copy()
print(set2)     # {'Java', 'Python'}

# isdisjoint():验证清白。判断两个集合之间是否清白（无相同元素）。
如果没有相同元素返回True，否则返回False。

示例3
set1 = {'Python', 'Java'}
set2 = {'Go', 'Php'}
print(set1.isdisjoint(set2))    # True

示例4
set1 = {'Python', 'Java'}
set2 = {'Java', 'Php'}
print(set1.isdisjoint(set2))    # False

# issubset():子集判断。用于判断集合的所有元素是否都包含在指定集合中。
如果是则返回True，否则返回False。

示例5
set1 = {'Python', 'Java'}
set2 = {'Java', 'Python', 'Php', 'Go'}
print(set1.issubset(set2))  # True

# issuperset():父集判断。用于判断指定集合的所有元素是否都包含在原始的集合中。
如果是则返回True，否则返回False。

set1 = {'Python', 'Java'}
set2 = {'Java', 'Python', 'Php', 'Go'}
print(set2.issuperset(set1))  # True
```

## 3.6 Dictionary 字典 {k:v}

> 定义
```
使用{键：值}对的形式，用于存放具有映射关系的数据。字典的key可以是任意不可变类型。
字典是无序的，key不可以重复。支持嵌套。
```

> 实例化
```
# 使用花括号创建字典
key和value之间用半角冒号隔开。当花括号中包含多个键值对时，则使用半角逗号隔开。

d = {}  # 空字典
d1 = {"name": "cifer", "age": 18}
d3 = {(20, 30):'good', 30:'bad'}    # 元祖（不可变）可以作为key，而列表不可以。


# dict()方法
可以传入包含多个key-value型列表或元祖对象的大列表来生成字典。这些子列表或元祖必须有且仅有2个元素。
d = dict()  # 空字典

li1 = [['菠菜', 2.5], ['胡萝卜', 1.6], ['空心菜', 1.2]]
d = dict(li1)   # {'菠菜': 2.5, '胡萝卜': 1.6, '空心菜': 1.2}

li2 = [('牛肉', 22.5), ('猪肉', 18.6), ('羊肉', 15.2)]
d2 = dict(li2)  # {'牛肉': 22.5, '猪肉': 18.6, '羊肉': 15.2}

# fromkeys()方法：dict类方法，使用指定的多个key创建列表，当不指定value时默认value都为None。
li = ['a', 'b', 'c']
tup = ('x', 'y')

d1 = dict.fromkeys(li)  # {'a': None, 'b': None, 'c': None}
d2 = dict.fromkeys(tup) # {'x': None, 'y': None}
d3 = dict.fromkeys(tup, 100)    # {'x': 100, 'y': 100}

# 赋值
使用方括号语法，可以为字典的key进行赋值。
d = {}
d['name'] = '中国'
print(d)    # {'name': '中国'}

```

> 增删改查

```
key是字典的关键，对字典的操作都是基于key的。通过key可以访问value，增加、修改、删除键值对，
也可以判断键值对是否存在。

# 增
如果赋值操作时key不存在，则为新增键值对。

d = {'x': 1, 'y': 2}
d['z'] = 'hello'    # {'x': 1, 'y': 2, 'z': 'hello'}

# 删
d = {'x': 1, 'y': 2}
del(d['x'])     # {'y': 2}

# 改
如果赋值操作时key已存在，则为修改该键值对的value值。
d = {'x': 1, 'y': 2}
d['x'] = 'Python'   # {'x': 'Python', 'y': 2}

# 查
即访问，可以通过方括号语法[key]来访问value。如果key不存在，则会引发KeyError错误。
d = {'x': 1, 'y': 2}
d['x']  # 1

get()方法：根据key来获取value值。当访问不存在的key则返回None，不会报错。
d = {'x': 1, 'y': 2}
print(d.get('z'))   # None

# setdefault(k, v):根据key获取对应的value。当指定的key存在时，则返回该key对应的value；
如果指定的key不存在，则返回给定的默认value。
d = {'x': 1, 'y': 2}
value1 = d.setdefault('z', 1.5)
value2 = d.setdefault('x', 1.5)
print(value1)   # 1.5
print(value2)   # 1

成员检测：判断字典是否包含某个key，可以使用in或者not in运算符。
China = {'北京': 1, '台湾': 2}
print('台湾' in China)    # True
print('伦敦' not in China)    # True
```

> 常用方法
```
# clear():清空。清空字典的所有键值对，返回一个空字典。
d = {'name': 'Dota', 'hot': False}
d.clear()   # {}

# update():有则改之，无则加勉。使用一个新字典来更新原有的字典。如果新字典的key已存在，则会用新字典的value覆盖
原有字典的value;如果新字典的key不存在，则向原有字典中新增。
d = {'x': 1, 'y': 2}
d1 = {'y': 99, 'Python': 60}
d.update(d1)    # {'x': 1, 'y': 99, 'Python': 60}

# items(),keys(),values():分别用于获取字典中所有的键值对dict_items对象、所有键dict_keys
对象，和所有值dict_values对象。Python不希望用户直接去操作这三个对象，但是允许通过list()函数
将他们转成列表后操作。
d = {'x': 1, 'y': 99, 'Python': 60}
items_obj = d.items()   # <class 'dict_items'>
print(list(items_obj))  # [('x', 1), ('y', 99), ('Python', 60)]

keys_obj = d.keys()     # <class 'dict_keys'>
print(list(keys_obj))   # ['x', 'y', 'Python']

# pop():删除。通过key来删除指定的键值对。
d = {'x': 1, 'y': 2, '垃圾': '香港废青'}
d.pop('垃圾')     # {'x': 1, 'y': 2}



```

## 其他数据类型

#### 字节串 bytes

> 定义
```
bytes是不可变序列，由多个二进制的字节组成，以字节为单位进行操作。
在字节串中每个数据单元都是字节，也就是8位，其中每4位（相当于4位二进制数，最小值0，最大值15）可以
用一个十六进制数来表示，因此每个字节需要2个十六进制数表示。
```

> 格式转换
```
1.字符串str --> 字节bytes
方式一：如果字符串内容都是ASCII字符，则可以直接在字符串前加b来构建子节串。
例如：bb = b'abc123'

方式二：调用bytes构造方法，将字符串按照制定的字符集转成字节串。默认使用UTF-8字符集。
例如：bb = bytes('Python编程使我快乐！', encoding='utf-8')

方式三：调用字符串的encode()方法，将字符串按照指定字符集转成字节串。默认使用UTF-8字符集。
例如：bb = 'Python编程使我快乐！'.encode('utf-8')

2.字节bytes --> 字符串str
可以调用bytes对象的decode()方法，将字节串按照指定字符集转成字符串。
例如 bb = b'Python\xe7\xbc\x96\xe7\xa8\x8b\xe4\xbd\xbf\xe6\x88\x91\xe5\xbf\xab\xe4\xb9\x90\xef\xbc\x81'
msg = bb.decode('utf-8')
print(msg)

>>> Python编程使我快乐！
```


> 字符集

```
待补充

计算机底层并不能保存字符，因此为每个字符编号，当程序要保存字符时，实际保存的是该字符对应的编号。
当程序读取字符时，读取的也是其编号，接着去查“编号-字符对应表”（简称码表）才能得到实际的字符。

字符集：所有字符的编号组成的总和。

ASCII字符集：早期美国人只给英文字母、数字和标点符号等字符进行了编号。天真的以为这些拢共也就100多
个编号，只要1个字节（8位，支持256个字符编号）。

Unicode字符集：后来美国人又为世界上所有书面语言的字符进行了统一编号，这次他们用两个字节（16位，
支持65536个字符编号）。UTF-8和UTF-16等都属于Unicode字符集。
```

####  堆栈，队列？
```
？？？待补充
```



# 四、运算符

#### 赋值运算符
赋值运算符为“=”，用于为变量或者常量指定值。整体被称为赋值表达式。

```
赋值表达式：
n = 1
s = 'hello world'
flag = True
s1 = s

连续赋值：赋值表达式的值就是被赋的值，因此Python支持连续赋值。
a = b = 20
print(a)    # 20,因为表达式 b=20的值为20

批量赋值：
a,b = 10,20
print(a)    # 10
print(b)    # 20
```

#### 算术运算符
7个基本算术运算符：加减乘除商余幂

> +:加法运算符
```
n = 1 + 1   # 2
```

> -:减法运算符
```
n = 2 - 1   # 1
```

> *:乘法运算符
```
n = 2 * 2   # 4
```

> /:除法运算符
```
f = 5/2     # 2.5
```

> //:求商运算符
```
f = 5 // 2  # 2
```

> %:求余运算符
```
f = 5 % 2   # 1
```

> **:求幂运算符
```
m = 2 ** 4  # 16
```

#### 比较运算符
比较运算符用于判断两个值（可以是变量、常量或者表达式）之间的大小，返回的结果是bool值。
True表示真，False表示假。
Python支持8种比较运算符。

> `>`:大于
```
判断运算符前面的值是否大于后面的值。如果大于则返回True，否则返回False。
```

> `>=`:大于或等于
```
判断运算符前面的值是否大于或等于后面的值。如果大于或等于则返回True，否则返回False。
```

> `>`:小于
```
判断运算符前面的值是否小于后面的值。如果小于则返回True，否则返回False。
```

> `>=`:小于或等于
```
判断运算符前面的值是否小于或等于后面的值。如果小于或等于则返回True，否则返回False。
```

> `==`:等于
```
判断运算符前面的值是否等于后面的值。如果相等则返回True，否则返回False。
```

> `!=`:不等于
```
判断运算符前面的值是否不等于后面的值。如果不等则返回True；否则返回False。
```

> `is`
```
判断两个变量所引用的对象是否相同。如果相同则返回True；否则返回False。
```

> `is not`
```
判断两个变量所引用的对象是否不相同。如果不相同则返回True；否则返回False。
```

注意：== 是比较两个变量的值，而is比较的是变量的引用是否指向相同的对象。
```
import time
t1 = time.ctime()
t2 = time.ctime()
print(t1 == t2)     # True
print(t1 is t2)     # False
```

#### 逻辑运算符
逻辑运算符用来操作bool类型的变量、常量或表达式，返回的结果也是bool值。
Python支持的逻辑运算符有3个：and、or、not (与、或、非)

> and
```
与。前后两个操作数必须都是True才返回True，否则返回False。

flag = 2>1 and 1>99  # False
```

> or
```
或。只要前后两个操作数中有一个是True则返回True，否则返回False。

flag = 2>1 or 1>99  # True
```

> not
```
非。对于一个操作数，如果操作数是True，则返回False；如果操作数是False，则返回True。

flag = not 1>99  # True
```

#### 索引运算符
索引运算符为“[]”。在方括号中，既可以使用单个索引值，也可以使用索引范围，并且还可以指定步长。
```
s = 'helloworld'

s1 = s[2:8]     # llowor
s2 = s[2:8:3]   # lw
s3 = s[2:8:2]   # loo

```

#### 位运算符（略）
```
？？？太难了，表示理解不了
```

#### 三目运算符
```
x = 1 if flag else 0
```

#### 包含运算符
```
in

not in
```

运算符优先级：
```
？？？待补充
```


# 五、流程控制

### 顺序结构
程序总是从上向下依次执行。Python默认是顺序执行流。

```
pass: 表示空语句，用来占位，实际不会做任何事情。
```

### 分支结构
实现根据条件，选择性地执行某段代码。
> if-else 分支
```
（1）if语句三种形式：
第一种：
if 条件表达式：
    代码块

第二种：
if 条件表达式：
    代码块
else:
    代码块

第三种：
if 条件表达式：
    代码块
elif 条件表达式：
    代码块
else:
    代码块
    
（2）if条件表达式
条件一般为布尔表达式，也可以是任意类型，支持6种数据类型等等。除了False本身外，各种代表“空”的，例如None,
空字符串，空元祖，空列表，空字典等等，都会被当做False来处理。

（3）if表达式
详见三目运算。

```


### 循环结构
实现当满足循环条件，重复执行某段代码；当条件为假时则结束循环。否则程序会成为死循环。
循环语句一般由4个部分组成：
1.初始化：一条或多条语句，用于完成变量或对象初始化工作，在循环开始前执行。
2.循环条件：布尔表达式，决定是否执行循环体。
3.循环体：如果循环条件成立，则执行这里面的代码。
4.迭代语句：在循环体结束后，重新计算循环条件前执行。通常用于控制循环条件中的变量以便
适时退出循环。

> while 循环
```
# 语法

初始化代码块
while 循环条件：
    循环体
    迭代语句
    
示例：
count = 0
while count<5:
	print(count)
	count += 1
	
# 遍历
li = ['C', 'Python', 'Java', 'Ruby']
n = 0
while(n<len(li)):
	print(li[n])
	n += 1
	
# 嵌套
if isHouseBought:
    if isCarBought:
        getMarry()
    else:
        wait()
else:
    breakUp()
```

> for-in 循环
```
# 语法：
for 变量 in 可迭代对象:
    代码块

可迭代对象是指该对象含有一个__iter__方法，并且返回值对象具有next()方法的对象。

# 用途：专门用来遍历范围、列表、元祖和字典等可迭代对象包含的元素。

示例：
li = ['C', 'Python', 'Java', 'Ruby']
for item in li:
	print(item)

d = {'语文': '89', '数学': '100', '英语': '115'}
for k,v in d.items():
	print('key:'+k)
	print('value:'+v)
for kk in d.keys():
	print('key:'+kk)
for vv in d.values():
	print('value:'+vv)
	
# 嵌套
冒泡排序算法
li = [64, 32, 25, 47, 11, 28]
n = len(li)
for i in range(n):
    for j in range(0, n-i-1):
        if li[j]>li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]
print(li)   # [11, 25, 28, 32, 47, 64]


# for表达式
1.列表推导式（方括号的for表达式）

语法：my_list = [表达式 for 计数器 in 可迭代对象]
上述语法返回结果是列表。其中，表达式相当于是循环体。可迭代对象拥有的元素个数即为循环执行的
次数，并将每次执行的值收集起来作为新的列表元素。

li = [x*x for x in range(1, 6)] # [1, 4, 9, 16, 25]

可以在for表达式后添加if条件，那么for表达式只会循环执行那些符合条件的元素。
li = [x*x for x in range(1, 6) if x%2==0]   # [4, 16]

还可以使用多个循环。并且多循环场景也支持if条件过滤。
li = [(x, y, z) for x in range(1, 3) for y in range(6, 8) for z in range(0,2)]
print(li)   # [(1, 6, 0), (1, 6, 1), (1, 7, 0), (1, 7, 1), (2, 6, 0), (2, 6, 1), (2, 7, 0), (2, 7, 1)]

2.生成器推导式（圆括号的for表达式）

语法：my_generator = (x*x for x in range(1, 6)) # [1, 4, 9, 16, 25)
最终返回的是生成器对象。
print(type(my_generator))   # <class 'generator'>
print(my_generator) # <generator object <genexpr> at 0x0000000002553E60>
for item in my_generator:
	print(item)
	
	
# 工具函数

1.打包函数 zip()
接收N个列表，返回一个zip对象（可迭代对象），这样就可以使用一个循环来遍历这些列表。
此时zip对象的元素就是长度为N的子元祖。

示例1
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
result = [x for x in zip(list1, list2)]     # [('a', 1), ('b', 2), ('c', 3)]

示例2
courses = ['语文', '数学', '英语']
scores = [105, 135, 120]
for course,score in zip(courses, scores):
	print('%s成绩是：%.0f 分' % (course, score))
>>>
语文成绩是：105 分
数学成绩是：135 分
英语成绩是：120 分

如果被打包的列表长度不一致，那么打包后的长度以短的列表为准。
示例3
courses = ['语文', '数学']
scores = [105, 135, 120]
for course,score in zip(courses, scores):
	print('%s成绩是：%.0f 分' % (course, score))
>>>
语文成绩是：105 分
数学成绩是：135 分

2.反转函数 reversed()
支持进行反向遍历。反转函数可以接收各种序列，包括字符串、元祖、列表、区间等，并返回一个逆序排列的迭代器。
反转函数不会对原对象产生影响。

示例1
num = range(10)
li = [x for x in reversed(num)]
print(li)   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(num)  # range(0, 10)

3.排序函数 sorted()
接收一个可迭代对象作为参数，返回一个队元素排列后的列表。排序函数不会对原对象产生影响。
示例1
s = 'hello'
li = [56, 23, 47, 19]
print(sorted(s))    # ['e', 'h', 'l', 'l', 'o']
print(sorted(li))   # [19, 23, 47, 56]

sorted()函数还可以传入一个reverse参数。如果设置为True，则表示反向排序。
示例2
li = [56, 23, 47, 19]
print(sorted(li))   # [19, 23, 47, 56]
print(sorted(li, reverse=True)) # [56, 47, 23, 19]

sorted()函数还可以传入一个key参数，用于指定一个函数来作为排序的标准。例如，如果希望按照
长度作为依据排列，那么可以传入len函数。
示例3
li = ['Python', 'Java', 'Ruby', 'Swift', 'C']
print(sorted(li, key=len))

```


> 循环控制

#### break 结束循环
```
当某种条件出现的时候需要强制结束循环，而不再是等待循环条件为False才退出循环。
示例1
for i in range(10):
	if i == 2:
		print('强制结束循环 i=%.0f' % i)
		break
	else:
		print('正在循环 i=%.0f' % i)
>>>
正在循环 i=0
正在循环 i=1
强制结束循环 i=2

应对嵌套循环：break只能结束当前所在的循环，而不能跳出外层循环。如果需要break语句同时跳出
外层循环，可以使用预定义的旗标来辅助。
示例2
flag = False
for i in range(5):
	for j in range(3):
		if j == 2:
			flag = True
			break
	if flag:
		break
```
#### continue 跳开并继续循环
```
不会结束循环，只会忽略当次循环的剩余语句，仍会继续执行下一个循环。

示例1
for i in range(3):
	if i == 1:
		continue
	print('啦啦啦，我被翻牌子啦 i=%.0f' % i)
>>>
啦啦啦，我被翻牌子啦 i=0
啦啦啦，我被翻牌子啦 i=2
```

#### return 结束方法
```
用于从被包围的最直接的函数处返回，该函数随之结束。如果return处于循环体中，无论循环有多少层，
都会直接结束整个所在函数或方法。

示例1
def test():
	for i in range(3):
		if i == 1:
			return i
		print('啦啦啦，我被翻牌子啦 i=%.0f' % i)

if __name__ == '__main__':
	index = test()
	print(index)

>>>
啦啦啦，我被翻牌子啦 i=0
1

```


# 六、函数

> 定义
```
函数是实现特定功能的可以复用的一段代码。函数拥有自己的名称，可以接收零个或多个参数，
可以返回零个或多个值。
1.参数：函数需要传入的动态变化的数据，应该被定义成函数的参数。
2.返回值：函数需要传出的重要数据，应该被定义成返回值。
3.函数体：函数的内部实现过程。

Python中的函数是“一等公民”，函数本身也是一个<class 'function'>对象，既可以用于赋值，
也可以作为其他函数的入参，还可以作为其他函数的返回值。
```


> 声明函数
```
def 函数名(形参1:类型 = 默认值, 形参2:类型 = 默认值):
    代码块
    return 返回值

函数名：建议使用一个或多个单词组成，单词字母一律小写，单词之间用下划线分隔。
形参：用于定义该函数可以接收的参数。
类型：数据类型，支持int,float,str,bool以及类名。
返回值：可以显式地返回一个或者多个值/变量/对象表达式/函数。如果同时返回多个值，那么值与
值之间用逗号分隔，并且Python会将多个返回值自动封装成元祖。

示例1
def add(x, y):
	result = x + y
	return result

示例2
def add(x, y):
	result = x + y
	return result, x, y 
if __name__ == '__main__':
	data = add(1,1)
	print(type(data))   # <class 'tuple'>
	print(data)     # (2, 1, 1)

```


> 调用函数
```
函数体默认按照顺序流执行，即从上往下依次执行。
如果形参没有指定默认值，那么调用时需要传入参数的个数必须完整。
调用时传参方式详见后续的“入参详解”部分。

示例1
def add(x, y):
	result = x + y
	return result
if __name__ == '__main__':
	n = add(1,1)
	print(n)
>>>
2
```


> 函数文档
```
# 定义函数文档
定义在函数声明def之后，函数体代码之前的一段字符串，即为函数的说明文档。通常使用三对双引号
包围的多行文本。

示例1
def add(x, y):
	"""
	计算两个数的和
	@param: x 数值
	@param: y 数值
	@return 和值
	"""
	result = x + y
	return result

# 查看函数文档
可以通过help()函数来查看，也可以通过__doc__属性查看函数的说明文档。
示例2
help(add)
>>>
Help on function add in module __main__:

add(x, y)
    计算两个数的和
    @param: x 数值
    @param: y 数值
    @return 和值
print(add.__doc__)
>>>
计算两个数的和
@param: x 数值
@param: y 数值
@return 和值
```


> 递归函数
```
递归是指一个函数体内调用自身。其中包含了一种隐式循环，会重复执行某段代码，并且这种重复执行
无需循环控制。因此必须自定义一个退出机制，否则很容易形成死循环。

示例1
需求：已知有一个数列，f(0)=1, f(1)=4, f(n+2)=2*f(n+1)+f(n)，其中n是大于0的整数，
求f(10)的值。
解题：由f(n+2)=2*f(n+1)+f(n)可知f(n) = 2*f(n-1)+fn(n-2).

def fn(n):
	if n == 0:
		return 1
	elif n == 1:
		return 4
	else:
		data = 2*fn(n-1) + fn(n-2)
		return data

if __name__ == '__main__':
	n = fn(10)
	print(n)    # 10497


# 斐波拉契数列

def fib(n):
	if n ==1 or n == 2:
		return 1
	else:
		return fib(n-1)+fib(n-2)
if __name__ == '__main__':
	data = fib(10)
	print(data)     # 55

```


> 入参详解
```
形参：形式参数，定义的时候只作占位，它们的值只有在函数的调用者真正调用的时候才能确定下来。
谁想调用函数，谁就要负责传入参数值。
入参：传入参数。

1.【固定参数】
参数的个数能够确定。


（1） 位置参数 args
是指按照形参的位置依次传入的参数值，因此对于位置先后有严格要求。

示例1
def introduce(name, age):
	msg = '大家好！我的名字叫“%s”, 今年“%s”岁。'  %(name, age)
	print(msg)

if __name__ == '__main__':
	introduce('老佛爷', '18')  # 大家好！我的名字叫“老佛爷”, 今年“18”岁。【正确】
	introduce('19', '老司机')  # 大家好！我的名字叫“19”, 今年“老司机”岁。【错误】

（2） 关键字参数 kwargs
是指按照参数名来对应传入参数值，无需遵守参数的位置顺序。

示例2
def introduce(name, age):
	msg = '大家好！我的名字叫“%s”, 今年“%s”岁。'  %(name, age)
	print(msg)

if __name__ == '__main__':
	introduce(age='19', name='老司机') # 大家好！我的名字叫“老司机”, 今年“19”岁。

（3） 混搭：
Python支持函数调用时同时使用位置参数和关键字参数，但是要求关键字参数必须在位置参数之后。

示例3
def introduce(name, age):
	msg = '大家好！我的名字叫“%s”, 今年“%s”岁。'  %(name, age)
	print(msg)

if __name__ == '__main__':
	introduce('cifer', age='18') # 大家好！我的名字叫“cifer”, 今年“18”岁。
	
（4） 指定数据类型：
指定参数值的数据类型。（待补充？？？）已指定数据类型的参数位置必须位于未指定数据类型的参数
之后。数据类型支持int,float,str,bool以及类名。
语法： （形参名1, 形参名2 : str） 

示例4
def introduce(name: str, age: int):
	msg = '大家好！我的名字叫“%s”, 今年“%s”岁。'  %(name, age)
	print(msg)
if __name__ == '__main__':
	introduce('cifer', age=18)

（5） 指定默认值：
函数在定义时可以为一个或者多个形参指定默认值，这样在函数调用时，可以省略为该形参传值，
而是直接使用默认值即可。需要注意的是，指定了默认值的形参位的位置必须在未指定默认值的
形参位置之后。
语法： （形参名1, 形参名2 = 默认值）

示例5
def introduce(name: str, age: int = 18):
	msg = '大家好！我的名字叫“%s”, 今年“%s”岁。'  %(name, age)
	print(msg)

if __name__ == '__main__':
	introduce('cifer')  # 大家好！我的名字叫“cifer”, 今年“18”岁。

2.【可变参数】-零存整取
Python定义函数时允许形参的个数是可变的，这样在调用函数时可以传入任意多个零星参数。
？？？可变参数的位置是否任意（特别是关键字参数），待考证

# 普通参数收集
在形参前添加一个星号*，即表示该参数可以接收N个参数值，传入后将被收集成元祖对象。
一个函数最多只能带一个普通参数收集的形参。

示例6
def tellHobby(name, *hobbies):
	print(type(hobbies))
	print(hobbies)
	print('我叫“%s”，我喜欢%s' %(name, hobbies))
if __name__ == '__main__':
	tellHobby('cifer', 'coding', 'fishing', 'cooking')

>>>
<class 'tuple'>
('coding', 'fishing', 'cooking')
我叫“cifer”，我喜欢('coding', 'fishing', 'cooking')

普通参数收集可以处于形参列表的任意位置。
如果普通参数收集的形参后面有固定参数，那么传参时的固定参数必须使用关键字方式传值。
示例7
def tellHobby(*hobbies, name):
	print(type(hobbies))
	print(hobbies)
	print('我叫“%s”，我喜欢%s' %(name, hobbies))
if __name__ == '__main__':
	tellHobby('coding', 'fishing', 'cooking', name='cifer')

>>>
<class 'tuple'>
('coding', 'fishing', 'cooking')
我叫“cifer”，我喜欢('coding', 'fishing', 'cooking')

# 关键字参数收集
在形参前添加两个星号**，即表示该参数可以接收N个关键字参数值，传入后将被收集成字典对象。
一个函数最多只能带一个关键字参数收集的形参。
关键字参数收集的可变形参，在参数列表中必须位于末尾。？？？待考证

示例8
def showScore(name, **scores):
	print(type(scores))
	print(scores)
	print('我叫“%s”，我的成绩是%s' %(name, scores))
if __name__ == '__main__':
	showScore(语文=89, 数学=125, 英语=130, name='乔碧萝')
>>>
<class 'dict'>
{'语文': 89, '数学': 125, '英语': 130}
我叫“乔碧萝”，我的成绩是{'语文': 89, '数学': 125, '英语': 130}

# 混搭收集
一个函数的参数列表允许同时包含一个普通参数收集和一个关键字参数收集。

示例9
def showScore(name, *hobbies, **scores):
	print('我叫“%s”，我爱好是%s，我的成绩是%s' %(name, hobbies, scores))
if __name__ == '__main__':
	showScore('乔碧萝', '直播', '美颜', 语文=89, 数学=125)
>>>
我叫“乔碧萝”，我爱好是('直播', '美颜')，我的成绩是{'语文': 89, '数学': 125}

3.【实参分解】-整存零取
Python允许在函数调用时，将现有的列表、元祖、字典等对象的元素拆开，逐个传值给形参。
在传入的实参前面添加星号即可，列表、元祖之前添加一个星号*，字典之前添加两个星号**。

示例10
def introduce(name, age):
	msg = '大家好！我的名字叫“%s”, 今年“%s”岁。'  %(name, age)
	print(msg)

if __name__ == '__main__':
	tup = ('公主', '19')
	li = ['王子', '20']
	dic = {'age': '21', 'name': '骑士'}
	introduce('cifer', '18')	# 普通青年：一个萝卜一个坑
	introduce(*tup)		# 文艺青年：分解元祖
	introduce(*li)      # 文艺青年：分解列表
	introduce(**dic)    # 文艺青年：分解字典

>>>
大家好！我的名字叫“cifer”, 今年“18”岁。
大家好！我的名字叫“公主”, 今年“19”岁。
大家好！我的名字叫“王子”, 今年“20”岁。
大家好！我的名字叫“骑士”, 今年“21”岁。


被分解后的元素，将会根据形参的位置依次进行赋值。
示例11
def tellHobby(name, *hobbies):
	print('我叫“%s”，我喜欢%s' %(name, hobbies))
if __name__ == '__main__':
	li = ['cifer', 'coding', 'fishing', 'cooking']
	tellHobby(*li)  # 列表的元素被分解，第一个赋值给name，剩下的则被hobbies收集

```


> 变量作用域
```
是指在程序中定义的变量的作用范围。

# 全局变量
全局变量是指在函数外面、全局范围内定义的变量。全局变量可以在所有函数中被访问。

示例1
var_global = 'global variables here'
def test():
	pass

# 局部变量
局部变量是指在函数中定义的变量，包括参数。如果在函数中对一个不存在的变量赋值时，默认是
重新定义一个新的局部变量。如果赋值给一个全局已存在的变量赋值，则会产生遮蔽。

示例2
def test(var_local1):
	var_local2 = 'local variables here'

# 查看变量字典
1.globals():返回当前全局范围内所有变量组成的变量字典。
2.locals():返回当前局部范围内所有变量组成的变量字典。
3.vars(object):获取在指定对象范围内的所有变量组成的变量字典。如果不传入object对象，
则跟locals()的效果完全相同。

示例3
hobby = 'Python'
def introduce(name, age):
	msg = '大家好！我的名字叫“%s”, 今年“%s”岁。' % (name, age)
	print(locals())

if __name__ == '__main__':
	print(globals())
	introduce('cifer', '18')

>>>
全局变量字典：{内置的变量...,'hobby': 'Python', 'introduce': <function introduce at 0x0000000001D42EA0>}
局部变量字典：{'msg': '大家好！我的名字叫“cifer”, 今年“18”岁。', 'age': '18', 'name': 'cifer'}


# 同名困境

（1）变量遮蔽 hide
如果在函数中定义了与全局变量同名的局部变量，那么该全局变量就会被局部变量遮蔽。

示例4 遮蔽前
name = '王校长'
def marry():
	print(name)    # 王校长
marry()

示例4 遮蔽后
name = '王校长'
def marry():
	print(name) # name变量已被遮蔽，强行访问被报错
	name = '叶良辰'
marry()
>>>
UnboundLocalError: local variable 'name' referenced before assignment

（2）解决遮蔽

1.不要同名
在函数中定义局部变量时，尽量不要跟全局变量同名，所谓一山不容二虎。

2.精确锁定
如果发生遮蔽，无力回天，却仍需要访问被遮蔽的全局变量时，则可以借助globals()获取全局变量字典来实现。

示例5
name = '王校长'
def marry():
	print(globals()['name'])    # 王校长
	name = '叶良辰'
	print(name)     # 叶良辰
marry()

3.升级作用域
在函数中定义局部变量时，可以使用global关键字来将其声明成全局变量，其作用域升级为全局。

示例6
name = '王校长'
def marry():
	global name
	print(name)
	name = '叶良辰'
marry()
print(name)

```


> 局部函数
```
局部函数是指在函数体内定义的函数，对于外部来说是隐藏的，只能在其封闭函数内
有效。其封闭函数也可以返回局部函数，以便程序在其他作用域中使用局部函数。

示例1
def get_math_func(type, nn):

	def square(n):
		return n*n

	def cube(n):
		return n*n*n

	def factorial(n):
		result = 1
		for index in range(2, n+1):
			result *= index
		return result

	if type == 'square':
		return square(nn)
	elif type == 'cube':
		return cube(nn)
	else:
		return factorial(nn)

局部函数中的局部变量也有可能出现遮蔽情形。解决对策跟普通函数思路类似，可以使用nonlocal
关键字将同名的局部变量升级为全局变量来使用，道理类似global关键字。
```


> 函数高阶
```
（1）函数变量
所有函数都是function对象，可以把函数本身赋值给变量。当把函数赋值给变量后，程序可以通过
该变量来调用函数。

示例1
def area(width, height):
	return width * height

my_func = area      # <class 'function'>
data = my_func(2, 5)    # 10


（2）函数形参
有时候在定义一个函数的时候，发现大部分计算逻辑都能确定，但是某些部分的处理逻辑暂时无法
确定，意味着程序的代码需要动态改变。如果希望调用函数的时候能够动态传入这些代码，则可以
在函数中定义函数形参，这样就可以在调用时传入不同的函数作为参数从而实现动态改变这段代码。

示例2
def my_map(data, func):
	result = []

	for item in data:
		result.append(func(item))
	return result

def square(n):
	return n*n

def cube(n):
	return n*n*n

def factorial(n):
	result = 1
	for index in range(2, n+1):
		result *= index
	return result

if __name__ == '__main__':
	data=[3, 4, 9, 5, 8]
	in_square = my_map(data, square)   # [9, 16, 81, 25, 64]
	in_cube = my_map(data, cube)   # [27, 64, 729, 125, 512]
	in_factorial = my_map(data, factorial) # [6, 24, 362880, 120, 40320]


（3）返回函数
可以使用函数对象作为其他函数的返回值。

示例3
def get_math_func(type):

	def square(n):
		return n*n

	def cube(n):
		return n*n*n

	def factorial(n):
		result = 1
		for index in range(2, n+1):
			result *= index
		return result

	if type == 'square':
		return square
	elif type == 'cube':
		return cube
	else:
		return factorial

if __name__ == '__main__':
	my_func = get_math_func('square')
	print(type(my_func))    # <class 'function'>
	print(my_func.__name__) # square


（4）lambda表达式（匿名函数）
函数是命名的可复用的代码块，而lambda表达式则是匿名的单行函数体。

# 语法（左进右出）
lambda 形参:表达式

语法说明：
1.关键字：必须使用lambda关键字声明。
2.形参：表达式的冒号左边是形参列表，形参个数可以是0，也可以是多个。多个形参之间用半角
逗号隔开。
3.返回：冒号右边整体是表达式的返回值。表达式中包含了对入参的各种逻辑运算。


# 简化局部函数
由于局部函数的特点是，其作用域仅限封闭函数内，因此它的名字没有太大意义，因此可以考虑使用
lambda表达式来简化局部函数的写法。

使用lambda前：
def get_math_func(type):

	def square(n):
		return n*n

	def cube(n):
		return n*n*n

	if type == 'square':
		return square
	elif type == 'cube':
		return cube

if __name__ == '__main__':
	my_func = get_math_func('square')
	print(type(my_func))    # <class 'function'>
	print(my_func.__name__) # square
	print(my_func(5))       # 25


使用lambda后：
def get_math_func(type):

	if type == 'square':
		return lambda n: n*n
	elif type == 'cube':
		return lambda n: n*n*n
if __name__ == '__main__':
	my_func = get_math_func('square')
	print(type(my_func))    # <class 'function'>
	print(my_func.__name__) # <lambda>
	print(my_func(5))       # 25

# 特点
总体来说，函数比lambda表达式的适应性更强，lambda表达式只能创建简单的函数对象。
lambda表达式的最佳实践：
1.对于单行函数，使用lambda表达式可以省去定义函数的过程，让代码更加简洁；
2.对于不需要多次复用的函数，使用lambda表达式可以用完后立即释放，提高了性能。

示例1：使用lambda表达式作为函数对象传入
data = map(lambda x: x*x, range(5))
print([i for i in data])    # [0, 1, 4, 9, 16]
```


# 七、面向对象 OOP
```
Python是面向对象的编程语言，支持面向对象的三大特征：封装、继承和多态。子类继承父类
同样可以继承到父类的变量和方法。

```

> 类和对象

```
一般来说，定义一个类是为了能够重复创建该类的对象，同一个类的多个对象具有相同的特征，而类
则定义了多个对象的共同特征。类是一种抽象，对象则是具体存在的实体。

（1）类
概念：是对一批对象的抽象。可以把类当成一种自定义的类型，可以用来表示变量，也可以使用
类来创建对象。

Python中使用class关键字来声明类。

语法：
class 类名(父类名):
    类变量
    实例方法
    ...

类名：必须由一个或者多个有意义的单词组成，每个单词的首字母大写，单词与单词之间不要使用
分隔符。
类变量：归属于类本身，用于定义该类本身所包含的状态数据。
实例方法：用于定义该类的对象的行为或功能实现。
父类名：所继承的父类名称（详见“继承”版块）。如果没有父类，则可以省略括号和父类名。


Python是动态语言，因此类所包含的变量可以动态增加和删除。程序在类体中为新变量赋值
就是增加类变量，程序也可以在任何地方为已有的类增加变量。程序可以使用del语句删除已有的
类变量。

同理，对象的实例变量也可以动态增加或者删除。只要对新的实例变量进行赋值，就是增加
实例变量，程序也可以在任何地方为已有的对象增加实例变量。程序可以使用del语句删除已有的
实例变量。

在类中定义的方法默认是实例方法，定义方式类似普通函数，只是实例方法的第一个参数会被绑定到
方法的调用者（该类的实例），因此实例方法天生自带一个参数，通常被命名为self。

构造方法：
在实例方法中有一个非常特别的方法：__init__，称为“构造方法”，用于构造该类的对象，并直接
返回该类的对象。这是创建对象的根本途径，如果开发者没有定义，那么Python会默认添加该函数。

类说明文档：放在类声明之后、类体之前。

类的作用：创建对象、派生子类

示例1
class Student(Person):
    """
    这是人类
    """

    # 定义类变量
    has_body = True
    has_spirit = True

    # 定义构造方法
    def __init__(self, name: str, age: int):
        # 定义对象的实例变量
        self.name = name
        self.age = age

    # 定义实例方法
    def eat(self):
        pass

    def study(self):
        pass

    def sleep(self):
        pass


（2）对象
也称为“实例”，是一个具体存在的实体。

创建：也称“实例化”，创建对象的根本途径是构造方法，调用类的构造方法即可创建这个类的对象。
class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

cifer = Student(name='cifer', age=18)
print(cifer)       # <__main__.Student object at 0x00000000021F85C0>


对象的作用：
对象的属性好比特征（静态），对象的方法好比行为（动态）。

1.操作对象的实例变量（属性）：访问实例变量的值、添加实例变量、删除实例变量。

语法：     类.属性        对象.属性

示例1
class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

if __name__ == '__main__':
    cifer = Student(name='cifer', age=18)   # 实例化对象
    print(cifer.name, cifer.age)        # 访问实例变量的值
    cifer.name = '叶良辰'
    cifer.school = '粤海街道办'     # 添加实例变量      
    print(cifer.school)     # 粤海街道办
    print('删除实例变量前：', dir(cifer))   # [...'age', 'name', 'school']
    del cifer.age      # 删除实例变量
    print('删除实例变量后：', dir(cifer))   # [...'name', 'school']

2.操作对象的方法：调用方法、添加方法、删除方法。

【首参self 自动绑定】

# 定义方法
对于在类体中定义的实例方法（包括构造方法），Python会自动绑定，将方法的第一个参数self
与调用方法的对象进行绑定。通常将首参命名为self，当然其他单词也可以但是不建议。
在构造方法中，首参self自动绑定的是该构造方法正在实例化的对象，而在普通实例方法中，首参
self自动绑定的是调用该实例方法的对象（调用者）。

# 调用方法·谁
由于首参自动绑定机制的存在，在调用构造方法和普通实例方法时就可以无需传入首参self。
首参self所指向的对象虽然是不确定的，但是它的类型是确定的，也就是self只能代表当前类的实例。
只有当这个方法被调用时，self所代表的具体对象才能确定下来，即谁在调用这个方法，那么self就
指向谁。

语法：     类.方法()        对象.方法()

# 方法调用 VS 函数调用
从Python语言的设计来看，Python的类、对象有点类似于命名空间，因此在调用类、方法时，一定要
加上“类.方法()”或“对象.方法()”的形式，否则光秃秃的直接嗲用方法的形式属于调用函数。

示例2
class Student:

    # 此处self绑定正在实例化的对象
    def __init__(self, name: str, age: int):
        self.name = name    # self作为对象的默认引用
        self.age = age

    # 此处self绑定调用者
    def study(self, language: str):
    	print('study {} everyday'.format(language))

if __name__ == '__main__':
	stu = Student(name='叶良辰', age=18)   # 实例化对象
	stu.study('Python')   # 调用方法

当给对象动态增加方法时，Python不会自动将调用者绑定到它们的第一个参数，因此程序需要手动
为新增的方法传入参数值。

示例3
class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def study(self, language: str):
    	print('study {} everyday'.format(language))

if __name__ == '__main__':
	stu = Student(name='叶良辰', age=18)   # 实例化对象
	stu.study('Python')   # 调用方法

    # 动态添加方法：定义函数
	def fn(self):
		print(self.name, self.age, end='')		# 叶良辰 18

	stu.show = fn		# 动态添加方法
	stu.show(stu)	# 调用添加后的方法
	print(type(stu.show))		# <class 'function'>
	print(dir(stu))		# [...'name', 'age', 'study', 'show']
	
	# 动态添加方法：lambda表达式
	stu.sleep = lambda self: print(self.name+'晚上10点睡觉。')    # 叶良辰晚上10点睡觉。
	stu.sleep(stu)
	print(dir(stu))     # [...'name', 'age', 'study', 'show']
	
	# 删除方法
	del stu.show
	print(dir(stu))     # [...'name', 'age', 'study']
	

如果希望既能为对象动态添加方法，又能让其自动绑定到第一个参数，则可以借助types模块
的MethodType进行包装。

示例4
class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

if __name__ == '__main__':

	stu = Student(name='叶良辰', age=18)   # 实例化对象

    # 动态添加方法：定义函数
	def fn(self):
		print(self.name, self.age, end='')		# 叶良辰 18

	# 动态添加方法
	from types import MethodType
	stu.show = MethodType(fn, stu)		# 包装
	stu.show()	# 调用添加后的方法


动态绑定的首参self并不依赖方法的具体调用方式，不管是采用方法调用形式，还是函数调用形式来
执行它，self参数都一样可以自动绑定。

示例5
class Student:
    def study(self):
    	print(self)

if __name__ == '__main__':
	stu = Student()
	stu.study()		# <__main__.Student object at 0x00000000023E8240>

	fn = stu.study
	fn()		# <__main__.Student object at 0x0000000001E585C0>


首参self除了可以作为方法的入参外，还可以作为方法的返回值。这样在某些场景下可以实现连续
调用（链式调用）。

示例6
class Student:

	def __init__(self, name: str):
		self.name = name

	def read(self):
		print('{} finished reading.'.format(self.name))
		return self

	def write(self):
		print('{} finished writing.'.format(self.name))
		return self

	def exam(self):
		print('{} finished exam.'.format(self.name))
		return self

if __name__ == '__main__':
	Student('叶良辰').read().write().exam()

>>>
叶良辰 finished reading.
叶良辰 finished writing.
叶良辰 finished exam.
```










# 八、异常机制
```
待补充
```


# 九、多线程
```
待补充
```


# 十、常用类库API
```
待补充
（1) time 时间日期

（2）DB 数据库

（3）I/O 读写文件

（4）HTTP网络请求

（5）GUI 界面交互
```