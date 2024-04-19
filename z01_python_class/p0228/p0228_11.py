# n1 단부터 n2단까지 출력하세요
n1 = int(input('숫자입력 >>'))
n2 = int(input('숫자입력 >>'))

# 크기 비교해서 n1이 더 크면 n2,n1 값 바꾸기
if n1>n2 :
    n1,n2 = n2,n1

for i in range(n1,n2+1) :
    for j in range(1,10) :
        print('{}*{}={}'.format(i,j,i*j), end = '\t')
    print()
    
# 출력 2,4 2단부터 4단까지 출력