from random import *
# 1~45까지의 숫자를 넣어서
lotto = [] # 1~45사이의 랜덤한 숫자 6 자리 지정(6개)
mynum = [] # 입력을 1~45 사이의 숫자를 입력받음
l = []
oknum = []
for i in range(1,46) :
    l.append(i)


for i in range(50) :
    tmp = randint(0,44)
    l[0],l[tmp] = l[tmp],l[0]

for i in range(6):
    lotto.append(l[i])
    #랜덤하고 중복이없는 숫자 6개 생성
print(lotto)
        
    
    

for n in range(6) :
    number = int(input('숫자 >>>'))
    mynum.append(number)
print(mynum)

#4. 입력숫자와 랜덤숫자 비교 같은거 출력
for i in range(6) :
    if mynum[i] in lotto :
        oknum.append(mynum[i])
print('당첨된 숫자 : {}'.format(oknum))
    