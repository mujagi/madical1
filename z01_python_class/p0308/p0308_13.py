# map : 문자열을 정수형으로모두변환해서 리스트 저장

today_list = ['2024','03','08']
#today_list[0]=int(today_list[0])+10
#print(today_list[0])
t_list = list(map(int,today_list))
print(t_list)


#정수형을 문자로 변환해서 리스트 저장
int_list = [10,20,30,40,50]
str_list = list(map(str,int_list))
print(str_list)

# 리스트의 데이터 타입 : str

# a_list = list(map(str,range(10)))
# print(a_list)

# input의 데이터 int변경해서 list 저장
a_list = list(map(int,input("숫자입력 :")))
print(a_list)


