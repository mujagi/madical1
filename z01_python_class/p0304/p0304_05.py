students = [["홍길동",90,100,99,299,99.97],
            ["유관순",80,100,99,299,99.97],
            ["이순신",100,100,99,299,99.97]
]

# 찾는 학생의 이름


# 찾고자 하는 학생찾기
while True :
    # 멈춤
    search = input("검색하고 싶은 학생 이름을 입력하세요.(0.취소)")
    chk = 0 # 찾는 정보확인
    count = 0
    if search == "0" :
        break
    for stu in students : # 홍길동,유관순,이순신
        if search in stu :
            chk = 1 # 정보를 찾았을때 정보를 1로 변경
            break
        count +=1
    if (chk==1) :
            
    # 전체학생 정보출력
        print("{} 학생성적 출력".format(search)) 
        print("[학생성적 출력]")
        print("-"*50)
        print("이름\t국어\t영어\t수학\t합계\t평균") #\n = 엔터키
        print("-"*50)
        for i in students[count] :
            print(i,end= "\t")
        print()
    else :
        print("존재하지 않는 학생입니다")