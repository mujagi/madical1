student=[[1,'홍길동',100,100,100,300,100.0,1],
         [2,'유관순',90,90,90,270,90.0,1]]

print('-'*35)
print('\t[학생성적프로그램]')
print('1. 학생성적 입력')
print('4. 학생성적 전체출력')
print('-'*35)
ch = int(input('원하는 번호를 입력하세요'))
#if ch == 1 :
    #print('학생성적 입력을 선택하셨습니다')
    #name = input('이름을 입력해주세요>>>')
    #kor = int(input('국어 점수를 입력해주세요>>>'))
    #eng = int(input('영어 점수를 입력해주세요>>>'))
    #math = int(input('수학 점수를 입력해주세요>>>'))
    #total = kor+eng+math
    #avg = total/3
    #print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        #1,name,kor,eng,math,total,avg,1))
#elif ch == 4 :
    #print(student)
stu = []
if ch == 1 :
    print('학생성적 입력을 선택하셨습니다')
    stu.append(input('학생 이름을 입력해주세요>>>'))
    stu.append(int(input('국어 점수를 입력해주세요>>>')))
    stu.append(int(input('영어 점수를 입력해주세요>>>')))
    stu.append(int(input('수학 점수를 입력해주세요>>>')))
    total=stu[1]+stu[2]+stu[3]
    avg = total/3
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}\t{}'.format(
        1,stu[0],stu[1],stu[2],stu[3],total,avg,1))
elif ch == 4 :
    print('학생성적 전체출력을 선택하셨습니다')
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        student[0][0],student[0][1],student[0][2],student[0][3],student[0][4],student[0][5]
        ,student[0][6],student[0][7]))
        
    