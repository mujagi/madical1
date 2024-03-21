# stu.txt 파일을 읽어 출력하시오
f= open("stu.txt","r",encoding="utf8")
students = []
while True :
    txt = f.readline() # 1줄씩 읽기
    if txt == "" : break
    stu_list = txt.split(",") # csv 파일을 분리
    #print("{},{},{},{},{},{},{}".format(*stu_list))
    s_dic={
        "stuNo":int(stu_list[0]), "name": stu_list[1], "kor" : int(stu_list[2]), "eng" : int(stu_list[3]), 
        "math" : int(stu_list[4]), "total" : int(stu_list[5]), "avg" : float(stu_list[6])
    }
    students.append(s_dic)
    #print("{},{},{},{},{},{},{}".format(*stu_list))

print(students[0]["name"])
