students = []
cnt = 0
while True :
    print('-'*35)
    print('\t'+'[학생성적프로그램]')
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('4. 학생성적전체출력')
    print('5. 학생검색출력')
    print('6. 등수처리')
    print('0. 프로그램 종료')
    print('-'*35)
    choice = input('원하는 번호를 입력하세요. >>>')
    choice = int(choice)
    if choice == 1 :
        print('학생성적입력을 선택하셨습니다.')
        name = input('이름을 입력해주세요 >>')
        kor = int(input('국어 점수를 입력해주세요>>>'))
        eng = int(input('영어 점수를 입력해주세요>>>'))
        math = int(input('수학 점수를 입력해주세요>>>'))
        total = kor+eng+math
        avg = total/3
        student = [name,kor,eng,math,total,avg]
        students.append(student)
    elif choice == 2 :
        chk = 0
        print('학생성적수정을 입력하셨습니다')
        rename = input('수정을 원하시는 학생이름을 입력해주세요 >>>')
        for i, stu in enumerate(students) :
            if rename in stu :
                result = input('변경을 원하는 과목을 선택해주세요 >>>')
                if result == '국어' :
                    print('국어점수를 선택하셨습니다')
                    print(rename,'님의 국어 점수는',students[i][1],'입니다')
                    stu_num = int(input('새로운 점수를 입력해주세요 >>>'))
                    students[i][1] = stu_num
                elif result == '수학' :
                    print('수학점수를 선택하셨습니다')
                    print(rename,'님의 수학 점수는',students[i][2],'입니다')
                    stu_num = int(input('새로운 점수를 입력해주세요 >>>'))
                    students[i][2] = stu_num
                elif result == '영어' :
                    print('영어점수를 선택하셨습니다')
                    print(rename,'님의 영어 점수는',students[i][3],'입니다')
                    stu_num = int(input('새로운 점수를 입력해주세요 >>>'))
                    students[i][3] = stu_num
            if rename not in stu :
                print('이름을 잘 못 입력하셨습니다.')
                break
    elif choice == 3 :
        print('학생성적 삭제를 입력하셨습니다.')
        chk = 0
        delname = input('삭제하실 학생의 이름을 입력해주세요 >>>')
        for i, stu in enumerate(students) :
            if delname in stu :
                del(students[i])
                chk = 1
            if chk == 0 :
                  print('검색하신 학생이 존재하지 않습니다')
    elif choice == 4 :
        print('학생성적 전체출력을 입력하셨습니다.')
        print('번호\t이름\t국어\t수학\t총점\t평균')
        for i in range(len(students)) :
            print('{}\t{}\t{}\t{}\t{}\t{}'.format(students[i][0],students[i][1],students[i][2],
                                                  students[i][3],students[i][4],students[i][5]))
    elif choice == 5 :
                print('학생검색출력을 입력하셨습니다 ')
                serch = input('이름을 입력해주세요 >>>')
                for stu in students :
                    for i, serch in enumerate(stu) :
                           print('번호\t이름\t국어\t수학\t총점\t평균')
                           print('{}\t{}\t{}\t{}\t{}\t{}'.format(students[i][0],students[i][1],students[i][2],
                                                  students[i][3],students[i][4],students[i][5]))
                    if serch not in stu :
                        print('이름을 잘 못 입력하셨습니다.')
    elif choice == 0 :
        print('프로그램을 종료합니다.')
        break
                       

                
            


    
                    
                    
                    
                
        
        