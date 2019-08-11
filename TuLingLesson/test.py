class PythonStudent():
	# 类属性
	name = 'Amoy'
	age = 18

	# 定义函数
	def introduce(self):
		msg = 'My name is {} and I\'m {} years old.'.format(self.name, self.age)
		print(msg)
stu = PythonStudent()
stu.introduce()