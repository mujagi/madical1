import random
random_num = random.randint(10000,99999)
print("[랜덤숫자 맞추기]")
print("랜덤숫자 :",random_num)
a_input = input("숫자 5자리를 입력하세요.")
rn = str(random_num)
ai = str(a_input)
cnt = 0

for i in range(len(rn)) :
    if rn[i] != ai[i] :
        break
    else :
        cnt += 1
if cnt == 0 :
    print("완전 꽝입니다.")
elif cnt == 1 :
    print("1개 맞췄습니다")
elif cnt == 2 :
    print("2개 맞췄습니다")
elif cnt == 3 :
    print("3개 맞췄습니다")
elif cnt == 4 :
    print("4개 맞췄습니다")
elif cnt == 5 :
    print("5개 맞췄습니다")


    
        
