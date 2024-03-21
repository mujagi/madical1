list = [1,2,3]
alist= [*list] #깊은복사
alist = list[:]  #깊은복사
list[0] = 100
print(alist)


a=100
b=a
a =10
print(a)