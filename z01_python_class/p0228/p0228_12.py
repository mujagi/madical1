''' 
주석 여러줄 쓸 때 
한줄 주석 # 주석 쓰셔도되고
control+/ 커서 있는 문장 주석
tab : 들여쓰기
shift +tab (들여쓰기 삭제) 
alt + shift + 위아래 방향키 (커서있는 문장 복사)
'''
num = [100,200,300,400]
# for 문을 사용해서 하나씩 출력해보세요
for i in num:
    print(i,end = ' ')
print()
for i in range(len(num)) :
    print(num[i], end = ' ')
print()
numlist = [[1,2],[3,4],[5,6]]
for n in numlist :
    for a in n :
        print(a,end = ' ')
    print ()
for k in range(len(numlist)) :
    for s in range(len(numlist[k])) :
        print(numlist[k][s], end = ' ')
print()
f = [['딸기',100,1000],['수박',100,500],['사과',100,1200],['귤',100,300]]
# 요소 한개한개를 출력해보세요
for i in range(len(f)) :
    for j in range(len(f[i])) :
        print(f[i][j], end = ' ')
print()
for n in f :
    for a in  n :
        print(a, end = ' ')     
print()
score = [90,80,70,100,95,85,100]
# 점수의 총합을 구하세요
t = 0 
for i in score :
    t=t+i
print(t)