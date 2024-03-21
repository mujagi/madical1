# 1~25까지 숫자를 랜덤으로 섞은 다음
# 2차원 리스트에 넣어보세요.
import random

num = random.randint(1,100)


# 숫자맞추기 프로그램을 구현
# 1-10까지 숫자 랜덤으로생성 숫자를 맞추는 프로그램입니다.
cnt = 1
a = []
print("정답",num)
while True:
    in_num = int(input("1-100까지의 숫자를 입력하세요."))
    a.append(in_num)
    print(a)
    if num>in_num :
        print("입력한 숫자보다 더 큽니다.")
    elif num < in_num :
        print("입력한 숫자보다 더 작습니다.")
    else :
        print("{}번째만의 정답입니다.".format(cnt))
        print("정답입니다.")
        break
    cnt+=1