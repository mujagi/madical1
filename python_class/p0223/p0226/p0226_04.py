# 해보세요
stu = ['홍길동', '유관순', '이순신', '김구', '강감찬']

# 1. 이순신 학생출력
# 2. 김구 이름을 안창호로 변경
# 3. 유관순부터 강감찬 출력
# 4. 왕건을 추가
# 5. 홍길동 삭제

print(stu[2])
stu[3] = '안창호'
print(stu)
print(stu[1:5])
stu.append('왕건')
stu.remove('홍길동')
print(stu)

f= ['사과','복숭아', '딸기', '배', '포도', '수박']
# 딸기 출력
# 포도를 망고로 바꾸기
# 배부터 끝까지 출력
# 복숭아 딸기 출력
# 사과 추가
# 감 추가
# 사과 삭제
# 수박이 있으면 수박이 있습니다 출력
print(f[2])
f[-2]='망고'
print(f)
print(f[3:])
print(f[1:3])
f.append('사과')
print(f)
f.append('감')
f.remove('사과')
print(f)
if '수박' in f:
    print('수박이 있습니다')
else :
    print('수박이 없습니다')

num=[10,20,30,40,50]
# 60이 없으면60추가
if 60 not in num :
    num.append(60)
print(num)
# 20 이 있으면 70 추가하고 20삭제
if 20 in num :
    num.append(70)
    num. remove(20)
print(num)

aa = [[1,2],[3,4]]
print(aa[0][1]) # 2
print(aa[1][1]) # 4
a1=[1,2]
a2=[3,4]
a3=[a1,a2]

stu1=['홍길동',90]
stu2=['유관순',100]
student=[stu1,stu2]

# student 리스트를 사용해서 유관순 출력
# student 리스트를 사용해서 홍길동 점수를 80으로 수정
# 이순신 95점을 student 에 추가
# 만약 student[][](유관순100점이용)100점이면 100점입니다 출력
print(student[1][0])
student[0][1]=80
print(student)
student.append(['이순신',95])
print(student)
if student[1][1]==100  :
    print('100점 입니다')
