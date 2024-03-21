stu_no="1"
stu_nam=input("이름을 입력하세요")
kor=input("숫자를 입력하세요:")
eng=input("숫자를 입력하세요:")
math=input("숫자를 입력하세요:")
total=int(kor)+int(eng)+int(math)
hipe=3
avg=total/3
rank=1
print("번호\t이름\t국어\t수학\t합계\t평균\t등수")
print("%s\t%s\t%s\t%s\t%s\t%d\t%f\t%d"%(stu_no,stu_nam,kor,eng,math,total,avg,rank))
      