# 해보세요
# 1. 숫자 두개를 입력받아서 나누니값 몫값 나머지값을 출력
n1=int(input('첫번째 숫자를 입력해주세요>>'))
n2=int(input('두번째 숫자를 입력해주세요>>'))
print('{}/{}={}'.format(n1,n2,n1/n2))
print('{}//{}={}'.format(n1,n2,n1//n2))
print('{}%{}={}'.format(n1,n2,n1%n2))
# 2. 3개의 수의 합을구하세요
s1,s2,s3='100','100.123','99.9'
print('{}+{}+{}={}'.format(int(s1),float(s2),float(s3),float(s1)+float(s2)+float(s3)))

result= int(s1)+float(s2)+float(s3)
print('합은{}입니다.'.format(result))