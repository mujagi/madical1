# a = 1 # 변수
# print() # 이름 뒤에 () 있으면 함수
# # C1 # 클래스

# from co import machine
import p0311.co as co

coffee = 0

while True:
    print('1. 보통 커피')
    print('2. 설탕 커피')
    print('3. 블랙 커피')
    coffee = int(input('어떤 커피를 드릴까요? : '))
    print()
    # 함수 호출
    co.machine(coffee)
    