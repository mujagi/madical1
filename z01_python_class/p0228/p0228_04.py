# 1~100까지의 합 구해보기
s1,s2,s3 = 0,0,0
for i in range(1,101) :
    s1 = s1+i
    if i%2 ==  0:
        s2 = s2+i
    else : 
        s3 = s3+i
# 1~100까지 짝수의 합 , 홀수의 합
print ('1~100까지의 합은 {}입니다'.format(s1))
print ('1~100까지의 짝수의 합은 {}입니다'.format(s2))  
print ('1~100까지의 홀수의 합은 {}입니다'.format(s3))

# 1 . 1~10 합

# num 리스트 안에 있는 값들의 합
t = 0
num = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(num)) :
    t=t+num[i]
print(t)
