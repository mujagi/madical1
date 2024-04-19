
from random import*
# c_number = [0]*13
# for i in range(13) :
#     c_number[i] = i+1

c_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# # 랜덤으로 2개의 숫자를 뽑아서 출력하시오.

num = sample(c_number,k=2)
print(num)

#   랜덤숫자 2 >> 1번방에 있습니다. 
#   랜덤숫자 9 >> 8번방에 있습니다.
for i in num :
    for j in range(len(c_number)) :
        if i == j :
            print(f"랜덤숫자{i}은 {j}번째 방에 있습니다.")

#   큰수: 9, 작은수: 2
if num[0] > num[1] :
    print(f"큰 수 : {num[0]}, 작은 수 : {num[1]}")
else :
    print(f"큰 수 : {num[1]}, 작은 수 : {num[0]}")