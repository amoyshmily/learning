def introduce(name, age):
	msg = '大家好！我的名字叫“%s”, 今年“%s”岁。'  %(name, age)
	print(msg)

if __name__ == '__main__':
	tup = ('公主', '19')
	li = ['王子', '20']
	dic = {'age': '21', 'name': '骑士'}
	introduce('cifer', '18')	# 普通青年
	introduce(*tup)		# 文艺青年
	introduce(*li)
	introduce(**dic)