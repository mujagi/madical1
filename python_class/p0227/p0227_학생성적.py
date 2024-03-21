stu = []
for i in range(5) :
    print('-'*35)
    print('\t[학생성적프로그램]')
    print('1. 학생성적 입력')
    print('4. 학생성적 전체출력')
    print('-'*35)
    ch = int(input('원하는 번호를 입력하세요>>'))

    if ch == 1 :
        print('학생성적 입력을 선택하셨습니다')
        name = input('이름을 입력하세요>>')
        kor = int(input('국어 점수를 입력해주세요 >>>'))
        eng = int(input('영어 점수를 입력해주세요 >>>'))
        math = int(input('수학 점수를 입력해주세요 >>>'))
        total = kor+eng+math
        avg = total/3
        stu1 = [1,name,kor,eng,math,total,avg,1]
        stu.append(stu1)
        
       
    elif ch == 4 :
        print('학생성적 전체출력을 입력하셨습니다')
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        for i in range(len(stu)) :
            print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(stu[i][0],stu[i][1],stu[i][2]
                                                  ,stu[i][3],stu[i][4],stu[i][5]
                                                  ,stu[i][6],stu[i][7]))
        

