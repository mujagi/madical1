
# 0~20 사이의 5의 배수로 이루어진 리스트를 만들어보세요
# 출력 : [0,5,10,15,20]
num=[]
for i in range(21) :
    if i%5 == 0 :
        num.append(i)
print(num)

lan =['c','python','java','jquery','css']


# 1. 하나하나 출력해보기
# 1) in 리스트명 사용
for i in lan :
    print(i)
# 2) in range()사용
for i in range(len(lan))  :
    print(lan[i])
# 2. 1.c, 2.python, 3. java 이렇게 출력해보기
for i in range(1,6,1) : # i= 0,1,2,3,4...
    #print(i)
    #print(lan[i])
    print('{}.{}'.format(i,lan[i-1]))

num = [1,-1,2,3,-4,5,6,-8,9,-10]
# 양수면 양수 음수면 음수
# 1: 양수
# -1  : 음수
# 2 : 양수..
for i in num : # num에 있는 각각의 값이 i로 처리가 됨
    print(num, end = ' : ')
    if i >=0 :
        print('양수')
    elif i<=0 :
        print('음수')
print()
n = len(num)
# num = [1,-1,2,3,-4,5,6,-8,9,-10]
# num[0] = ? # num[0] = 1
for i in range(n) : # i: 0,1,2,3
    print(i)
    if num[i] >= 0 : # i = num[0]부터 시작 즉 num[i]는 num[0]과 동일 
        print('{}:양수'.format(num[i]))
    else :
        print('{}:음수'.format(num[i]))