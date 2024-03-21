#점수를 입력받아서
# 90점 이상이면 A 80점 이상이면 B 70점 이상이면 c, 나머지는 f를 출력해보세요

n=int(input('점수를 입력해주세요>>'))
if n>=90 :
    if n>=98 : 
        print('A+입니다')
    if n>93:
        print('A입니다')
    if n>90 :
        print('A-입니다')
    
elif n>=80 :
    if n>=88 : 
        print('B+입니다')
    if n>84:
        print('B입니다')
    if n>80 :
        print('B-입니다')
elif n>=70 :
    if n>=78 : 
        print('B+입니다')
    if n>74:
        print('B입니다')
    if n>70 :
        print('B-입니다')
else:
    print('f입니다')

#2. 98점 이상 a+, 90~93 사이는 A-
#b+,b-,c+,c- (중첩 if)
