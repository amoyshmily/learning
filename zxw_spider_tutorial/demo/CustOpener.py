from urllib import request

# 构建HTTP处理器对象
http_handler = request.HTTPHandler()

# 创建自定义的Opener
my_opener = request.build_opener(http_handler)

# 创建自定义请求对象
req = request.Request("http://www.baidu.com")

# 发送请求，获取响应
res = my_opener.open(req)
res_content = res.read().decode()

# 把自定义你的opener设置为全局
request.install_opener(my_opener)   # 后续即便是使用request.urlopen()走的也是此opener

print(res_content)

