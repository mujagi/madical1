# 학생성적 입력

#변수를 사용합니다
stu_name = input('이름을 입력해주세요>>')
kor=int(input('국어성적을 입력해주세요>>'))
eng=int(input('영어성적을 입력해주세요>>'))
math=int(input('수학성적을 입력해주세요>>'))
total = kor+eng+math
avg = float(total)/3

#입력을 받아서 총점과 평균을 계산하고,
#출력해보세요
print(''.format())


#홍길동 100 10 100 300 100.0

print('{}\t{}\t{}\t{}\t{}\t{}'.format(stu_name,kor,eng,math,total,avg))

stu =[1,'홍길동',100,100,100,300,100.0,1]
stu1 = [1,stu_name,kor,eng,math,total,avg,1]

