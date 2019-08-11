
#### vue源码的下载地址：
```
vue1：http://v1-cn.vuejs.org/js/vue.js
vue2：https://unpkg.com/vue@2.2.1/dist/vue.js
vue2的router：https://unpkg.com/vue-router/dist/vue-router.js
```

#### vue常用指令
1.`{{}}` 

插值表达式。当模型中的数据发生变化时，视图中的数据也对应发生变化。

2.`v-text`

将一个变量的值渲染到指定元素中。

3.`v-html`

输出html元素。

4.`v-model`

实现数据双向绑定。

5.`v-bind`
绑定页面元素的属性。

6.`v-if`
控制是否加载固定的内容。如果是True，则加载进dom；否则移出dom。

7.`v-show`
控制是否显示内容。

v-if 和 v-show的共同点：都是控制元素的展现与否。
不同点：if是控制元素添加和移出dom树，show则是控制display属性。

if有更高的切换消耗，安全性高。show的初始化消耗高。如果需要频繁切换且对安全性要求不高时，
可以使用v-show。

8.`v-for`
控制元素的循环

9.`v-on`
绑定页面的事件。



#### 组件template


#### 路由router


### 项目实战

环境配置

```
1.安装node.js
从官网下载安装包进行安装。启动命令行，输入node -v如何显示版本号则表示安装成功。

2.安装脚手架
npm install -g vue-cli

3.初始化项目
使用在线模板：vue init webpack ShopDemo
使用本地模板：vue init webpack-simple ShopDemo
按照提示进行选择即可。

4.安装项目依赖
cd ShopDemo

5.运行项目
npm run dev

如果访问：http://localhost:8080/ 能够看到vue欢迎页面，则表示环境配置成功。

```

