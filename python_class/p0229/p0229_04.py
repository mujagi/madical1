
# 숫자 두개를 입력받고,
# 연산자를 입력받아서 (+-*/)
# 무한한 계산하는 계산기를 만드는데
# 첫번째 숫자에 0을 입력하면 프로그램이 종료가 되는 코드를 만드세요
while True :
    num1 = (int(input('숫자 1 >>>')))
    if num1 == 0 :
        print('종료되었습니다')
        break 
    num2 = (int(input('숫자 2 >>>')))
    x = input('부호를 입력해주세요 >>>')
    if x == '+' :
        print('{}+{}={}'.format(num1,num2,num1+num2))
    elif x == '-' :
        print('{}-{}={}'.format(num1,num2,num1-num2))
    elif x == '*' :
        print('{}*{}={}'.format(num1,num2,num1*num2))
    elif x == '/' :
        print('{}/{}={}'.format(num1,num2,num1/num2))
        
        
        

    

