# 중첩 if

a=97
#if a>90:
    #print('a가 90보다 큽니다')
#else:
    #print('a가 90보다 작습니다')
if a>90:
    print('90보다 큽니다')
    if a<95:
        print('95보다 작습니다')
    else:
        print('95보다 큽니다')
else:
    print('90보다 작습니다')


#만약 사과의상태가 good 이며
# 1000원 이하이면 [10r개 구매]
# 1000원 보다  비싸면 [3개 구매]를 출력
# 사과의 상태가 'good'이 아니면 [사과를 구매하지 않습니다]    
apple='good'
price=1000
if apple == 'good' :
    if price<=1000 :
        print('10개구매') 
    else :
        print('3개 구매')
else :
        print('사과를 구매하지 않습니다')
        
#숫자를 하나 입력받아서 
# 100보다 큰 수면서 짝수면 짝수, 홀수면 홀수출력
# 100보다 작은경우 [100보다 작다] 출력

n=int(input('숫자를 입력해주세요>>'))

if n>100 :
    if n%2==0 :
        print('짝수입니다')
    else :
        print('홀수입니다')
else :
    print('100보다 작습니다')