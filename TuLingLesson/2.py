class Student:
	# 这个类只定义了构造方法
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

def study_fn(self, language: str):
	print('study {} everyday'.format(language))

if __name__ == '__main__':
	stu = Student('叶良辰', 99)
	Student.study = study_fn
	stu.study('Chinese')