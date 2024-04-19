# 랜덤으로 숫자 1개 생성 1-100
# 입력한 숫자보다 크면 작은수를 입력하시오
# 입력한 숫자보다 작으면 큰 수를 입력하시오. 라고 멘트가나오게
# 정답을 맞추면
# 현재까지 입력했던 숫자를 모두 출력하시오

import random

r_num = random.randint(1,100)
i_num = []
cnt = 0
while True :
    num = int(input("숫자를 입력해주세요>>"))
    cnt +=1
    if num > r_num :
        print("입력한 숫자보다 작은수를 입력하세요")
        
    elif num < r_num :
        print("입력한 숫자보다 큰수를 입력하세요")
        
    elif num == r_num :
        print("정답입니다.")
        break
    i_num.append(num)
print("{}번째 도전하셨습니다.".format(cnt))
print("현재까지 입력한 숫자 :",i_num)