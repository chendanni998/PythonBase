####递归函数####

#例子一
def fact1(n):
    if n==1:
        return 1
    return n * fact1(n - 1)

print(fact1(5))

#result:5*4*3*2*1=120

#例子二
def fact2(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact2(5))

#练习一
def move(n,a,b,c):
    if n == 1:
        print('move',a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
print(move(3,'a','b','c'))
