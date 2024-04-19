import random

from random import *
# 0.00000000 - 0.9999999 랜덤으로 소수점의 결과값 리턴
print(random())
# 10 과 20 사이의 소수점 결과값 리턴
print(uniform(10,20))

# 0-2까지의 랜덤숫자 리턴 3 포함 x
print(randrange(3))

# 리스트 내에 랜덤 1개 선택
print(choice([1,2,3,4,5]))

# 리스트의 요소를 랜덤으로 섞음
a_list = [1,2,3,4,5]
shuffle(a_list) # 출력을 하는것이 아니라, a_list 결과를 저장
print(a_list)

# k = 숫자  만큼 리스트에서 랜덤으로 뽑아냄
print(sample([1,2,3,4,5],k=2))

# 범위 내 랜덤int를 선택
print(randint(1,10))







# print(math.sin(1))
# print(math.cos(1))
# print(math.tan(1))
