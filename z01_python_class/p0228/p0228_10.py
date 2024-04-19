# for 문을 사용해서 2단을 출력
# 입력받은 숫자의 단을 출력하세요

for i in range(10) :
    print('[{} 단]'.format(i))
    for j in range(1,10) :
        if i%2 == 0 :
            print('{}*{}={}'.format(i,j,i*j), end = ' ')
    print()
for i in range(10) :
    print('[{} 단]'.format(i))
    for j in range(1,10) :
        if j%2 != 0 :
            print('{}*{}={}'.format(i,j,i*j), end = ' ')
    

        

#for i in range(1,10) :
    #print('{}*{}={}'.format(2,i,2*i))

#for j in range(5) : # j = 0 1 2 3 4
    #print(j+1, '번째 출력')
    #for i in range(1,6) : # i = 1 2 3 4 5
        #print(i,end=' ') # 1 2 3 4 5 를 한줄로 출력
    #print() #줄바꿈
    
# 짝수단만 출력해주세요

#(*1,3,5,7,9)

