# 함수선언
def cal(num1,num2) :
    sum = 0
    temp = 0
    if num1>num2 :
        temp = num1
        num1 = num2
        num2 = temp
        # num1,num2 = num2,num1 # 2개 변수 치환 # 파이썬에서만 사용가능
    for i in range(num1,num2+1) :
        sum +=i
    return sum
        
        



# 두수를 입력받아, 입력한 사이의 합계를 구하는 프로그램을 구현하시오.
# ex) 1,10 -> 55 = 1+2+3.....=55
sum = 0
num1 =int(input("첫번째 숫자를 입력하세요.>>"))
num2 =int(input("두번째 숫자를 입력하세요.>>"))

sum = cal(num1,num2)
print("합계 :",sum)