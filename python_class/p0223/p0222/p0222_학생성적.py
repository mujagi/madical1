print('-'*35)
print('\t[학생성적프로그램]')
print('1.학생성적입력')
print('2.학생성적수정')
print('3.학생성적삭제')
print('4.학생검색출력')
print('6.등수처리')
print('0.프로그램종료')
print('-'*35)

print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
print('{} \t{} \t{} \t{} \t{} \t{} \t{} \t{}'.format(
   1,'홍길동' ,100,100,100,300,100.0,1 
))

# 홍길동 100 100 100
# 유관순 90 100 90
# 두 정보를 입력을 받아서출력해보세요
print('번호\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
num=1
num2=2
name1=input('이름을 입력해주세요>>')
kor1=int(input('국어 점수를 입력해주세요>>'))
eng1=int(input('영어 점수를 입력해주세요>>'))
math1=int(input('수학 점수를 입력해 주세요>>'))
total1=kor1+eng1+math1
avg1=total1/3
num2=2
name2=input('이름을 입력해주세요>>')
kor2=int(input('국어 점수를 입력해주세요>>'))
eng2=int(input('영어 점수를 입력해주세요>>'))
math2=int(input('수학 점수를 입력해 주세요>>'))
total2=kor2+eng2+math2
avg2=total2/3
print('{} \t{} \t{} \t{} \t{} \t{} \t{} \t{}'.format(
   num,name1,kor1,eng1,math1,total1,avg1,1 
))


print('{} \t{} \t{} \t{} \t{} \t{} \t{:.2f} \t{}'.format(
   num2,name2,kor2,eng2,math2,total2,avg2,1 
))