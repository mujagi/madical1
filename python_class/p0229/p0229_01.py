for i in range(5) : # 5번 반복 i = 0,1,2,3,4
    print('i=' , i)
    print('-'*25)
    for j in range(3): # 3번 반복 j = 0,1,2
        print('j =', j)
    print('하단부', '-'*25)

# 구구단

# 2단 출력
for i in range(1,10) :
    print('{}*{}={}'.format(2,i,2*i))

# 구구단 전체 출력
for i in range(2,10) : # i = 2~9 단
    print('{}단'.format(i))
    for j in range(1,10) : # *1~*9
        print('{}*{}={}'.format(i,j,i*j))
    print() # 줄바꿈

for i in range(2,10) :
    print('{}단'.format(i), end ='\t')
for i in range(1,10) : # *1~9
    # 줄이 바뀔때마다
    for j in range(2,10) : # 단
        # 요소가 출력될때마다
        print('{}*{}={}'.format(j,i,i*j),end = '\t')
        print()
