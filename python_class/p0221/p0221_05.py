#변수
#int형 : 10진법 : 정수 1,2,3,...-1,-2,-3
num1=10
print(num1)
print(10)
num2=-100
print(num2)


#2진법:0b로 시작함
num3 = 0b101010
print(num3)


#8진법:0o로 시작함
num4=0o52
print(num4)


#16진법:0x로 시작함
# 1,2,3,4,5,6,7,8,9,a,b,c,d,e,f 의 수로 표현
num5=0x2a
print(num5)

#float형:실수 즉 소수점을 포함하고 있는 수
num6=3.14
print(num6)
print("%f"%num6)
num7=2*3.14*5
print(num7)

#complex형 : 실수+허수
# 3+2i 파이썬에서는 i대신j를 사용한다.
comp1=3+4j
print(comp1)
print(comp1.real)
print(comp1.imag)

#boolean형:True 참, False 거짓
bool1=True
bool2=False
print("bool1 : ",bool1)
print("bool2 : ",bool2)
bool3=(1==2)#False
print("bool3:",bool3)
bool4=(0x2a==42)#True
print("bool4:",bool4)

#String 형
str1 = "안녕하세요"
str2 = "hello"
print(str1)
print(str2)

#그외에 list,tuple,dict,set 등이 있음
