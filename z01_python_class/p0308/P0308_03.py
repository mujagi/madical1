# 2차원 리스트 생성방법
# [
#    [0],[0],[0]...52개를 생성하시오
# ]
aa = [[0]*1]*52 # 얕은 복사이기에 쓸 수 없음.
bb = [ [0]*2 for i in range(52)]

cc = []
for i in range(52):
    dd = []
    for i in range(2):
        dd.append(0)
    cc.append(dd)
print(cc)

# bb[0][0] = 1
# bb[51][0] = 10
# print(bb)

# 1차원 리스트 생성방법
#[0,0,0,0,0,0...52개를 생성하시오]

# a_list = [0]*52

# b_list = []
# for i in range(52):
#     b_list.append(0)

# c_list = [ 0 for i in range(52)]

# print(a_list)
# print(b_list)
# print(c_list)