# 반복문
'''

for 변수 in range(시작값, 끝값+1, 증가값) :
'''

for i in range(3) :
    print('안녕')
    # i = 0 일때
    # i = 1 일때
    # i = 2 일때
    
for i in range(3) : # i = 0,1,2
    print(i)

# i = 0,1,2,3...
# i = 1,2,3,4...
for i in range(100) :
    print(i+1)

sum1 = 0
for i in range(1,6,1) :
    sum1 = sum1+1

# 숫자 한개를 입력 받아서 1부터 입력한 수 까지의 합을 구하세요

n = int(input('숫자를 입력해주세요 >>>'))
t = 0
for i in range(1,n+1) :
    if i%2 == 0 :
        t = t+i

print('{}부터{}까지의 합은 : {}입니다. '.format(2,n,t))
#짝수의 합만 구하기

# 1-10까지의 곱
x = 1
for i in range(1,11):
    x = x*i
print('{}부터{}까지의 곱은 : {}입니다. '.format(1,11,x))