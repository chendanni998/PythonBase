#class $tack:
#	def __init__(self,size):
#		self.__size = size
#		self.data = []
#	def getsize(self):
#		return self.__size
#	def push(self,a):
#		if len(self.data) < self.__size:
#			self.data.append(a)
#	def pop(self):

import requests

#1.抛异常  try...except

data={'login.py': 'a 8 d 2 u 3', 'order.py': 'a 15 d 0 u 34', 'info.py': 'a 1 d 20 u 5'}
for k,v in data.items():
	line=[]
	list=v.split('')
	for i in  list:
		try:
			line.append(int(i))
		except:
			pass
	print("")