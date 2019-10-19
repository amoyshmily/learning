def tellHobby(name, *hobbies):
	print(type(hobbies))
	print(hobbies)
	print('我叫“%s”，我喜欢%s' %(name, hobbies))
if __name__ == '__main__':
	tellHobby('cifer', 'coding', 'fishing', 'cooking')
