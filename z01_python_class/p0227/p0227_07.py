# 1 - 5 까지의 합계를 구하세요
sum = 1+2+3+4+5
print(sum)
total=0 # t=0
total=total+1 # t = 1
total=total+2 # t = 1+2
total=total+3 # t = 1+2+3
total=total+4 # t = 1+2+3+4
total=total+5 # t = 1+2+3+4+5
print(total)
t = 0
for i in range(1,6,1): # i = 1,2,3,4,5
    t=t+i
print(t)
for i in range(1,6,1): # i = 1,2,3,4,5
    t+=i

print(t)

# 1에서 부터 10까지의 합을 구해보세요
t = 0
for i in range(1,11,1) :
    t= t+i # i = 1,2,3,4,5,6,7,8,9
print(t)
# 1에서 부터 100까지의 합을 구해보세요
t = 0
for i in range(1,101,1) :
    t=t+i
    print(t)
print('1부터 100까지의 합은 : {}입니다'.format(t))

# 입력한 수부터 입력한 수 까지의 합을 구해보세요

n1 = int(input('첫번째 숫자>>>'))
n2 = int(input('두번째 숫자>>>'))
total = 0
# n1부터 n2까지의 합을 구해보세요
for i in range(n1,n2+1) :
    total= total+i
    print(total)
print('{}부터 {}까지의 합은 : {}입니다'.format(n1,n2,total))