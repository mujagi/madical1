# 리스트변수명 = [요소1,2,3,4,5....n]
# 요소가 될 수 있는 타입이 : bool, int, float, String, list

fruits = ['딸기','사과','배','수박','귤']
# 귤을 출력
print(fruits[4])
print(fruits[-1])
print(fruits[len(fruits)-1])
# 리스트에 요소를 추가
fruits.append('포도')
print(fruits)
fruits.remove('딸기') # 특정요소를 삭제
print(fruits)
# 리스트에서 3번째 삭제
del(fruits[3])
print(fruits)

if '한라봉' in fruits :
    print('있음')

for f in fruits : # in 리스트명
    print(f)

for i in range(len(fruits)) : # i = 0,1,2.....
    print(fruits[i])

num = [[10,20,30],[100,200,300],[1,2,3]]
for n in num :
    print(n)

for n in num :
    for a in n :
        print(a)

print('-'*25)
for i in range(len(num)) :
    print(i)
for i in range(len(num)) :
    for j in range(len(num[i])) :
        print(num[i][j])
        
# 리스트에 숫자 넣을 때 한줄로 표현하기 
aa = []

for i in range(1,11) :
    aa.append(i)


print(aa)

a=[i for i in range(1,11)]
a = [0 for _ in range(10)]
a = [[] for i in range(10)]

a = [ i*j for i in range(1,3) for  j in range(1,3)]
# [1,2,2,4]
a = [i for i in range(100) if i%2 == 0]
print(a)
b = [i for i in range(1,11)]
print(b) #[1,2,3,4,5,6,7,8,9,10]
c = [i+1 for i in b]
print(c)
# [표현식 for 항목 in 리스트 if 조건문]

names = ['홍길동', '유관순', '이순신', '강감찬', '김구']
# 출력
# 1.홍길동 2.유관순 3.이순신 4.강감찬 5.김구
for i in range(len(names)) : 
    print('{}.{}'.format(i+1,names[i]), end = ' ')

# 변수 1개 더 필요
i = 0
for name in names :
    i = i+1
    print('{}.{}'.format(i,name))
# 1.홍길동 2.유관순 3.이순신 4.강감찬 5.김구
for i, name in enumerate(names, start=1) : # index :0부터 시작
    print('{}.{}'.format(i,name))
    
    
    
     
    