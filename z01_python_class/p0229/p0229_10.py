''' 
str1 = '10'
print(str1.isdigit()) #False
while True :
    n = input("원하는 번호를 입력해주세요 >>>")
# n 은 문자열

    if n.isdigit() : # 숫자지만 문자열 ex) "0" "1"
        n = int(n)
        # n 은 문자열
    else :
        print('문자가 입력되었습니다. 다시 입력해주세요')
    
    if n == 0:
        print('숫자 0이 입력되었습니다')
'''
# 이름을 검색해보고, 이름을 검색해서 삭제
students = [[1,'홍길동',100],[2,'이순신',90],[3,'유관순',85],[4,'김유신',70],[5,'김구',95]]

while True :
    print('1. 학생 검색')
    print('2. 학생 삭제')
    print('3. 프로그램 종료')
    ch = input('원하는 번호를 입력해주세요 >>>')
    if ch.isdigit() :
        ch = int(ch)
    if ch == 1 :
        searchname = input('검색할 학생의 이름을 입력해주세요 >>')
        chk = 0
        for stu in students :
            #print(stu)
            if searchname in stu :
                print('{} 학생이 존재합니다.'.format(searchname))
                print(stu)
                chk = 1
        if chk == 0 :
            print('검색하신 학생이 존재하지 않습니다')
    
    elif ch == 2 :
        delname = input('삭제하고싶은 학생의 이름을 입력하세요>>')

        for i , stu in enumerate(students):
            if delname in stu :
                del(students[i]) 
            if delname not in stu :
                print('검색하신 학생이 존재하지 않습니다')
    elif ch == 3 :
            print('프로그램이 종료되었습니다.')
            break
    else :
        print('잘못입력하셨습니다. 다시 입력해주세요')