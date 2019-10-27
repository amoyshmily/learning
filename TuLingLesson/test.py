
def fx(fn):
	print('函数fx执行')
	def fz(*args):
		print(fn.__name__)
		fn()
	return fz

@fx
def fy():
	print('函数fy执行')
	print('fy = \'这是装饰函数返回值\'')

if __name__ == '__main__':
	print(type(fy))
	print(fy)