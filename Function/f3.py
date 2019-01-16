####高级特性####

#1、切片append
L = ['Danny','Liming','jenny']
r = []
n = 3
for i in range(n):
	r.append(L[i])

print(r)

#2.列表生成式list
a = list(range(1,11))
print(a)

#结果：[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#list生成式的循环
b = [x * x for x in range(1, 11)]
print(b)

c = [x * x for x in range(1,11) if x % 2 == 0]
print(c)

d = [m + n for m in 'ABC' for n in 'abc']
print(d)

#list生成式列出目录下的所有文件和目录名
import os
dir = [d for d in os.listdir('.')]
print(dir)

#循环使用多个变量
data = {'x':'1','y':'2','z':'3'}
result = [k + '=' + v for k,v in data.items()]
print(result)

#大小写字母转换  lower() 和 upper()
name = ['DANNY','HELLO']
change = [q.lower() for q in name]
print(change)

name1 = ['danny','hello']
change1 = [q.upper() for q in name]
print(change1)
