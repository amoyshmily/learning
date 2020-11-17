import enum

class Gender(enum.Enum):
	MALE = '男', '貌似潘安'
	FEMALE = '女', '含羞闭月'

	def __init__(self, cn_name, desc):
		self.cn_name = cn_name
		self.desc = desc

	@property
	def desc(self):
		return self._desc

	@desc.setter
	def desc(self, desc):
		self._desc = desc

	def info(self):
		print('枚举成员是：{}, {}'.format(self.value, self.desc))

if __name__ == '__main__':
	print(Gender.MALE)
	print(Gender['FEMALE'])
	print(Gender['FEMALE'].value)
	Gender.MALE.info()

