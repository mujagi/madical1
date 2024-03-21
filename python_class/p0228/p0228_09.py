from random import *
# 1. 변수선언 1~10
lotto=[]
# 2. 입력받은 숫자 6개
mynum = [2,5,1,9,3,7]
# 3. 로또 번호 생성하기

for i in range(6) :
    n = randint(1,10)
    lotto.append(n)


num = [1,2,3,4,5,6,7,8,9,10] # 특징 : 중복이 없다, 1~10까지
for i in range(10) :
    tmp = randint(0,9) # 0번방에서 9번방 사이의 랜덤한 숫자 생성
    print(tmp)
    num[0],num[tmp] = num[tmp],num[0]
    print(num)



for i in range(6) :
    lotto.append(num[i])
 

ok = []
for i in range(len(mynum)):
    print(mynum[i])
    if mynum[i] in lotto :
        ok.append(mynum[i])

print(ok)