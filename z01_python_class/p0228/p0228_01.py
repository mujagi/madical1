''' 
반복문
for 변수 in 반복가능한데이터 :
    실행문
'''
# 순차적으로 커질때는 range를 사용한다.
for i in range(0,3,1) : # range(시작값,끝값+1, 증감값)
    print('hi')       # i가     0      2+1    1
    # i = 0 일 때, hi
    # i = 1 일 때, hi
    # i = 2 일 때, hi

for i in range(5): # i가 0부터 4까지 반복해라 > 5번 반복해라
    print(1)

for i in range(1,11) :
    print(i)

print('-'*35)
a = 10  
b = '안녕하세요'
# a,b를 5번 반복해서 출력
for i in range(5): # i 는 0~4
    print(i)
    a = a+1
    print(a)
    print(b)
# i = 0, i = 0 , 10+1 >11
# i = 1 , i = 1 , 11+1 > 12
# i = 2 , i = 2 , 12+1 > 13
name = input('이름 >>>')
score = int(input('점수 >>>'))


# 입력 : 이름, 점수 (5명의 이름과 점수를 입력받습니다.)
# 60점 이상이면 합격, 60점 미만이면 불합격을 출력하는데
# 출력의 형태는 [홍길동님 합격입니다][홍길동님 불합격입니다]
for i in range(5) :
    name = input('이름 >>>')
    score = int(input('점수 >>>'))

    if score >= 60 :
        print('{}님 합격입니다'.format(name))
    else :
        print('{}님 불합격입니다'.format(name))

