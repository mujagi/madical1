import oracledb


conn = oracledb.connect(user="ora_user", password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()


while True :
    #검색어 입력부분
    search = input("찾고자 하는 이름을 입력하세요 . >> ,(-1. 종료)")
    if search == "-1":
        break
    
    #검색부분
    sql = f"select *from stu_score\
        where name like '%{search}%'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for d in data :
            print(d)
    
        
    