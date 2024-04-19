fruit=['사과','복숭아', '딸기', '포도', '배']
#한라봉을 추가하고싶을때
print(fruit) # 추가 전
#리스트에 요소 추가하기
fruit.append('한라봉')
print(fruit) #추가 후

if '딸기' in fruit:
    print('딸기가 있습니다.')
else:
    print('딸기가 없습니다')
    
temp=[]
print(temp)
temp.append(1)
print(temp)
temp.append(2)
print(temp)
temp.append('홍길동')
print(temp)


# 과일 리스트에 '체리' 추가하기
fruit.append('체리')
print(fruit)

# remove : 제거
# 리스트명.remove(항목의 특정값)
fruit.remove('사과')
print(fruit)

# 변수
a=2
b=3
c=a+b
print('{}+{}={}'.format(a,b,c)) # 2+3=5
l1 = [1,2,3,4,5] # 리스트를 사용해서 2+3=5 값을 출력해보세요
print('{}+{}={}'.format(l1[1],l1[4],l1[1]+l1[4]))


#list l1에 있는 숫자들의 합을 구해보세요
print(l1[0]+l1[1]+l1[2]+l1[3]+l1[4])
