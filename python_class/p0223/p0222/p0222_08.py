#원의 넓이와 원의 둘레를 출력하세요
#원의 넓이 :pi*(r**2)
#원의 넓이는:2pir

#변수:원의 반지름r
#pi = 3.14195

pi=3.14195
r=input('반지름 값을 입력해주세요>>')
r=int(r) #정수로 변환

print('원의 넓이 : {}'.format(pi*(r**2)))
print('원의 둘레 : {}'.format(2*pi*r))