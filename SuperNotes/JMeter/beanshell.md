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

## vars 用户自定义变量
```
vars.put(String key,Value)放置一个Map到vars
vars.get(String key)获取String变量

 
vars.putObject("list",list);
Object Value = vars.getObject("list");
```



## cxt 调用请求/响应数据

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

## prev 

prev是Beanshell后置处理器的内置对象 相当于`ctx.getPreviousResult()`。


## props 全局变量