
score = [[80,90,85],[70,80,90],[84,92,80],[72,81,76]]
name = ['홍길동','유관순','이순신','김구']
total = []
# 2. 코딩
# 2-1) 요소 하나하나 출력해보세요 80,90,85,70,80,90,84,92,80,72,81,76
for i in range(len(score)) :
    for j in range(len(score[i])) :
        print(score[i][j], end = ' ')
print()
# 2-2) 작은 요소의 합을 구해서 total에 넣어주세요

for n in range(len(score)) :
    s=0    
    for k in range(len(score[n])) :
        s+=score[n][k]
    total.append(s)
print(total)
for u in range(4) :
    for i in range(len(total)):
        if total[i] >= 250 :
            print('{}님 합격입니다'.format(name[u]))
        else :
            print('{}님 불합격입니다'.format(name[u]))
        
# 3. 출력
# 3-1)total = [255,240,256,229]
# 3-2) 250 미만 불합격 250이상 합격 