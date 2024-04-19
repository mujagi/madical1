season = input("월을 입력해주세요>>")
se = season[0:-1]
s=int(se)
if s==12 or s==1 or s==2 :
    print("겨울입니다.")
elif s==3 or s==4 or s==5 :
    print("봄입니다.")
elif s==6 or s==7 or s==8 :
    print("여름입니다.")
elif s==9 or s==10 or s==11 :
    print("가을입니다.")
