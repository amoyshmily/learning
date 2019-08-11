# 表单开发


#### 表单介绍
表单是HTML页面中负责数据采集功能的部件。
组成：表单标签、表单域、表单按钮。

表单标签：用于声明表单的范围，位于表单标签中的元素将被提交。
语法：<form></form>
属性：method,enctype,action

表单域
包含了文本框、密码框等多种类型
语法：<input />
属性：type,name,value
种类：
- 文本框 type=text
- 密码框 type=password
- 文本域 type=textarea
- 文件上传框 type=file
- 单选框 type=radio
- 复选框 type=checkbox

表单按钮
- 提交按钮
- 复位按钮
- 一般按钮

```
# html

<body>
    <form name="form1" action="">

        <input type="text" placeholder="text" name="text1">
        <input type="password" placeholder="password" name="password"><br />

        <textarea placeholder="textarea" name="textarea" id="" cols="30" rows="10"></textarea><br />

        <input type="file" name="file"><br />

        <input type="radio" name="radioInp" value="option1" />option1
        <input type="radio" name="radioInp" value="option2" />option2
        <input type="checkbox" name="checkboxInp" value="option1" />option1
        <input type="checkbox" name="checkboxInp" value="option2" />option2<br/>

        <input type="submit" value="submit">
        <input type="reset" value="reset">
        <input type="button" value="button" onclick="getValue()">

    </form>

</body>

# js
function getValue(){
    var text = document.form1.text1.value;
    alert(text)

    var text2 = document.form1.radioInp.value;
    alert(text2)

    var arr = document.form1.checkboxInp
    alert(arr[0].value)
}

```

