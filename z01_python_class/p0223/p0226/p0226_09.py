numL=[]

# 0에서 부터 5까지 넣어보세요
for i in range(6) :
    numL.append(i)
    print('numL[]=',numL)

aa = [1,2,3,4]
#index를 사용해서 값 읽기
for i in aa :
    print(i)
for i in range(0,4) :
    print(aa[i])

f=['사과','복숭아','딸기','포도','자몽']

for i in f :
    print(i)
for i in range(len(f)): # 리스트의 길이 len 함수는  반복문에서 많이 사용, len : 전체길이
    print(f[i])

c=['미국','영국','호주','캐나다','일본','중국']
# for문을 사용해서 출력해보기
for i in range(0,5,1) :
    print(c[i])
for i in range(len(c)) :
    print(c[i])
# 1에서 100까지 들어가는 numL=[]만들고 출력해보기
numl=[]

for i in range(100) :
    numl.append(i+1)
    #print(i+1,end='')
    print(numl)
for i in range(100):
    print(numl[i])
    
# 반복문 안에 if 문 사용
for i in range(10) :
    #print(1) #0~9 까지 출력이 됨
    if i == 9 :
        print('9입니다')

lan = ['영어', '스페인어', '일본어', '중국어']
for i in lan:
    if i == '영어' :
        print('영어입니다')
    else:
        print('다른언어입니다')

# 2의 배수만 출력 (1-100사이)
num=[]
for i in range(1,101,1) :
    if i%2 == 0 : 
        print(i, end=',')
print()
# 7의 배수만 출력 (1-100사이)
for i in range(1,101,1) :
    if i%7 == 0:
        print(i, end=',')
print()
aa = [100,90,86,79,72,52,98,94]
# 80점 이상만 합격 출력 > 합격이 5개 출력
for i in aa :
    print(i)
    if i >= 80 :
        print('합격')

# 딸기가 있으면 딸기, 다른 과일은 다른과일 이라고 출력

f=['사과','복숭아','딸기','포도','자몽']
for i in f :
    print(i)
    if i == '딸기' :
        print('딸기입니다')
    else :
        print('다른 과일입니다')

num=[1,2,5,7,9,10,23,43]
# 짝수면 짝수 홀수면 홀수를 출력

for i in num :
    print(i)
    if i%2 == 0 :
        print('짝수')
    else :
        print('홀수')

for i in range(len(num)) :
    if num[i]%2 == 0 :
        print(num[i], '짝수')
    else :
        print(num[i],'홀수')

    


