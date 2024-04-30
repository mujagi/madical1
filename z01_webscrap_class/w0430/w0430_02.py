import oracledb

#sql
conn = oracledb.connect(user = "ora_user", password = "1111", dsn = "localhost:1521/xe")
cursor = conn.cursor() # db와 연결되어 지시자 생성


#stu_score avg 90점 이상 a,80점 이상 b, 70점 이상 c, 60점 이상 d, 미만 d
# 학번 이름  합계 평균 학점 
# sql = "select no,name,total,avg,\
#     case\
#     when avg >= 90 then 'A'\
#     when avg >= 80 then 'B'\
#     when avg >= 70 then 'c'\
#     when avg >= 60 then 'd'\
#     else 'f'\
#     end as grade\
#     from stu_score "

#평균을 가지고 파이썬에서 프로그램 하여 학점을 출력하시오.
# 학번,이름, 합계,평균,학점
sql = "select *from stu_score"
# board 테이블 모든 컬럼, member 테이블의 name 컬럼을 가져와 출력하시오
# board 테이블 id, member 테이블 name
#sql = "select bno, a.id, name, btitle, bcontent,bdate,bgroup,bstep,bindent,bhit,bfile\
#    from board a,member b "
cursor.execute(sql) # cursor 에 select 한 결과값을 저장 (결과값 : list)
data= cursor.fetchall() # fetchall() : 모든 데이터를 가져옴 . fetchone() : 1개의 데이터를 가져옴

print("[ 모든 데이터출력 ]")
#print(data)
# grade = ""
# for d in data :
#     if d[6] >= 90 :
#         grade = "A"    
#     elif d[6]>=80 :
#         grade = "B" 
#     elif d[6]>=70 :
#         grade = "C"   
#     elif d[6]>=60 :
#         grade = "D" 
#     else :
#         grade = "F" 
#     print("학번 : ",d[0])
#     print("이름 : ",d[1])
#     print("합계 : ",d[5])
#     print("평균 : ",d[6])
#     print("학점 : ",grade)
#     print("-"*20)
# print("-")
# print("타입 : ",type(data))

sql = "select round(avg(salary),2) from employees"
cursor.execute(sql)
data = cursor.fetchone()
print(data[0])
conn.close() #데이터베이스연결해제