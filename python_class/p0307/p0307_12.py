# 공간을 만들어놓고 for문 사용
list = [0]*10
for i in range(10) :
    list[i] = i+1
print(list)
# 컴프리헨션을 사용하는방법
list1 = [i+1 for i in range(10)]    
#2차원 리스트 -크기가 지정이 안됨
a_list = []
a_list.append(0) # 리스트 append 추가를 하게 되면 속도가 느림.
a_list.append(1)
a_list.append(2)
a_list[0] = 3
print(a_list)