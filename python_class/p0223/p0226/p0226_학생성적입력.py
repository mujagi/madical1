student=[]
for i in range(5) :
    print('-'*35)
    print('\t[학생성적 프로그램]')
    print('1.학생성적입력')
    print('4.학생성적 전체출력')
    print('0.프로그램 종료')
    print('-'*35)
    ch=input('원하는 번호를입력하세요 >>')
# if 문을 사용해서 1누르면 [학생성적입력]
# 4 누르면 [학생성적 전체출력]
# 0 누르면 [프로그램 종료]
    if ch == '1' :
        print('학생성적입력')
        name=input('이름을 입력해주세요>>')
        kor=int(input('국어 점수를 입력해주세요>>'))
        eng=int(input('영어 점수를 입력해주세요>>'))
        math=int(input('수학 점수를 입력해주세요>>'))
        total = kor+eng+math
        avg = total/3
        print(name)
        print(kor)
        print(eng)
        print(math)
        stu = [1, name,kor,eng,math,total,avg,0]
        student.append(stu)
        print(student)
        # 이름,국, 영, 수 점수를 입력받아
    elif ch == '4' :
        print('학생성적 전체출력')   
        for s in range(len(student)):
            print(student[s])
    elif ch == '0' :
        print('프로그램 종료')
    else :
        print('잘 못 입력하였습니다')
    