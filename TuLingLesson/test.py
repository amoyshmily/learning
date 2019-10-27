num = 3
def eat():
	print('全局空间的eat方法，num={}'.format(str(num)))

class Student:
	num = 4
	def eat(self):
		print('Student空间的eat方法，num={}'.format(self.num))

if __name__ == '__main__':
	eat()
	print(num)
	stu = Student()
	Student.eat(stu)
	print(Student.num)