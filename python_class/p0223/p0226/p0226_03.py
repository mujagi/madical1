# list
# 데이터를 잘 관리하기 위해서 묶어서 관리하는 자료형
# 리스트 변수명 = [요소1, 요소2, 요소3 ....]
lis1 = []
lis2 = [0,2,4]
lis3 = ['짝수', '홀수']
lis4 = ['홍길동', 100,100,100]
lis5 = [ '짝수',[2,4,6], '홀수', [1,3,5]] # list 자체도 하나의 요소로 사용가능

# 인덱싱 (index) 리스트를 검색, 접근
# index 는 0부터 시작
numL = [0,1,2,3,4]
#       0 1 2 3 4 순서로 
#      -5 -4 -3 -2 -1 순서
# 0을 출력하고 싶을 때
print(numL[0])
print(numL[-5])
# 인덱스의 범위를 넘어가면 오류출력 numL[10] <<< 오류

# 인덱스를 가지고 리스트의 특정 요소의 값을 수정할 수 있다.
# 리스트명[n] = 값
numL[0] = 20
print(numL)
numL[-1] = 222
print(numL)
# lis5 = [ '짝수',[2,4,5], '홀수', [1,3,5]]
# 숫자2에 접근하기 위해서는 ?
print(lis5[1]) # [2,4,6]
print(lis5[1][0])
# 숫자 5에 접근
print(lis5[3][2])
print(lis5[-1][-1])

# 리스트 슬라이싱: 리스트 자르기
# 콜론 : 를 사용해서 ~에서 ~까지
# 리스트명 [시작인덱스: 끝인덱스 +1]
print(numL [2:4]) # 2이상 4미만
print(numL[1:]) # 1번 인덱스부터 끝까지
print(numL[:3]) # 처음부터 3번 미만까지(2번 인덱스까지) 
print(numL[:]) # 처음부터 끝까지
print(numL[1:-1]) # 1번부터 끝바로 앞까지

# 리스트의길이 : len(리스트명)
print(len(lis1))
print(len(lis2)) 
print(len(lis5))
print(len(numL))

# 특정요소 삭제 : del(리스트명[n])
aa = [100,200,300,400,500,600,700]
print(aa)
del(aa[1])
print(aa)
del(aa[3:5])
print(aa)

# 리스트 값 추가 : 리스트명, append(값)
aa=[100,200,300,400,500,600,700]
aa.append(800)
print(aa)
aa.append('숫자')
print(aa)
aa.append([1,2,3])
print(aa)

# 리스트에서 특정값 제거
# 리스트명 .remove(값)
aa.remove(200)
print(aa)

aa.append(100)
aa.append(400)
aa.append(100)
print(aa)
aa.remove(100) # 같은 값이 2개 이상
print(aa) # 맨 앞 100만 제거

#aa.remove(1) # 오류 1은 존재 x []안의 값은 별개로 지정되지 않음

# 요소확인 : 내부 포함된 요소의 존재를 확인하는 방법
# in, not in
print(100 in aa)
print(200 not in aa)

f = ['사과', '딸기', '복숭아', '수박', '배']
print('딸기' in f)

if '사과' in f :
    print('사과가 있습니다')
else:
    print('사과가 없습니다')

if '사과' not in f :
    print('사과가 없습니다')
else:
    print('사과가 있습니다')
    