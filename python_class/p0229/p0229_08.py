# 1~100 까지 더하는데,
# 총 합이 100이 넘었을 때 수를 출력하세요
# 1+2+...
sum = 0
for i in range(1,11):
    sum += i
    if sum > 4 :
        break
print('수 : ', i)
print('총합 : ', sum)
sum =0
t= 1
while t<=100 :
    sum += t
    t += 1
    if sum > 100 :
        break
print(sum)
        
    
# 1~10 까지 더하는데 총합이 4가 넘는 순간의 수를 출력
