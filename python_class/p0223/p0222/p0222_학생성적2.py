# 학생 이름, 국어,영어, 수학 점수를 입력받아서
#아래와 같이 출력을 하고
#만약에 평균 80점 이상이면 합격입니다를 출력하세요
num=1
name=input('이름을 입력해주세요')
kor=int(input('국어 점수를 입력해주세요'))
eng=int(input('영어 점수를 입력해주세요'))
math=int(input('수학 점수를 입력해주세요'))
total=kor+eng+math
avg=total/3


print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(num,name,kor,eng,math,total,avg,1))
if total>=80 :
    print('합격입니다')
else :
    print('불합격입니다')    