import random

a = "1조123456"
b = "1조123456"
cnt = 0
for i in range(len(a),0,-1) :
    if i == 2 : continue # 조는 건너뛰기
    if a[i-1] != b[i-1] :
        break
    else :
        cnt+=1 # 맞는 회수 1증가

if cnt == 0 :
    print("완전 꽝입니다.")
elif cnt == 1:
    print("1만원 당첨입니다.")
elif cnt == 2:
    print("10만원 당첨입니다.")
elif cnt == 3:
    print("100만원 당첨입니다.")
elif cnt == 4:
    print("1000만원 당첨입니다.")
elif cnt == 5:
    print("1억 당첨입니다.")
elif cnt == 6:
    print("10억 당첨입니다.")
elif cnt == 7 :
    print("100억 당첨입니다.")

