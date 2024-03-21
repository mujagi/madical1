student = []

# 두명 이상의 학생의
# 이름, 국, 영, 수 점수를 입력받아 input()사용
# 리스트를 생성 후,
# student리스트에 넣어주세요
name = input('이름을 입력해주세요>>>')
kor = int(input('국어 점수를 입력해주세요>>>'))
eng = int(input('영어 점수를 입력해주세요>>>'))
math = int(input('수학 점수를 입력해주세요>>>'))
name2 = input('이름을 입력해주세요>>>')
kor2 = int(input('국어 점수를 입력해주세요>>>'))
eng2 = int(input('영어 점수를 입력해주세요>>>'))
math2 = int(input('수학 점수를 입력해주세요>>>'))
stu1=[name,kor,eng,math]
stu2=[name2,kor2,eng2,math2]
student.append(stu1)
student.append(stu2)
print(student)
# student 리스트 전체 출력