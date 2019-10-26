class Student:

	def __init__(self, name: str):
		self.name = name

	def read(self):
		print('{} finished reading.'.format(self.name))
		return self

	def write(self):
		print('{} finished writing.'.format(self.name))
		return self

	def exam(self):
		print('{} finished exam.'.format(self.name))
		return self

if __name__ == '__main__':
	Student('叶良辰').read().write().exam()