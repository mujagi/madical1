from random import *

n1 = randrange(1,10) # 1~9 사이의 정수
n2 = randrange(1,10) # 0~10 사이의 정수
n3= randint(1,10) # 1~10 사이의 정수
n4 = randrange(1,10)
n5 = randrange(1,10)
n6 = randrange(1,10)

print(n1,n2,n3)


lotto = []
# lotto 에 1~10사이의 랜덤한 숫자 6개를 넣어보세요
for i in range(6) :
    a= randint(1,10)
    lotto.append(a)
print(lotto)
mynum = []
# 내가 직접 입력한 숫자 6개를 넣어보세요
for i in range(6) :
    n = int(input('숫자 입력 >>>'))
    mynum.append(n)
print(mynum)
