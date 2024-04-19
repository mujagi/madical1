from random import *

n1 = randrange(1,11) # 1 ~ 10 까지의 정수
n2 = randint(1,10) # 1~10 까지의 정수

# 랜덤한 숫자 6개  lotto 리스트에 넣고
# 내가 입력한 숫자 6개는 mynum 리스트에 넣어주세요
lotto = []
mynum = []
for i in range(6) :
    n2 = randint(1,10)
    lotto.append(n2)
print(lotto)
for n in range(6):
    num = int(input('숫자 >>> '))
    mynum.append(num)

for i in range(6) :
    tmp =randint(1,10)
    # 만약에 랜덤숫자 (tmp)가 lotto 리스트에 없다면
    if tmp not in lotto :
        lotto.append(tmp)



f=['딸기', '포도']
if '딸기' in f :
    print('딸기가 있습니다')
