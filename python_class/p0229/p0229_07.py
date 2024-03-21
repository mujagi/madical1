from random import *
# 랜덤한 숫자를 만들어서 (1~100 사이)
# 내가 입력한 값이 랜덤한 숫자랑 같으면 당첨,
# 아니면 다시 입력해주세요
# 를 출력하는 프로그램을 만들어보세요
r = randint(1,100)
# 1. 현재 입력한 숫자 모두를 inputlist에넣으세요
inputlist = []
# 2. 10회 도전 후 프로그램이 종료 되게 해주세요

for i in range(3) :
        num = int(input('숫자 >>>'))
        inputlist.append(num)
          
        if r == num:
            print('당첨')
            break
        elif r>num :
            print('더 큰 수를 입력해주세요')
        elif r<num :
            print('더 작은 수를 입력해주세요')
print('종료되었습니다')    
    


    