# JMeter学习笔记

## 一、前言



### 1.1 简介



​	Apache JMeter是Apache组织开发的基于Java的压力测试工具。用于对软件做压力测试，它最初被设计用于Web应用测试，但后来扩展到其他测试领域。 可以用于测试静态和动态资源，例如静态文件、CGI 脚本、Java 对象、数据库、FTP 服务器 等等。JMeter 可以用于对服务器、网络或对象模拟巨大的负载，来自不同压力类别下测试它们的强度和分析整体性能。

​	JMeter也称为“Apache JMeter”，它是一个开源的，100%基于Java的应用程序，带有图形界面。 它旨在分析和衡量Web应用程序和各种服务的性能和负载功能行为。

​	JMeter主要用于测试Web应用程序或FTP应用程序，但目前，它适用于功能测试，JDBC数据库连接，Web服务，通用TCP连接和OS本机进程。 您可以执行各种测试活动，如性能，负载，压力，回归和功能测试，以便针对您的Web服务器获得准确的性能指标。

​	JMeter最初是由Apache软件基金会的Stefano Mazzocchi编写和开发的。 它主要用于测试Apache JServ(目前称为Apache Tomcat项目)的性能。Apache重新设计了JMeter以增强GUI，增加更多功能和功能测试功能。

​	JMeter不是一个浏览器，它不像任何浏览器那样呈现html页面，而是在协议级别上运行。



### 1.2 特性

- 开源应用程序：JMeter是一个免费的开源应用程序，可以帮助用户或开发人员使用源代码开发其他应用程序。

- 用户友好的GUI：JMeter带有简单的交互式GUI。

- 支持各种测试方法:JMeter支持各种测试方法，如负载测试，分布式测试和功能测试等。
  - Web: HTTP, HTTPS, SOAP
  - 数据库: JDBC, LDAP, JMS
  - Mail: POP3

- 支持多协议：JMeter支持HTTP，JDBC，LDAP，SOAP，JMS和FTP等协议。

- 模拟：JMeter可以使用虚拟用户或唯一用户模拟多个用户，以便对正在测试的Web应用程序产生大量负载。

- 框架：JMeter是一个多线程框架，允许许多或单独的线程组同时和同时采样不同的函数。

- 远程分布式测试：JMeter具有用于分布式测试的主从概念，其中主服务器将在所有从服务器之间分配测试，而从服务器将针对服务器执行脚本。

- 测试结果可视化：测试结果可以以不同的格式查看，如图形，表格，树型和报告等。



### 1.3 工作流程

JMeter通过模拟一组用户将请求发送到目标服务器。 随后，收集数据以通过各种格式计算目标服务器的统计和显示性能度量。

