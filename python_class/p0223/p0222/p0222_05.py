# 국어,영어,수학 점수를 입력받아서 평균을 출력하세요
# 출력: 평균은 : 95점 입니다.
# 변수: kor,eng,math

#kor= 100, eng=90, math=80


kor=input('국어 점수를 입력해주세요>>>')
eng=input('영어 점수를 입력해주세요>>>')
math=input('수학 점수를 입력해주세요>>>')
kor=int(kor)
eng=int(eng)
math=int(math)
total=kor+eng+math
avg=total/3
print('평균은',avg,'입니다')