import oracledb

# DB connect 연결
conn = oracledb.connect(user="ora_user", password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

# sql 실행
# 퀴즈 employees 테이블에서 사번, 이름, 월급 , 실제월급 (월급 + (월급*커미션)), 월급*1410 원하로 환산해서
# 천단위 표시해서 출력하시오
'''
sql = "select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)),to_char((salary+(salary*nvl(commission_pct,0)))*1410,'999,999,999l') from employees "
cursor.execute(sql)
data = cursor.fetchall()

print ("[ 데이터 출력 ]")
for d in data :
    print(d)
'''

# sql = "select employee_id,emp_name,salary,salary+(salary*nvl(commission_pct,0)),to_char((salary+(salary*nvl(commission_pct,0)))*1410,'999,999,999l') from employees "
# cursor.execute(sql)
# data = cursor.fetchall()
# print("[ 데이터 출력 ]")
# print("-"*40)
# print("사원번호\t사원명\t월급\t실제월급\t원화환산")
# print("-"*40)
# for d in data :
#     print(d[0],end="\t")
#     print(d[1],end="\t")
#     print(d[2],end="\t")
#     print(d[3],end="\t")
#     print("￦"+d[4].strip())
    
# 부서별 평균월급, 최대월급, 최소월급을 출력하시오
sql = "select department_id,avg(salary),max(salary),min(salary) from employees\
    where department_id is not null\
    group by department_id\
    order by department_id\
    "
cursor.execute(sql)
data = cursor.fetchall()
print("[ 데이터 출력 ]")
print("-"*40)
#print("사원번호\t사원명\t월급\t실제월급\t원화환산")
print("-"*40)
for d in data :
    print(d[0],end="\t")
    print(d[1],end="\t")
    print(d[2],end="\t")
    print(d[3])
    