![img](https://www.yiibai.com/uploads/images/2018/08/01/164815_79832.png)





### 1.4 安装

- JDK8

首先需要下载安装JDK，并配置环境变量。

 目前JMeter只支持到JDK8，尚不支持JDK9。

> 官网地址：https://www.oracle.com/java/technologies/javase-downloads.html



-  jmeter

推荐版本：apache-jmeter-4.0

> 官网地址：https://jmeter.apache.org/



### 1.5 运行

- GUI运行



- 非GUI运行



## 二、结构

主要组件：

- 测试计划

- 线程组

- 采样器

- 监听器

- 定时器

- 逻辑控制器

- 前置处理器

- 后置处理器

- 配置元件

- 断言

  

  



### 2.1 测试计划

可以将测试计划可视化为用于运行测试的JMeter脚本。 测试计划由测试元素组成，例如线程组，逻辑控制器，样本生成控制器，监听器，定时器，断言和配置元素。

测试计划包含执行脚本的所有步骤。 测试计划中包含的所有内容都按照从上到下的顺序执行，或者按照测试计划中定义的顺序执行。



Tips：

在运行整个测试计划之前，应保存测试计划。

JMeter文件或测试计划以`.JMX`扩展文件的形式保存。JMX是一种基于开放测试的格式，它使测试计划能够在文本编辑器中启动。

您还可以将测试计划的一部分保存为不同的选择。 例如，如果要使用侦听器保存HTTP请求采样器，可以将其保存为测试片段，以便它也可以在其他测试场景中使用。

![1616857586570](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616857586570.png)





### <font color='blue'>2.2 线程组</font>

线程组表示JMeter在测试期间将使用的线程组。 线程组元素是任何测试计划的起点。 

![1616857646926](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616857646926.png)



线程组控制面板包括:

- 线程组名称。
- 线程数：您正在测试的用户数
- 加速时间：您希望允许线程组从0到N个用户的时间。
- 循环计数：循环测试的次数

![1616857665961](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616857665961.png)



#### 元件树

线程组中，可以添加的元件有：

- Sampler（采样器）
  - **<font color='blue'>HTTP 请求</font>**
  - Test Action
  - Debug Sampler
  - AJP/1.3 Sampler
  - Access Log Sampler
  - BeanShell Sampler
  - FTP请求
  - JDBC Request
  - JMS Point-to-Point
  - JMS Publisher
  - JMS Subscriber
  - JSR223 Sampler
  - JUnit Request
  - Java 请求
  - LDAP Extended Request
  - LDAP Request
  - Mail Reader Sampler
  - OS Process Sampler
  - SMTP Sampler
  - TCP Sampler
- 逻辑控制器
  - <font color='blue'>**如果（if）控制器**</font>
  - 事物控制器
  - <font color='blue'>**循环控制器**</font>
  - While Controller
  - Critical Section Controller
  - ForEach控制器
  - Include Controller
  - 交替控制器
  - 仅一次控制器
  - 随机控制器
  - 随机顺序控制器
  - 录制控制器
  - Runtime Controller
  - 简单控制器
  - 吞吐量控制器
  - 模块控制器
  - Switch Controller
- 前置处理器
  - JSR223预处理器
  - <font color='blue'>**用户参数**</font>
  - HTML链接解析器
  - HTTP URL重写修饰符
  - JDBC预处理器
  - RegEx用户参数
  - Sample Timeout
  - <font color='blue'>**BeanShell预处理器**</font>
- 后置处理器
  - CSS/JQuery提取器
  - <font color='blue'>**JSON提取器**</font>
  - Boundary 提取器
  - <font color='blue'>**正则表达式提取器**</font>
  - JSR223后置处理器
  - Debug后置处理器
  - JDBC后置处理器
  - 结果状态操作处理程序
  - <font color='blue'>**XPath提取器**</font>
  - <font color='blue'>**BeanShell后置处理器**</font>
- 断言
  - <font color='blue'>**响应断言**</font>
  - <font color='blue'>**JSON断言**</font>
  - Size断言
  - JSR223断言
  - <font color='blue'>**XPATH断言**</font>
  - Compare断言
  - 断言持续时间
  - HTML断言
  - MD5Hex断言
  - SMIME断言
  - XML断言
  - XML Schema断言
  - <font color='blue'>**Bean Shell断言**</font>
- 定时器
  - 固定定时器
  - Uniform Random Timer
  - Precise Throughput Timer
  - Constant Throughput Timer
  - 高斯随机定时器
  - JSR223定时器
  - Poisson Random Timer
  - Synchronizing Timer
  - Bean Shell Timer
- Test Fragment
- 配置元件
  - <font color='blue'>**CSV数据文件设置**</font>
  - <font color='blue'>**HTTP信息头管理器**</font>
  - HTTP Cookie管理器
  - HTTP Cache管理器
  - HTTP请求默认值
  - 计数器
  - DNS Cache管理器
  - FTP请求默认值
  - HTTP授权管理器
  - <font color='blue'>**JDBC连接配置**</font>
  - Java请求默认值
  - 秘钥库配置
  - LDAP 扩展请求默认值
  - LDAP请求默认值
  - 登录配置元件
  - 随机变量
  - 简单配置元件
  - TCP取样器配置
  - <font color='blue'>**用户定义的变量**</font>
- 监听器
  - <font color='blue'>**查看结果树**</font>
  - Summary Report
  - <font color='blue'>**聚合报告**</font>
  - Backend Listener
  - Aggregate Graph
  - 断言结果
  - Comparison Assertion Visualizer
  - 生成概要结果
  - 图形结果
  - JSR223 Listener
  - 邮件观察仪
  - Response Time Graph
  - 保存响应到文件
  - Simple Data Writer
  - 用表格查看结果
  - Bean Shell Listener



![1616863200213](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616863200213.png)



### 2.3 采样器



采样器是允许JMeter将特定类型的请求发送到服务器的组件。它模拟用户对目标服务器的页面的请求。

采样器是必须将组件添加到测试计划中的，因为它只能让JMeter知道需要将哪种类型的请求发送到服务器。 请求可以是HTTP，HTTP(s)，FTP，TCP，SMTP，SOAP等。

菜单路径：线程组/添加/Sampler

![1616857794993](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616857794993.png)

采样器列表：

- **<font color='blue'>HTTP 请求</font>**
- Test Action
- Debug Sampler
- AJP/1.3 Sampler
- Access Log Sampler
- BeanShell Sampler
- FTP请求
- JDBC Request
- JMS Point-to-Point
- JMS Publisher
- JMS Subscriber
- JSR223 Sampler
- JUnit Request
- Java 请求
- LDAP Extended Request
- LDAP Request
- Mail Reader Sampler
- OS Process Sampler
- SMTP Sampler
- TCP Sampler



#### <font color='blue'>HTTP 请求</font>

（1）发送GET请求

![1616862997462](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616862997462.png)



（2）发送POST请求

![1616864125508](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616864125508.png)







### 2.4 监听器

性能测试就是以各种形式分析服务器响应，然后将其呈现给客户端。

当JMeter的采样器组件被执行时，监听器提供JMeter收集的关于那些测试用例的数据的图形表示。它便于用户在某些日志文件中以表格，图形，树或简单文本的形式查看采样器结果。

监听器可以在测试的任何地方进行调整，直接包括在测试计划下。JMeter提供了大约15个监听器，但主要使用的是表，树和图形。



![1616860144597](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616860144597.png)



- <font color='blue'>查看结果树</font>
- Summary Report
- <font color='blue'>聚合报告</font>
- Backend Listener
- Aggregate Graph
- 断言结果
- Comparison Assertion Visualizer
- 生成概要结果
- 图形结果
- JSR223 Listener
- 邮件观察仪
- Response Time Graph
- 保存响应到文件
- Simple Data Writer
- 用表格查看结果
- Bean Shell Listener



#### 查看结果树



#### 聚合报告



**聚合报告详解**

- Label：每个 JMeter 的 element（例如 HTTP Request）都有一个 Name 属性，这里显示的就是 Name 属性的值。
- \#Samples：请求数——表示这次测试中一共发出了多少个请求，如果模拟10个用户，每个用户迭代10次，那么这里显示100。
- Average：平均响应时间——默认情况下是单个 Request 的平均响应时间（ms），当使用了 Transaction Controller 时，以Transaction 为单位显示平均响应时间。
- Median：中位数，也就是 50％ 用户的响应时间
- 90% Line：90％ 用户的响应时间
- Min：最小响应时间
- Max：最大响应时间
- Error%：错误率——错误请求数/请求总数
- throughput：吞吐量——默认情况下表示每秒完成的请求数（Request per Second）
- KB/Sec：每秒从服务器端接收到的数据量，相当于LoadRunner中的Throughput/Sec









### 2.5 定时器

当您在网站或应用程序上执行任何操作时，它们自然会有暂停和延迟。 这些可以使用计时器(Timers)进行模拟。

JMeter发送请求时不会在每个采样器/请求之间应用延迟。 如果在服务器上执行负载/压力测试没有指定延迟，它将会超载。 这可能不完全是我们想要的。可以添加一个计时器元素，该元素允许您定义在每个请求到达时间等待的终止。

![1616860186586](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616860186586.png)



下面给出了JMeter提供的所有计时器元素的列表：

- 固定定时器
- Uniform Random Timer
- Precise Throughput Timer
- Constant Throughput Timer
- 高斯随机定时器
- JSR223定时器
- Poisson Random Timer
- Synchronizing Timer
- Bean Shell Timer









### 2.6 逻辑控制器

逻辑控制器可帮助您控制线程中采样器处理顺序的流程。 它还可以更改来自其子元素的请求的顺序。



![1616858169319](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616858169319.png)



以下是JMeter中所有逻辑控制器的列表：

- <font color='blue'>如果（if）控制器</font>

- 事物控制器

- <font color='blue'>循环控制器</font>

- While Controller

- Critical Section Controller

- ForEach控制器

- Include Controller

- 交替控制器

- 仅一次控制器

- 随机控制器

- 随机顺序控制器

- 录制控制器

- Runtime Controller

- 简单控制器

- 吞吐量控制器

- 模块控制器

- Switch Controller

  

分类：
（1）控制测试计划执行过程中节点的逻辑执行顺序，如：Loop Controller、If Controller等
（2）对测试计划中的脚本进行分组、方便JMeter统计执行结果以及进行脚本的运行时控制等，如：Throughput Controller、Transaction Controller。



#### 如果控制器if

菜单路径：添加/逻辑控制器/如果IF控制器

在if逻辑控制器的Expression中不能直接填写条件表达式，需要借助函数将条件表达式计算为true/false，可以借助的函数有__jexl3和__groovy函数。

勾选“Interpret Condition as Variable Expression?”，则指定为groovy脚本，否则默认视为JavaScript脚本。

> groovy脚本示例

```
${__groovy(vars.get('response').equals("true"))}
```

> JS脚本示例

```
"${response}" == "true"
```

------

```
int len = listArray.size();
for(int i=0;i<len;i++){
    temp[i]= listArray.getJSONObject(i).getString("DEVICE_ID");
}
```







### 2.7 前置处理器

预处理器元素在采样器发出请求之前执行，如果预处理器附加到采样器元素，那么它将在该采样器元素运行之前执行。
预处理器元素用于在运行之前修改样本请求的设置，或更新未从响应文本中提取的变量。



![1616860260518](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616860260518.png)



以下是JMeter提供的所有预处理器元素的列表:

- JSR223预处理器
- <font color='blue'>用户参数</font>
- HTML链接解析器
- HTTP URL重写修饰符
- JDBC预处理器
- RegEx用户参数
- Sample Timeout
- <font color='blue'>BeanShell预处理器</font>



#### 用户参数





### 2.8 后置处理器

在发出采样器请求之后执行后处理器元素。 如果后处理器连接到Sampler元素，那么它将在该sampler元素运行之后执行。

后处理器最常用于处理响应数据，例如，为了将来目的而提取特定值。

![1616860354685](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616860354685.png)



下面给出了JMeter提供的所有后处理器元素的列表：

- CSS/JQuery提取器

- <font color='blue'>JSON提取器</font>

- Boundary 提取器

- <font color='blue'>正则表达式提取器</font>

- JSR223后置处理器

- Debug后置处理器

- JDBC后置处理器

- 结果状态操作处理程序

- <font color='blue'>XPath提取器</font>

- <font color='blue'>BeanShell后置处理器</font>

  



#### Bean Shell



数据类型

```
String s = 'a';
int i = 0;
```

数组

```
String[] str1 = new String[]{"aa","bb","cc"};
String[][] str2 = new String[][]{{"AA","BB"},{"CC","DD"},{"EE","FF"}};
for(int i = 0; i< str1.length ; i++){
    log.info(str1[i]);
}
```

集合

```
//list集合只能保存String类型
List li = new ArrayList();
li.add("a");
li.add("b");
```

> 遍历

```
for(int i = 0; i < list.size(); i++){
log.info(list.get(i));
}
```

逻辑分支

```
if(i>0){
    log.info("do something")
}

for(int i=0; i< 5; i++)){
    log.info(""+i)
}

for(item:li){
    log.info(item)
}
```

函数

```
public void test(){
    log.info("do something")
}
```





常用内置对象

cxt 上下文对象

```
//SampleResult需要import对象
import org.apache.jmeter.samplers.SampleResult;

SampleResult result = ctx.getPreviousResult();

//getRequestHeaders()方法返回String字符串
String RequestHeaders = result.getRequestHeaders();

//getResponseHeaders() 返回响应headers
String ResponseHeaders = result.getResponseHeaders() 

//getResponseCode() 返回响应状态码字符串
String responseCode = result.getResponseCode();

//getURL() 返回请求URL对象 
URL url = result.getURL();
log.info(RequestHeaders);
log.info(RequestHeaders);


```

 vars 用户自定义变量

系统内置定义：JMeterVariables vars=ctx.getVariables();

```
vars.put(String key,Value)放置一个Map到vars
vars.get(String key)获取String变量

 
vars.putObject("list",list);
Object Value = vars.getObject("list");
```





prev

prev是Beanshell后置处理器的内置对象，

系统内置定义：SampleResult prev=ctx.getPreviousResult() ;



props 全局变量

```
String response = prev.getResponseDataAsString();

如果对于json结果，可以参考使用fastJSON进行解析。

```



引用第三方JAR包

示例：fastjson

JAR包下载地址：`http://repo1.maven.org/maven2/com/alibaba/fastjson/1.2.47/`



```
JSONObject responseObj = JSON.parseObject(responseStr);

JSONArray listArray = resObj.getJSONArray("records");


int len = listArray.size();
for(int i=0;i<len;i++){
    temp[i]= listArray.getJSONObject(i).getString("DEVICE_ID");
}
```



#### JSON提取器





#### 正则表达式提取器







### 2.9 配置元件

配置元素的工作与采样器的工作类似。但是，它不发送请求，但它允许修改采样器发出的请求。

这是一个简单的元素，您可以在其中收集所有采样器的关联配置值，如webserver的主机名或数据库URL等。

配置元素只能从放置元素的分支内部访问。



![1616860466791](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616860466791.png)





下面给出了JMeter提供的一些最常用配置元素的列表：

- <font color='blue'>CSV数据文件设置</font>
- <font color='blue'>HTTP信息头管理器</font>
- HTTP Cookie管理器
- HTTP Cache管理器
- HTTP请求默认值
- 计数器
- DNS Cache管理器
- FTP请求默认值
- HTTP授权管理器
- <font color='blue'>JDBC连接配置</font>
- Java请求默认值
- 秘钥库配置
- LDAP 扩展请求默认值
- LDAP请求默认值
- 登录配置元件
- 随机变量
- 简单配置元件
- TCP取样器配置
- <font color='blue'>用户定义的变量</font>



#### CSV数据文件设置





#### JDBC连接配置

连接数据库，可以执行SQL语句。

![1616689696643](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616689696643.png)





### 2.10 断言

判断测试的结果是否符合预期。

![1616864571736](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\1616864571736.png)

JMeter支持的断言方式：

- <font color='blue'>响应断言</font>
- <font color='blue'>JSON断言</font>
- Size断言
- JSR223断言
- <font color='blue'>XPATH断言</font>
- Compare断言
- 断言持续时间
- HTML断言
- MD5Hex断言
- SMIME断言
- XML断言
- XML Schema断言
- <font color='blue'>Bean Shell断言</font>













---



















## 三、进阶

### 3.1 函数

JMeter函数可以称为特殊值，可以填充测试树中任何Sampler或其他元素的字段。

JMeter中函数的语法:

```
${__functionName(var1,var2,var3)} ,
```

这里`__ functionName`匹配函数的名称，圆括号围绕发送给函数的参数。

如果函数参数包含逗号，那么请务必使用`“\”`对其进行转义，否则JMeter会将其视为参数分隔符。
例如:

```
${__time(EEE\, d MMM yyyy)}
```



常用函数列表

| 函数类型 | 名称                 | 说明                                   |
| -------- | -------------------- | -------------------------------------- |
| 信息     | threadNum            | 获取线程号                             |
| 信息     | samplerName          | 获取采样器名称(标签)。                 |
| 信息     | log                  | 记录(或显示)消息(并返回值)。           |
| 信息     | machineName          | 获取本地计算机名称。                   |
| 输入     | StringFromFile       | 从文件中读取一行。                     |
| 输入     | FileToString         | 读取整个文件。                         |
| 输入     | CSVRead              | 从CSV分隔文件中读取。                  |
| 输入     | XPath                | 使用XPath表达式从文件中读取。          |
| 计算     | Counter              | 生成递增数字。                         |
| 计算     | intSum               | 相加int数字。                          |
| 计算     | longSum              | 相加long数字。                         |
| 计算     | Random               | 生成一个随机数。                       |
| 计算     | RandomString         | 生成随机字符串。                       |
| 脚本     | BeanShell            | 运行BeanShell脚本。                    |
| 脚本     | javaScript           | 运行javaScript脚本。                   |
| 脚本     | jexl, jexl2          | 评估Commons Jexl表达式。               |
| 属性     | Property             | 读取property文件。                     |
| 属性     | P                    | 读取一个属性(速记方法)。               |
| 变量     | Split                | 将字符串拆分为变量。                   |
| 变量     | eval                 | 评估变量表达式。                       |
| 字符串   | regexFunction        | 使用正则表达式解析先前的响应。         |
| 字符串   | escapeOroRegexpChars | 引用ORO正则表达式使用的元字符。        |
| 字符串   | Char                 | 从数字列表生成Unicode char值。         |
| 字符串   | Unescape             | 包含Java转义的进程字符串(例如\n＆\t)。 |
| 字符串   | unescapeHtml         | 解码HTML编码的字符串。                 |
| 字符串   | escapeHtml           | 使用HTML编码对字符串进行编码。         |
| 字符串   | TestPlanName         | 返回当前测试计划的名称。               |



备注：JMeter函数和变量始终区分大小写





### 3.2 持续集成

ant

Jenkins



## 四、实战



### 4.1 接口测试



添加线程组

添加HTTP请求

配置请求的URL，路径等参数

添加查看结果树

发起请求，查看返回结果



### 4.2 性能测试











