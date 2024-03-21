member = []
cnt = 0
# 이름을 입력받아서 [1,홍길동],[2,유관순],[3,이순신]
while True :
    print('-'*25)
    print('1. 입력')
    print('2. 전체출력')
    print('3. 검색출력')
    print('4. 학생 삭제')
    print('5. 수정')
    print('0. 종료')
    ch = input('원하는 번호를 선택하세요 >>>')
    print('-'*25)
    ch = int(ch)
    if ch == 1 :
        print('입력')
        name = input('이름을 입력해주세요 >>>')
        cnt = cnt+1
        m = [cnt,name]
        member.append(m)
    elif ch == 2 :
        print('출력')
        print('번호\t이름')
        for i in range(len(member)) :
            print('{}\t{}'.format(member[i][0],member[i][1]))
    elif ch == 3 :
        print('검색출력')
        serch = input('이름을 입력해주세요 >>>')
        chk = 0
        for stu in member :
            if serch in stu :
                for i in range(len(member)) :
                    print('번호\t이름')
                    print('{}\t{}'.format(member[i][0],member[i][1]))
            if serch not in stu :
                print('검색하신 학생이 존재하지 않습니다')
    elif ch == 4 :
            chk = 0
            delname = input('삭제하실 이름을 입력해주세요>>>')                 
            for i, stu in enumerate(member):
                if delname in stu :
                    del(member[i])
                    chk = 1
            if chk == 0 :
                print('검색하신 학생이 존재하지 않습니다')   
    elif ch == 5 :
            chk = 0
            re = input('수정하실 학생의 이름을 검색해주세요 >>>')
            for i, stu in enumerate(member):
                if re in stu :
                    move = input('1. 번호수정, 2. 이름수정')
                    if move == '1' :
                        print('번호수정')
                        print(re,'님의 번호 수정을 선택하셨습니다')
                        print(re,'님의 번호는',member[i][0],'입니다')
                        stu_num = input('새로운 번호를 입력해주세요 >>')
                        stu_num = int(stu_num)
                        member[i][0] = stu_num
                    elif move == '2' :
                        print('이름수정')
                        print(re,'님의 이름 수정을 선택하셨습니다')
                        print(re,'님의 이름은',member[i][1],'입니다')
                        stu_name = input('새로운 이름을 입력해주세요 >>')
                        member[i][1] = stu_name
                
                        
                   
    elif ch == 0 :
        print('종료')
        break
    else :
        print('다시 입력해 주세요')