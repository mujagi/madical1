import datetime


now=datetime.datetime.now() #현재를 가져옴
print(now)
# 2024-02-23 13:03:09.195335
month=now.month #현재 월
#현재가 봄 여름가을 겨울
#12,1,2 겨울. 3,4,5 봄. 6,7,8 여름 9,10,11 가을
#elif를 사용하세요
if month==12 or month==1 or month==2  :
    print('겨울')
    if month==12 :
        print('12월 입니다')
    if month==1 :
        print('1월 입니다')
    if month==2 :
        print('2월 입니다')
        
elif month==3 or month==4 or month==5 :
    print('봄')
    if month==3 :
        print('3월 입니다')
    if month==4 :
        print('4월 입니다')
    if month==5 :
        print('5월 입니다')
elif month==4 or month==5 or month==6 :
    print('여름')
    if month==6 :
        print('6월 입니다')
    if month==7 :
        print('7월 입니다')
    if month==8 :
        print('8월 입니다')
elif month==9 or month==10 or month==11 :
    print('가을')
    if month==9 :
        print('12월 입니다')
    if month==10 :
        print('1월 입니다')
    if month==11 :
        print('2월 입니다')
    