class Programmer:

    has_hair = True 	# 类属性

    def soul_torture(self):
    	self.has_hair = False	# 实例属性
    	self.has_mate = False


if __name__ == '__main__':
	p = Programmer()
	p.soul_torture()
	print('类属性：', Programmer.has_hair)
	print('实例属性：', p.has_hair)
	Programmer.has_hair = None
	print('实例属性：', p.has_hair)
