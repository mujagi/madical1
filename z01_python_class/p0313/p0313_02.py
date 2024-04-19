# 함수선언 : def 이름 () 정의
# 함수값은 return
# 함수호출 : 이름()
# 매개변수 개수는 항상 같아야하고
# 가변매개변수 선언 *values, 가변매개변수는 일치하지 않아도 된다.
# 리스트, 딕셔너리 매개변수는 주소값이 전달이 된다.

# 퀴즈1
# 함수를 사용하여 두수를 입력받아, 더하기, 빼기, 곱하기, 나누기 결과값을 출력하시오.

def cal(num1,num2) :
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    print(num1/num2)

    
    
    
    
    
num1 = int(input("첫번째 수를 입력해주세요."))
num2 = int(input("두번째 수를 입력해주세요"))
cal(num1,num2)
print(cal)    
    
# 두수  입력을 받아 값을 리턴받은 다음, 출력하시오
# def cal(num1,num2,num3) :
#     sum = 0
#     if num3 == "+" :
#         sum = num1+num2
#     elif num3 == "-" :
#         sum = num1-num2
#     elif num3 == "*" :
#         sum = num1*num2
#     elif num3 == "/" :
#         sum = num1/num2
#     return sum
    
    

# num1 = int(input("첫번째 수를 입력해주세요."))
# num2 = int(input("두번째 수를 입력해주세요."))
# num3= input("부호를 입력해주세요")
# data = cal(num1,num2,num3)
# print("결과값:",data)
