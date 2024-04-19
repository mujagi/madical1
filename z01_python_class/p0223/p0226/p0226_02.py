# 해보세요
# 나이가 10살 이상이고 키 150이상만 탑승가능
# 나이, 키를 입력받아
# [탑승가능][탑승불가능]을 출력해보세요
age,tall= int(input('나이를 입력해주세요>>>')), int(input('키를 입력해주세요'))
if age >= 10 :
    if tall >=150 :
        print('탑승가능')
else :
    print('탑승 불가능')

# 2.숫자 3개 (정수)를 입력받고, 연산 1개를 입력받아
# +++,---,***,/// (나누기값은 둘째 자리까지 표현)
# ex) a+b+c=d 의 형태로 출력 (1+2+3=6)

num1, num2, num3 = int(input('숫자를 입력해주세요>>>')), int(input('숫자를 입력해주세요>>>')), int(input('숫자를 입력해주세요>>>'))
n=input('기호를 입력해주세요>>>')
if n == '+' :
    print('{}+{}+{}={}'.format(num1,num2,num3,num1+num2+num3))
elif n == '-' :
        print('{}-{}-{}={}'.format(num1,num2,num3,num1-num2-num3))
elif n == '*' :
    print('{}*{}*{}={}'.format(num1,num2,num3,num1*num2*num3))
elif n == '/' :
    print('{}/{}/{}={:.2f}'.format(num1,num2,num3,num1/num2/num3))


