import oracledb

conn = oracledb.connect(user = "ora_user", password="1111", dsn="localhost:1521/xe")
cursor = conn.cursor()

# 평균점수를 입력받아 입력한 평균점수 이상의 학생을 출력하시오.
# 반복해서 진행하고 -1을 입력받으면 프로그램을 종료하시오.

while True :
    search = int(input("점수를 입력하세요 >> (-1.종료)"))
    if search == -1 :
        break
    else :
        search2 = int(input("이상, 이하 중 어떤것을 출력하시겠습니까?>> (1.이상 2.이하)"))
        if search2 == 1 :
            sql = f"select *from stu_score\
            where avg>={search}\
                
            order by no"
            cursor.execute(sql)
            data = cursor.fetchall()
            for d in data :
                print(d)
        elif search2 == 2 :
            sql = f"select *from stu_score\
            where avg<={search}\
            order by no"
            cursor.execute(sql)
            data = cursor.fetchall()
            for d in data :
                print(d)