import random
# 주택복권
# 2조 711
# 1조 740

f_num = random.randint(1,9)
l_num = random.randint(0,999999)
lotto = str(f_num)+"조"+"{:06d}".format(l_num)
print(lotto)
l_input = str(input("복권을 입력하세요.(예:1조111)"))
cnt = 0
for i in range(len(lotto),0,-1) :
    if lotto[i] == l_input[i] :
        print("1만원 당첨입니다")
    
            







# lotto = "1조740"
# # 예 : 2조 711 ->1개 번호가 맞았습니다.
# print("맞는 갯수 :",cnt-1)