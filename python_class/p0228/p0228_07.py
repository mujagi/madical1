
a,b = 10,8
a,b = b,a

n1 = [0,1,2,3,4,5]
#     0의 위치와
#           3의 위치를 바꾸고 싶다
n1[0],n1[3] = n1[3],n1[0]

con = ['미국', '영국', '일본', '중국', '스페인']
# 영국,중국 위치를 바꿔보세요
con[1],con[-2] = con[-2],con[1]
print(con)

from random import*
n1 = [1,2,3,4,5,6,7,8,9,10]
#     0                 9
for i in range(10) :
        tmp = randint(0,9) # 랜덤한인덱스 만들기
        n1[0],n1[tmp] = n1[tmp],n1[0] # 숫자를 서로 섞어주기
        print(tmp)
        print(n1)
        

