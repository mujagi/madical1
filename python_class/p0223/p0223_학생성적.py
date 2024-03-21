#stu1=[1,'홍길동',100,100,100,300,100.0,1]
#stu2=[2,'유관순',90,90,90,270,90.0,2]
print('-'*35)
print('[학생성적프로그램]')
print('-'*35)
print('1. 학생성적 입력')
print('2. 학생성적 전체출력')
print('3. 프로그램 종료')
print('-'*35)
choice=int(input('원하는 번호를 입력해주세요>>'))
print(choice)
if choice==1 :
    print('학생성적 입력')
    name=(input('이름'))
    kor=int(input('국어'))
    eng=int(input('영어'))
    math=int(input('수학'))
    all=[1,name,kor,eng,math,kor+eng+math,(kor+eng+math)/3,1]
elif choice==2:
    print('학생성적 전체출력')
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(
        all[0],all[1],all[2],all[3],all[4],all[5],all[6],all[7]))
    
    
    
    


    
