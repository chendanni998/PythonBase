#高阶函数
#1.map
import unittest
#class Getparams(unittest.TestCase):
def f(x):
	return x * x
map1 = map(f,[1,2,3,4,5,6,7,8,9])
print(list(map1))

#匿名函数lambda：
  #（1）不能包含命令；		（2）只能返回一个表达式.
  #（2）格式：冒号前是参数，可以有多个，用逗号隔开，冒号右边的为表达式。
# 其实lambda返回值是一个函数的地址，也就是函数对象。

map2 = map(lambda m : m * m,[1,2,3,4,5,6,7,8,9])
print(list(map2))

a = lambda n : n * n
print(a(3))

#2.reduce
 #注：在Python 3里，reduce()函数已经被从全局名字空间移除，现在被放在fucntools模块里，
 #所以，用的话要先引入：	from functools import reduce

from functools import reduce
map3 = reduce(lambda x,y : x + y,[1,2,3,4,5])
print(map3)

#3.filter过滤

def T(t):
	return t % 2 == 0
map4 = filter(T,[1,2,3,4,5])
print(list(map4))

#4.sorted排序
 #（1）默认从小到大排序，升序

print(sorted([33,-2,100,0,9,0.4]))

 #（2）高阶函数，可以接受一个key函数来实现自定义排序
 #按照绝对值排序
print(sorted([33,-2,100,0,9,0.4],key=abs))
 #反值reverse
def R(t):
	return t[0].lower()
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=R,reverse=True))


#返回函数
#1.可变参数
def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax
print(calc_sum(1,2,3))
#def cdn(*n):
#	return n
#print(cdn(2,3,4))

def person(name,age,**kw):
	if 'city' in kw:
		pass
	if 'job' in kw:
		pass
	#print('name:',name,'age','other:',kw)
	print('name:',name,'age','other:',kw)

#http://192.168.2.111:8000/lehome/event/api/add?title=python大会&time=2018-01-06
protocol = 'http'
domain = '192.168.2.111'
port = str(8000)
url = 'lehome/event/api/add'
data = "title='python大会'&time='2018-01-06'"
print(protocol+'://'+domain+':'+port+'/'+url+'?'+data)

