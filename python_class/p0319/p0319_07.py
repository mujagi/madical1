class Student :
    count = 1
    
    def __init__(self,name,kor,eng,math,stuNo=0,rank=0) :
        self.stuNo = stuNo
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = kor+eng+math
        self.avg = float("{:.2f}".format(self.total/3))
        self.rank = rank
    def __str__(self) :
        return f"{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}"

students=[]
f=open("stu.txt","r",encoding="utf8")
while True :
    txt = f.readline()
    if txt == "" :
        break
    txt_list = txt.split(",")
    s = txt_list[1],int(txt_list[2]),int(txt_list[3]),int(txt_list[4]),int(txt_list[0]),int(txt_list[7])
    students.append(s)
f.close
Student.count = len(students)+1
search_txt = ["","찾고자하는이름을 입력하시오>>","몇점이상 찾겠습니까?>>","몇점이하 찾겠습니까?>>"]

#------------------------------------------------------- 함수빼기
def main_title_print() :
    print("-"*40)
    print("[ 학생성적프로그램 ]")
    print("-"*40)
    print("1. 학생성적입력")
    print("2. 학생성적전체출력")
    print("3. 학생검색")
    print("4. 학생성적수정")
    print("5. 학생성적삭제")
    print("6. 등수처리")
    print("0. 종료")
    print("-"*40)
    choice = int(input("원하는 번호를 입력하세요 >>"))
    return choice

def main_print() :
    print('\t[ 학생성적출력 ]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t합계\t평균\t등수')
    print('-'*65)
    
def stu_insert() :
    while True :
        print("학생성적 입력을 선택하셨습니다.")
        name = input("이름을 입력해주세요>>(0. 취소)")
        if (name == 0) :
            break
        kor = int(input("국어점수를 입력해주세요>>"))
        eng = int(input("영어점수를 입력해주세요>>"))
        math = int(input("수학점수를 입력해주세요>>"))
        s = Student(name,kor,eng,math)
        students.append(s)
        print(s)

def stu_print() :
    main_print()
    for i in students :
        print(i)
    print()

def stu_search_title() :
    print("\t[ 학생성적 검색 ]")
    print("-"*40)
    print("1. 학생이름으로 검색")
    print("2. 총점이상 검색")
    print("3. 총점이하 검색")
    print("0. 이전화면 이동")
    choice = int(input("원하는 번호를 입력하세요.>> "))
    return choice
        
def stu_search(choice) :
    
    if choice == 1 :
        search = input(search_txt[choice])

    else  :
        search = int(input(search_txt[choice]))
    s_list = []
    for i in students :
        if choice == 1 :
            if i.name.find(search) != -1 :
                s_list.append(i)
        elif choice == 2 :
            if i.total >= search :
                s_list.append(i)
        elif choice == 3 :
            if i.total <= search :
                s_list.append(i)
    if len(s_list) != 0 :
        main_print()
        for i in s_list :
            print(i)
    else :
        print("찾고자 하는 학생이 없습니다. 다시 입력해주세요.")
        


#-------------------------------------------------------
while True :
    choice = main_title_print()
    if choice == 1 :
        stu_insert()
    elif choice == 2 :
        stu_print()
    elif choice == 3 :
        while True :
            choice =stu_search_title()
            if choice == 0 :
                print("이전 화면으로 돌아갑니다.")
                print()
                break
            stu_search(choice)
    elif choice == 4 :
        search = input("수정하실 학생의 이름을 입력해주세요>>")
        cnt = 0
        for s in students :
            if s.name == search :
                break
            cnt+=1
        if cnt >= len(students) :
            print("찾고자 하는 학생이 없습니다. 다시 입력해주세요.")
        else :
            print(f"{search}(으)로 검색한 학생을 찾았습니다")
            print()
            print("[수정할 과목 선텍]")
            print("-"*30)
            print()

    
        
        
        

        
