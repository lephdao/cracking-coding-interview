class IsUnique:
	def __init__(self, string):
		self.string = string

	def checkUnique(self):
		unique = 0
		list = []
		for s in self.string:
			for l in list:
				if s == l:
					unique = 1
					print(self.string)
					print("String is not unique")
					return
			list.append(s)
		if unique == 0:
			print(self.string)
			print("String is unique")

l = IsUnique('mooooomin')
l.checkUnique()

l1 = IsUnique('abcde fgh')
l1.checkUnique()

l2 = IsUnique('')
l2.checkUnique()

l3 = IsUnique('unique')
l3.checkUnique()

l4 = IsUnique("asdfghjkloiuytrewqzxcvbnm")
l4.checkUnique()

