import datetime #날짜 관련 기능을 가져옴
now = datetime.datetime.now()
year=now.year
#print(now)
#print(now.year)#연도
#print(now.month)#월
#print(now.day)#일

#print(now.hour)#시간
#print(now.minute)#분
#print(now.second)#초

#시간을 사용해서 지금이 오전이면 오전입니다. 오후면 오후입니다 출력
if now.hour>12 :
    print('오후입니다')
else :
    print('오전입니다')
if now.hour==17:
    print('현재는 17로 오후입니다')
    
# 1. 짝수달입니다. 홀수달 입니다
m=now.month
if m%2==0 :
    print("짝수달입니다")
else :
    print("홀수달입니다")
if m<=11 :
    print('겨울입니다')
else :
    print('겨울이 아닙니다')
    
#월
#겨울입니다. 겨울이 아닙니다
print(type(m)) #type을 알아보는 방법:<class'int'> <- 이 코드의 타입