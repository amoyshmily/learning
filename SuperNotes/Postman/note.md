# POSTMAN 使用笔记
2019-8-11
BY CIFER

# 调用
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


#### 批量执行 Collection Runner
可以使用Collection Runner来批量运行API，同时可以进行环境变量、迭代执行次数、延迟时间等设置。
```
参数配置：
Environment：环境（dev/sit/mock/prod/release...）
Iterations：迭代次数
Delay：调用间隔，单位毫秒ms
Log Response：记录响应日志
Data：外部数据（可以用于数据驱动）
```


# 变量

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
通过导入外部文件（json或者csv等）来获取变量，多用于数据驱动。具体用法是在Collection Runner中配置Data参数，详见数据驱动版块讲解。


# 断言
Tests模块
```

//判断是否包含字符串
pm.test("Body matches string", function () {
    pm.expect(pm.response.text()).to.include("string_you_want_to_search");
});

//将xml报文转换成json报文
var jsonObject = xml2Json(responseBody);


//判断是否相等
pm.test("Body is correct", function () {
    pm.response.to.have.body("response_body_string");
});

//判断json报文字段值是否相等
pm.test("Your test name", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.value).to.eql(100);
});

//判断响应头信息
pm.test("Content-Type is present", function () {
    pm.response.to.have.header("Content-Type");
});

//判断响应时间
pm.test("Response time is less than 200ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(200);
});
```

# 数据驱动 Data
在Collection Runner中配置Data外部数据。

```
Iterations: 迭代次数
Data：数据源
Data File Type：文件数据格式，推荐使用“application/json”


示例
GET:postman-echo.com/get?username={{username}}&age={{age}}
数据源：
[
    {"username":"manyan", "age":"18"},
    {"username":"cifer", "age":"19"},
    {"username":"sf","age":"100"}
]

```

# 工作流 flow
控制用例的执行顺序，实现方式有两种：手工拖动、脚本设置。Tests模块。
```
示例
要求：假设当前用例集中有4个接口用例，分别是request1,request2,request3,request4，当前需要控制用例的执行顺序为request1->request4->request2->request3。
实现：
(1)在request1的Tests中添加脚本：postman.setNextRequest('request4');
(2)在request4的Tests中添加脚本：postman.setNextRequest('request2');
```


# 命令行 CLI
需要使用的辅助应用是Newman，它是一款基于Node.js开发的，可以运行postman用例的工具。使用Newman可以很方便地从命令行直接运行和测试postman用例集。

```
前提：安装Newman V4.5.3
npm install newman --global
查看版本：newman -v

步骤一：导出用例集
选中用例集collection，执行Export导出，保存文件，例如 tbp_api_collection.json。

步骤二：执行命令
newman run tbp_api_collection.json -d data.json -r html

参数说明：
run：表示要执行的用例集文件，即导出的postman的collection文件。
-d：表示依赖的外部数据文件，即数据驱动所引用的数据源。如果不需要数据源，则可以省略。
-r：表示生成测试报告的格式。支持的格式有：json、html、junit。

备注1：必须在用例集文件的同级目录运行命令。
备注2：html报告模板需要自行npm安装：npm install newman-reporter-html --global才能使用。

步骤三：测试报告
运行完毕后，会在当前目录自动生成一个名为newman的文件夹，其中存放是的之前运行的测试结果。

```


# CI集成
在jenkins的构建项目的Execute Windows batch command中，添加newman执行命令即可。
```
newman run tbp_api_collection.json -d data.json -r html
命令释义：运行名为tbp_api_collection.json的用例集，同时引用数据源data.json文件，最终生成html格式的测试报告。
```


