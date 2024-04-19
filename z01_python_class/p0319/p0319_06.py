student = [["홍길동",100],["유관순",98]
        ,["이순신",95],["김구",50],["강감찬",99],["김유신",90],["홍길순",80],["홍길자",70],]
while True :
    print("[학생성적 검색]")
    print("[1. 이름으로 검색]")
    print("[2. 점수로 검색]")
    choice = int(input("원하시는 번호를 입력하세요>>"))
    
    if choice == 1 :
        search = input("찾고자 하는 학생의 이름을 입력하시오 >>")
        search_list = []
        cnt = 0
        for i in student :
            # : # -1은 없냐라는 뜻 !=  : 같지 않다 즉 최종은 있냐라는 뜻
            if search in i[0] :#= 위와 같은 수식 
                search_list.append(cnt)
            cnt+=1
        
        if len(search_list) == 0 :
            print("찾고자 하는 학생이 없습니다")
        
        else :
            print(f"{search}(으)로 검색된 사람 :", end=" ")
            for i in search_list :
                print(student[i][0],end=" ")
            print()
            print()

    if choice == 2 :
        score = int(input("몇 점 이상을 검색하시겠습니까? >>"))
        # 80 -> 80점 이상인 사람의 이름이 출력되도록 해보세요.
        search_list = []
        cnt = 0
        for i in student :
            if score == i[1] :
                search_list.append(cnt)
            cnt+=1
        if len(student) == 0 :
            print("찾고자 하는 학생이 없습니다.")
        
        else :
            print(f"{score}(으)로 검색된 사람 :", end = " ")
            for i in search_list :
                print(student[i][0],end = " ")
            print()
            print()
        