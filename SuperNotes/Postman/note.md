# POSTMAN 使用笔记
2019-8-11
BY CIFER


#### RESTful接口请求方式
- GET
- POST
- PUT
- DELETE
- PATCH

#### 发送GET请求
```
# 不带参数
url:postman-echo.com

# Params传参
url:postman-echo.com/get?user=manyan&title=beauty

```

#### 发送POST请求
```
# Params传参
url:postman-echo.com/post?user=manyan

# Body传参的Content-Type四种类型
（1）form-data 复合表单
（2）application/x-www-form-urlencoded 单一表单
（3）raw:xml,json 文本内容
（4）binary 二进制（文件、音频、视频）

示例：
url:postman-echo.com/post
content-type:application/x-www-form-urlencoded
Body: user=manyan&msg=hello

示例：
url:postman-echo.com/post
Content-Type:application/json; charset=utf-8
Body:
{
	"user":"manyan"
}

```

#### 身份验证Authorization
```
# Basic Auth
GET:postman-echo.com/basic-auth
Authorization：Username填postman,Password填password

如果不添加认证的话，服务器将返回401；添加认证后，返回200，响应报文：
{
    "authenticated": true
}

# Digest Auth
采用哈希加密方法，避免用明文传输用户的口令。摘要认证就是要合适参与通信的两方都知道双方共享的一个口令。
Digetst realm='iptel.org', qop='auth,auth-int'
nonce="abcdedeedde...", opaque="", algorithm=MD5

# Hawk Auth

# OAuth 1.0 开放授权
允许用户让第三方应用访问该用户在某一网站上存储的私密资源，而无需将用户名和密码提供给第三方使用。

```

#### Cookie


#### 环境变量

（1） 本地变量 Local
定义在Pre-request Script脚本中的，只针对单个URL请求设置的变量。作用域仅限单个请求范围内。
```
# 定义
pm.variables.set("username","manyan")
pm.variables.set("password","123")

# 引用
{{username}}
{{password}}
```

（2） 全局变量 Global
在所有的环境中，变量的值都是一样的，作用域是所有的请求。定义方式有两种：界面设置、脚本设置。
```
# 界面设置
Globals

# 脚本定义
pm.globals.set("user", "cifer")

备注：如果全局变量出现和环境变量重名时，会被环境变量所覆盖。


# 参数提取
在实际接口测试中经常遇到接口相互关联的请情况，一个接口需要引用上个
接口返回的某个值作为自己的参数。

接口A:GET:postman-echo.com/get?user=manyan
响应：
{
    "args": {
        "user": "manyan"
    },
    "headers": {
        "x-forwarded-proto": "https",
        "host": "postman-echo.com",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "cache-control": "no-cache",
        "cookie": "sails.sid=s%3AajH-00YRJ0_VfQjpeLxKdKAu_MvOu0kg.nQ%2BfEX7q1NrFGkPzOK7H%2FvzaxfU9abjzp1gBAR89sCE",
        "postman-token": "81bfcca9-c22f-4c94-83f8-0d5f5e844926",
        "user-agent": "PostmanRuntime/7.15.2",
        "x-forwarded-port": "80"
    },
    "url": "https://postman-echo.com/get?user=manyan"
}

在接口A的Tests中提参：
var jsonData = pm.response.json();
my_girl = jsonData.args.user
pm.globals.set("my_girl", my_girl)


接口B:POST:postman-echo.com/post
Content-Type:application/json; charset=utf-8
Body:{"username": {{my_girl}}}


```

（3） 环境变量 Env
值会根据环境的不同而发生变化的变量，例如开发环境、测试环境和生产环境，有利于在不变更
测试用例的前提下通过切换环境达到测试不同环境接口的目的，便于维护。
```
示例
定义DEV 环境host:dev.tbp.com
定义SIT 环境host:sit.tbp.com
引用：{{host}}/api/getUserInfo
```



（4） 数据变量
通过导入外部文件（json或者csv等）来获取变量，多用于数据驱动。
