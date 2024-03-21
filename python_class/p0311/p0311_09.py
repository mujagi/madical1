def number(num1,num2,num3) :
    result = 0
    if num3 == "+" :
        result=num1+num2
    elif num3 == "-" :
        result=num1-num2
    elif num3 == "*" :
        result=num1*num2
    elif num3 == "/" :
        result=num1/num2
    return result

    

while True :
    input1 =int(input("첫번째 숫자를 입력하세요 >>>"))
    input2 =int(input("두번째 숫자를 입력하세요 >>>"))
    input3 = input("사칙연산을 입력하세요.")
    data = number(input1,input2,input3)
    print("결과값 :",data)

# 함수를 사용해서 입력된 두수의 사칙연산 결과값을 출력하시오.


# for i in range(10) :
#     sum = 0
#     sum += i
# print(sum)
# for i in range(5) :
#     result = 1
#     result += i
# print(result)





# def plus(v1,v2):
#     v1=v1+100
#     v2=v2+200
#     return v1,v2
    
    
# # 함수호출
# v1 = 1
# v2 = 2
# v1,v2 = plus(v1,v2)
# #출력
# print(v1,v2)