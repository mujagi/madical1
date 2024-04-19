member = []

# 입력 : 이름, 점수 (input사용)
# 총 3명의 정보를 mamber 리스트에 넣으세요
for i in range(3) :
    name = input('이름 >>>')
    score = int(input('숫자 >>>'))
    stu = [name,score]
    member.append(stu)
    

print(member)

for i in range(3) :
    if member[i][1] >= 60 :
        print('{}님 합격입니다'.format(member[i][0]))
    else :
        print('{}님 불합격입니다'.format(member[i][0]))
    