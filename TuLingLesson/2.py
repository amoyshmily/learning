



动态添加方法


当给对象动态增加方法时，Python不会自动将调用者绑定到它们的第一个参数，因此程序需要手动
为新增的方法传入参数值。

示例3
class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def study(self, language: str):
    	print('study {} everyday'.format(language))

if __name__ == '__main__':
	stu = Student(name='叶良辰', age=18)   # 实例化对象
	stu.study('Python')   # 调用方法

    # 动态添加方法：定义函数
	def fn(self):
		print(self.name, self.age, end='')		# 叶良辰 18

	stu.show = fn		# 动态添加方法
	stu.show(stu)	# 调用添加后的方法
	print(type(stu.show))		# <class 'function'>
	print(dir(stu))		# [...'name', 'age', 'study', 'show']
	
	# 动态添加方法：lambda表达式
	stu.sleep = lambda self: print(self.name+'晚上10点睡觉。')    # 叶良辰晚上10点睡觉。
	stu.sleep(stu)
	print(dir(stu))     # [...'name', 'age', 'study', 'show']
	
	# 删除方法
	del stu.show
	print(dir(stu))     # [...'name', 'age', 'study']
	

如果希望既能为对象动态添加方法，又能让其自动绑定到第一个参数，则可以借助types模块
的MethodType进行包装。

示例4
class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

if __name__ == '__main__':

	stu = Student(name='叶良辰', age=18)   # 实例化对象

    # 动态添加方法：定义函数
	def fn(self):
		print(self.name, self.age, end='')		# 叶良辰 18

	# 动态添加方法
	from types import MethodType
	stu.show = MethodType(fn, stu)		# 包装
	stu.show()	# 调用添加后的方法


动态绑定的首参self并不依赖方法的具体调用方式，不管是采用方法调用形式，还是函数调用形式来
执行它，self参数都一样可以自动绑定。

示例5
class Student:
    def study(self):
    	print(self)

if __name__ == '__main__':
	stu = Student()
	stu.study()		# <__main__.Student object at 0x00000000023E8240>

	fn = stu.study
	fn()		# <__main__.Student object at 0x0000000001E585C0>




class Student:
	room = '302'

	@classmethod
	def clean(cls):
		print('clean the classroom {}.'.format(cls.room))

	@staticmethod
	def study(course):
		print('study {}.'.format(course))

if __name__ == '__main__':
	Student.clean()
	Student.study('Python')
	
	stu = Student()
	stu.room = '303'
	stu.clean()
	stu.study('Python')