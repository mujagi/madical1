students = [["홍길동",90,100,99,299,99.97],["유관순",80,100,99,299,99.97],["김구",100,100,99,299,99.97]]
kors = 0
# students = 2차원배열
# stu = 1차원배열
for i,stu in enumerate(students) :
    print(stu)
    kors+=stu[1]
print(kors)