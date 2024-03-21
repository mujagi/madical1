# continue 예제
# 1~100 합계를 구하는데 3의 배수는 제외하고 더하기
# while or for
t = 0
for i in range(1,101) :
    if i%3 == 0 :
        continue
    t+=i
print(t)
print('-'*35)
sum =0
n = 1
while n<101 :
    if n%3 == 0 :
        n = n+1
        continue
    sum += n
    n = n+1
print(sum, end = ' ')