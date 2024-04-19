students = [
    {'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 87, 'total': 286, 'avg': 95.33},
    {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 93, 'math': 87, 'total': 278, 'avg': 92.67},
    {'stuNo': 'S003', 'name': '이순신', 'kor': 88, 'eng': 76, 'math': 30, 'total': 194, 'avg': 64.67},
    {'stuNo': 'S004', 'name': '김구', 'kor': 100, 'eng': 100, 'math': 100, 'total': 300, 'avg': 100.0},
    {'stuNo': 'S005', 'name': '강감찬', 'kor': 98, 'eng': 85, 'math': 44, 'total': 227, 'avg': 75.67}
]
cnt = len(students)+1
while True :
    print('-'*40)
    print('[학생성적프로그램]')
    print('-'*40)
    print('1. 학생성적입력')
    print('2. 학생성적전체출력')
    print('3. 학생검색')
    print('4. 학생수정')
    print('5. 등수처리')
    print('6. 학생삭제')
    print('0. 프로그램 종료')
    print('-'*40)
    choice = int(input('원하는 번호를 입력하세요:  '))
    print('-'*40)
    if choice == 1 :
        print("학생성적입력을 선택하셨습니다.")
        stu = int(input("학생 성적을 입력하시겠습니까? (1.입력 2.취소)"))
        if stu == 1 :
            student = {}
            student["stuNo"] = "S"+"{:03d}".format(cnt)
            name = input("학생이름을 입력해주세요>>")
            kor = int(input("국어 점수를 입력해주세요>>"))
            eng = int(input("영어 점수를 입력해주세요>>"))
            math = int(input("수학 점수를 입력해주세요>>"))
            total = kor+eng+math
            avg = total/3
            student["name"] = name
            student["kor"] = kor
            student["eng"] = eng
            student["math"] = math
            student["total"] = total
            student["avg"] = float("{:.2f}".format(avg))
            students.append(student)
            cnt+=1
            print(students)
            
        elif stu == 0 :
            break
    if choice == 2 :
            print("학생성적 전체출력을 입력하셨습니다.")
            stu=int(input("학생성적을 출력하시겠습니까? (1.출력 0.취소)"))
            if stu == 0 :
                break
            elif stu == 1 :
                print("번호\t이름\t국어\t영어\t수학\t총합\t평균")
                for i in students :
                    for j in i :
                        print(i[j],end='\t')
                    print()
            else :
                print("번호를 잘 못 입력하셨습니다 다시 입력해주세요.")
                continue
    if choice == 3 :
        print("학생검색을 입력하셨습니다.")
        search = input("검색하실 학생의 이름을 입력해주세요 >>")
        for stu in students :
            if stu["name"] == search :
                print(stu)
    if choice == 4 :
        s_title = ['','국어','영어','수학']
        while True :
            search = input("수정하실 학생의 이름을 입력하세요 (0.취소)")
            chk = 0
            if search == "0" :
                break
            for s_dic in students :
                if s_dic["name"] == search :
                    break
                chk += 1
            print("찾고자 하는 학생의 위치",chk)
            if chk == len(students) :
                print(f"{search} 학생은 없습니다. 다시 입력하세요.")
            else :
                print(f"{search} 학생을 찾았습니다.")
                while True :
                    resault = int(input('수정할 과목 선택 1.국어 2.영어 3.수학'))
                    if resault == 1 :
                        s_1 = "kor"
                        resault2 = int(input("수정하실 점수를 입력해주세요 >>"))
                        students[chk][s_1] = resault2
                    print(students[chk])
                    if resault == 2 :
                        s_1 = "eng"
                        resault2 = int(input("수정하실 점수를 입력해주세요 >>"))
                        students[chk][s_1] = resault2
                    print(students[chk])
                    if resault == 3 :
                        s_1 = "math"
                        resault2 = int(input("수정하실 점수를 입력해주세요 >>"))
                        students[chk][s_1] = resault2
                    print(students[chk])
    
                    

                
                
                
                     
            

    
                    

        
                        

                
                
                
            
    
                    
                
                
            
        