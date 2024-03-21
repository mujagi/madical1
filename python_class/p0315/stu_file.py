def stu_open() :
    f= open("stu.txt","r",encoding="utf8")
    students = []
    while True :
        txt = f.readline() # 1줄씩 읽기
        if txt == "" : break
        stu_list = txt.split(",") # csv 파일을 분리
        
        s_dic={
            "stuNo":int(stu_list[0]), "name": stu_list[1], "kor" : int(stu_list[2]), "eng" : int(stu_list[3]), 
            "math" : int(stu_list[4]), "total" : int(stu_list[5]), "avg" : float(stu_list[6])
        }
        students.append(s_dic)
    return students

# 학생성적파일저장함수
def stu_save(students) :
    f = open("stu.txt","w",encoding="utf8")
    for s in students :
        stuNo=s["stuNo"]
        name=s["name"]
        kor=s["kor"]
        eng=s["eng"]
        math=s["math"]
        total=s["total"]
        avg=s["avg"]
        f.write(f"{stuNo},{name},{kor},{eng},{math},{total},{avg}")
    print("모든 내용이 파일에 저장되었습니다.")
    print()
    
def stu_update() :
    pass
    
    

