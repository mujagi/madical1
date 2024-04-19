# random 함수
from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(int(random()*10))# 0 ~ 10 미만의임의의 값 생성
# 1~10이하의 임의의 값 생성
print(int(random()*10)+1)
# 1 ~ 45 이하의 임의의 값 생성
print(int(random()*45)+1)

print(randrange(1,46))# 1~46 미만의임의의값 생성
print(randint(1,45)) # 1~45이하의 임의의 값 생성


# 해보세요 >>
# 1~10 사이의 숫자를 입력받아서
# 랜덤한 숫자와비교해 같으면 [당첨] 
# 다르면 [랜덤숫자는 {}로 일치하지 않습니다.]

i = int(input('숫자를 입력해주세요>>>'))
ran=(randint(1,10))
print(i)
if i == ran :
    print('당첨')
else  :
    print('랜덤숫자는 {}로 일치하지 않습니다'.format(ran))
    


