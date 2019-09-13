
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