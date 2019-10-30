class Person:
	def __init__(self, name: str):
		self.name = name

	def eat(self):
		print('{}是铁饭是钢'.format(self.name))

class Student(Person):
	def __init__(self, name):
		# 通过super()函数实例化super对象
		super().__init__(name)

class Teacher(Person):
	def __init__(self, name):
		# 通过super()函数传参实例化super对象
		super(Teacher, self).__init__(name)

class Programmer(Person):
	def __init__(self, name):
		# 通过类调用实例方法的方式实现，需要手动传参self
		Person.__init__(self, name)

if __name__ == '__main__':
	Student('学生').eat()
	Teacher('老师').eat()
	Programmer('程序猿').eat()