print("Hello python")
print("Hello!"*3)
print("혼자 공부하다 모르면 강의를 참고하세요!")

#  참 / 거짓
print( 5>10) # false
print(5<10) #True
print(True)
print(False)
# prin(true)는 문자취급
print(not True) #False
print(not (5>10))# True
#"" ''안에 들어가면 문자취급
print("0")
print(0*10) # 0
print("0"*10)

print(100)#숫자
print('100')#answk

print("100+100")
print(100+100)

print("숫자는 %d"%200)
print("%d" %200)
print("%d+%d=%d"%(2,3,2+3))
# 서로짝이맞지않으면 오류발생

print("%d*%d=%d"%(2,1,2))
print("%d*%d=%d"%(1,2,1*2))

#깔끔한 출력
print("%d"%123)
print("%7d"%123) # 7자리숫자를보여줌, 빈공백으로채움
print("%05d"%123)

# %d:정수
# %f:실수
print("%d"%123.45)
print("%f"%123.45)

print("%7.1f"%123.45)
print("%07.1f"%123.45) #소숫점을 포함해서 총 7자리출력
#빈 공백으로 채움, 소숫점이하는 1자리까지표현
# 소숫점이하는 3자리로 표현하고 빈 공백은 0으로 채움
print("%07.3f"%123.45)
print("%.2f" %12.3456)
print("%.3f"%12.234567)

#문자열은 %s 를 사용
print('안녕하세요')
print("%s"%"반갑습니다")

# 문자 하나는 %c
print("%c"%'a')


print("%.2f"%758.12345678) #소수점 둘째까지
print("%010.2f"%25.05)# 총10자리 빈칸은0으로 채워 소수점2자리까지
print('%d'%150.15)# 변수150.15 정수,실수,문자열로 출력
print('%.2f'%150.15)
print('%s'%"150.15") #문자로 취급위해 "",'' 사용필요
print("*"*10)#*을 10개 출력 

