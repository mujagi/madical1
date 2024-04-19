import random
c_number = [0]*13
for i in range(13):
    c_number[i] = i+1
c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# 랜덤으로 2개를 숫자를 뽑아서 출력하시오.
# 랜덤숫자 : 2 -> 1번방에 있습니다.
# 큰 수 : 9, 작은 수 : 2
ran_num = random.sample(c_number,k=2)
print(ran_num)
for i in ran_num:
    for j in range(len(c_number)):
        if i == j:
            print(f'랜덤숫자 : {i}, {j} 번째 방에 있습니다.')