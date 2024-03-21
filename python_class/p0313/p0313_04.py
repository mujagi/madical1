# 다른 파일에 있는 함수를 사용 할 때
# # import math -> 사용방법
# from math import *
# #import lotto
# from lotto import *
# while True :
#     lotto.screen()
import math as m # 모듈명을 줄여서 사용가능 , 별칭부여
import lotto as lo 
l = [0]*45
#lo.screen()
#lo.num_generate(l)


# # ceil - 올림
print(m.ceil(12.2)) # 13
# # floor - 버림
print(m.floor(12.9)) # 12
# #round - 반올림
# print(round(12.6)) # 13

print(dir(m))