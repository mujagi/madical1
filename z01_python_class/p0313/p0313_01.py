# 함수선언 : def 이름 () 정의
# 함수값은 return
# 함수호출 : 이름()
# 매개변수 개수는 항상 같아야하고
# 가변매개변수 선언 *values, 가변매개변수는 일치하지 않아도 된다.
# 리스트, 딕셔너리 매개변수는 주소값이 전달이 된다.

# 퀴즈1
# 함수를 사용하여 두수를 입력받아, 더하기, 빼기, 곱하기, 나누기 결과값을 출력하시오.

def cal(num1,num2) :
    r_list = [0]*6
    r_list[0] = num1
    r_list[1] = num2
    r_list[2] = num1+num2
    r_list[3] = num1-num2
    r_list[4] = num1*num2
    r_list[5] = num1/num2
    return r_list
# 
save_list = []

while True :
    num1 = int(input("첫번째 수를 입력해주세요.(0.종료)"))
    if num1 == 0 :
        break   
    num2 = int(input("두번째 수를 입력해주세요"))
    r_list = cal(num1,num2)
    save_list.append(r_list)
    
    print("{},{} 결과값 :{},{},{},{}".format(num1,num2,*r_list))  


# 현재까지 입력한 숫자와 결과값을 모두 출력을 해보세요.
for i in save_list :
    print("[현재까지 입력한 숫자 {},{}, 결과값 : {},{},{},{}]".format(*i))











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
