####函数及调用  例子####
#def my_abs(x):
#    if x >= 0:
#        return x
#    else:
#       return -x
#print(my_abs(-99))

#定义函数
def Num(n):
    sum = 0
    while n > 0:
        sum = sum + n
        n = n - 2
        return sum

#调用函数
print(Num(99))