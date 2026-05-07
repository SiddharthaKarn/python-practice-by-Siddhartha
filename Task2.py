# Task 2= Swap values of two variables and print before and after
#method 1 
a = 10
b = 20
print("before swap",a,b)
c = a # c=10
a = b # a=20
b = c # b=10
print("after swap",a,b)

#method 2

a = 10
b =20
print("before swap",a,b)
a = a+b # 10+20=30
b = a-b # 30-20=10
a = a-b # 30-10=20
print("after swap",a,b)

#method 3= only in python 
a =10
b =20
print("before swap",a,b)
a,b=b,a # only in python
print("after swap",a,b)
