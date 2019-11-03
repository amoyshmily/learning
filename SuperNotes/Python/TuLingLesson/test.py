class WeChat:
	name = '朋友圈'
	def interview(self, people):
		people.say(self.name)

class Passerby:
	def say(self, target):
		print('在{}底下评论：这两个人真傻，有驴不骑'.format(target))

class Man:
	def say(self, target):
		print('在{}底下评论：这女人真自私，逗不知道让男人一起骑驴'.format(target))

class Womam:
	def say(self, target):
		print('在{}底下评论：这男人真自私，自己骑却让女人在下面走'.format(target))

class Donkey:
	def say(self, target):
		print('在{}底下评论：人类真过分，竟然两个人骑着，一点都不知道爱惜动物'.format(target))

we = WeChat()
we.interview(Passerby())
we.interview(Man())
we.interview(Womam())
we.interview(Donkey())