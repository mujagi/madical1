#student = ['K001','K002','K003']
students = []
count = 1
# 학번, 이름, 국어, 영어, 수학, 합계, 평균 입력하는 프로그램
while True :
    chk = int(input("학생성적을 추가하시겠습니까?(1.추가, 0.취소)"))
    if chk == 1 :
        student = {}
        stuNo = "K"+"{:03d}".format(count)
        name = input("이름을 입력해주세요 >>")
        kor = int(input("국어점수를 입력해주세요 >>"))
        eng = int(input("영어점수를 입력해주세요 >>"))
        math = int(input("수학점수를 입력해주세요 >>"))
        total = kor + eng + math
        avg = '{:.2f}'.format(total/3)
        student["stuNo"] = stuNo
        student["name"] = name
        student["kor"] = kor
        student["eng"] = eng
        student["math"] = math
        student["total"] = total
        student["avg"] = avg
        students.append(student)
        print("[학생정보내역]")
        for k in student.keys():
            print("{}:{}".format(k,student[k]))
        print("-"*50)
        print("학생 1명 추가 되었습니다.")
        count+=1
        
        
    else :
        print("학번 추가를 종료합니다.")
        pass

