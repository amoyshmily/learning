
#### 避免urllib3打印多余的安全警告信息
```
背景：requests请求https资源时使用了参数verify=False，默认在控制台便会打印安全警告信息，比较闹心。

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```

#### 快速将字符串拆分成单个字符
```
words = 'hello'
li = list(words)
print(li)

>>>
['h', 'e', 'l', 'l', 'o']
```


#### 获取当前所在路径
```
import os

current_path = os.path.dirname(__file__)
parent_path = os.path.dirname(os.path.dirname(__file__))

```



#### 冒泡排序

```
def bubbleSort(input_list: list):

    lens = len(input_list)
    for i in range(lens-1):
        for j in range(lens-1-i):
            if input_list[j] > input_list[j+1]:
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

```


#### 屏幕截图
```
from PIL import ImageGrab

# 屏幕截图
image_obj = ImageGrab.grab((0, 0, 500, 500))
# 保存图片
image_obj.save('/....png')
```


#### 日志简单配置
```
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
```


#### 大列表拆分成N个小列表
```
解决方案：列表生成式

示例：

father = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
children = list(father[i:i+3] for i in range(0,len(father), 3))
print(children)

>>>
[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
```



#### 装饰器

```
示例：

def logit(name: str = ''):
	def decorator(fn):
		def wrapFn():
			print('-'*20+name+' 开始 '+'-'*20)
			result = fn()
			print('-'*20+name+' 结束 '+'-'*20)
			return result
		return wrapFn
	return decorator

@logit(name="造数")
def test():
	print('......正在努力......')



if __name__ == '__main__':
	test()

>>>
--------------------造数 开始 --------------------
......正在努力......
--------------------造数 结束 --------------------
```



#### 关于 __repr__ 和 __str__ 

```
__repr__ 目的是为了表示清楚，是为开发者准备的。

__str__ 目的是可读性好，是为使用者准备的。

我的理解是 __repr__ 应该尽可能的表示出一个对象来源的类以及继承关系，方便程序员们了解这个对象。而 __str__ 就简单的表示对象，而不要让不懂编程的以为输出的是 bug。

>>> import datetime
>>> today = datetime.datetime.now()
>>> str(today)
'2012-03-14 09:21:58.130922'
>>> repr(today)
'datetime.datetime(2012, 3, 14, 9, 21, 58, 130922)'

官方文档：

object.__repr__(self)
Called by the repr() built-in function to compute the “official” string representation of an object. If at all possible, this should look like a valid Python expression that could be used to recreate an object with the same value (given an appropriate environment). If this is not possible, a string of the form <...some usefuldescription...> should be returned. The return value must be a string object. If a class defines __repr__()but not __str__(), then __repr__() is also used when an “informal” string representation of instances of that class is required.

This is typically used for debugging, so it is important that the representation is information-rich and unambiguous.





object.__str__(self)
Called by str(object) and the built-in functions format() and print() to compute the “informal” or nicely printable string representation of an object. The return value must be a string object.

This method differs from object.__repr__() in that there is no expectation that __str__() return a valid Python expression: a more convenient or concise representation can be used.

The default implementation defined by the built-in type object calls object.__repr__().




repr(object)
Return a string containing a printable representation of an object. For many types, this function makes an attempt to return a string that would yield an object with the same value when passed to eval(), otherwise the representation is a string enclosed in angle brackets that contains the name of the type of the object together with additional information often including the name and address of the object. A class can control what this function returns for its instances by defining a __repr__() method.





str(object='')
Return a string containing a nicely printable representation of an object. For strings, this returns the string itself. The difference with repr(object) is that str(object) does not always attempt to return a string that is acceptable to eval(); its goal is to return a printable string. If no argument is given, returns the empty string, ''.



```


#### 安全遍历删除字典项
```
data = {'a':1, 'b':2, 'c':3}

for key in list(data):
	if data[key] == 2:
		data.pop(key)

print(data)
>>>
{'a': 1, 'c': 3}

注意：如果采用k in data.keys()，data.values()或者data.items()来遍历，会报错。

错误用法：
    for k, v in driver_node.items():
        if v is None:
            driver_node.pop(k)
```