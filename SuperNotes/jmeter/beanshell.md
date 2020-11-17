# 基本语法

## 数据类型

```
String s = 'a';
int i = 0;
```

#### 数组
```
String[] str1 = new String[]{"aa","bb","cc"};
String[][] str2 = new String[][]{{"AA","BB"},{"CC","DD"},{"EE","FF"}};
for(int i = 0; i< str1.length ; i++){
    log.info(str1[i]);
}
```

#### 集合
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


## 逻辑分支

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

## 函数

```
public void test(){
    log.info("do something")
}
```





# 常用内置对象


## cxt 上下文对象

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

## vars 用户自定义变量


系统内置定义：JMeterVariables vars=ctx.getVariables();

```
vars.put(String key,Value)放置一个Map到vars
vars.get(String key)获取String变量

 
vars.putObject("list",list);
Object Value = vars.getObject("list");
```





## prev

prev是Beanshell后置处理器的内置对象，

系统内置定义：SampleResult prev=ctx.getPreviousResult() ;



## props 全局变量

```
String response = prev.getResponseDataAsString();

如果对于json结果，可以参考使用fastJSON进行解析。

```




# 常用元件

## 逻辑控制器 Logic Controller

Logic Controllers determine the order in which Samplers are processed.

分类：
（1）控制测试计划执行过程中节点的逻辑执行顺序，如：Loop Controller、If Controller等
（2）对测试计划中的脚本进行分组、方便JMeter统计执行结果以及进行脚本的运行时控制等，如：Throughput Controller、Transaction Controller。

#### if控制器

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


---

引用fastjson

JAR包下载地址：`http://repo1.maven.org/maven2/com/alibaba/fastjson/1.2.47/`

JSONObject responseObj = JSON.parseObject(responseStr);

JSONArray listArray = resObj.getJSONArray("records");

```
int len = listArray.size();
for(int i=0;i<len;i++){
    temp[i]= listArray.getJSONObject(i).getString("DEVICE_ID");
}
```
