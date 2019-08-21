
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