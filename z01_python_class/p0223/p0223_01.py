# 출력 print()
print('문자열') # 문자열 출력
print(10.123) # 숫자 출력
print(123*111) # 사칙연산 후 출력


# %d 정수, %f 실수, %s 문자열을 나타낸다
print('%d %f %s'%(10,12.1234,'문자'))
print('%.2f'%(22.358894)) # 소수점 둘째자리까지 출력

# str. format()
print('문자열을쓰고 {}'.format(1))
# 정수
print("{0:d}".format(123)) # 다 같은값 예시
print('{0}'.format(123))
print("{}".format(123))
# 실수
print('{0:f}'.format(123.456789)) # 다 값은값 예시
print('{0}'.format(123.456789))
print('{}'.format(123.456789))

print('{:.1f}'.format(123.456789)) #  소숫점 한자리까지 나타내고 싶을 경우
# 문자
print('{0:s}'.format('문자'))
print('{0}'.format('문자'))
print('{}'.format('문자'))

print('{0} {1} {2}'.format('빨','주','노'))
print('{0} {2} {1}'.format('빨','주','노') )

#변수
number=10 #정수 - int
pi=3.14 #실수 - float
result=True #bool
str1 = '문장입니다'#string
ch = 'A' #문자
print(number)

s1 = '1+1=2'
print(s1)
s2 ='{}+{}={}'.format(1,1,2) 
print(s2) # 두 결과값이 같다
print('{}+{}={}'.format(1,1,2))# 두 결과값이 같다

a=100
a +=1 #a=a+1 같다
# +=, -+, *=, /=, //=, %=

a,b=10,20 #동일하다
a=10 #동일
b=20 #동일

# 참 거짓 출력
print(a==b)
print(a !=b) #같은지 물어보는 명령어
print(a>b)
print(a>=b)

#논리 연산자
#and (둘 다 참이여야 참) or (둘 중 하나만 참이여도 참)
#not (참=>거짓, 거짓=>참)

#and 예시
a,b,c=100,200,150
result=(a>c)and(b>c) #false and true
print(result)

#not 예시
r1 = True
print(not r1)

#입력받기 input()
name = input("이름을 입력하세요>>")
print("당신의 이름은 {}입니다.".format(name))
# iput()의 결과값은 문자형
age=input("나이를 입력하세요")
#ptint('당신은 내년에{}살입니다.'.format(age+1)) #age 값이 문자열이기 때문에 처리 안됨
print('당신은 내년에{}살입니다.'.format(int(age)+1)) # int로 숫자로 변경

# if 조건문
# if 조건문1 :
# : 실행문1
# [else :
# 실행문2]
# 조건문1이 참이면 실행문1을 실행 후 종료
# 조건문1이 거짓이면 실행문2를 실행 후 종료
f='apple'
if f=='apple':
    print('먹는다')
else:
    print('버린다')