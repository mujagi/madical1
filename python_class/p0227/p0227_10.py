num = []
# for 문을 사용해서 1-10 까지 숫자를 채우세요
for i in range(1,11) :
    num.append(i)
print(num)

# 1-10 까지 짝수를 num2 리스트에 넣으세요
num2 = []
for i in range(1,11) :
    if i%2 ==0:
        num2.append(i)
        
print(num2)

# 1 ~ 10 까지의 합 for문을 사용해서 구할 수 있음        
num = [1,2,3,4,5,6,7,8,9,10]
# num 리스트를 사용해서 1~10까지의 합을 구해보세요
s1 = 0
for n in num :
    s1 += n
print(s1)
s2 = 0
for n in range(len(num)) :
    s2 = s2 + num[n]
print(s2)
    #print(num[n], end = ' ')
# num2 리스트 내 숫자들의 합을 구하세요
s3 = 0
for n in num2 :
    s3+=n
s4 = 0
for i in range(len(num2)) :
    s4 = s4 + num2[i]
print(s3,s4)


    