# card_list = [['spade', 'A'], ['spade', 2], ['spade', 3], ['spade', 4], ['spade', 5], ['spade', 6], ['spade', 7], 
#              ['spade', 8], ['spade', 9], ['spade', 10], ['spade', 'J'], ['spade', 'Q'], ['spade', 'K'], 
#              ['diamond', 'A'], ['diamond', 2], ['diamond', 3], ['diamond', 4], ['diamond', 5], ['diamond', 6], ['diamond', 7], 
#              ['diamond', 8], ['diamond', 9], ['diamond', 10], ['diamond', 'J'], ['diamond', 'Q'], ['diamond', 'K'], 
#              ['heart', 'A'], ['heart', 2], ['heart', 3], ['heart', 4], ['heart', 5], ['heart', 6], ['heart', 7], 
#              ['heart', 8], ['heart', 9], ['heart', 10], ['heart', 'J'], ['heart', 'Q'], ['heart', 'K'], 
#              ['clover', 'A'], ['clover', 2], ['clover', 3], ['clover', 4], ['clover', 5], ['clover', 6], ['clover', 7], 
#              ['clover', 8], ['clover', 9], ['clover', 10], ['clover', 'J'], ['clover', 'Q'], ['clover', 'K']]
# 딕셔너리 형태로 변경
import random

card_list = [{},{}]

shape_list = ['spade','diamond','heart','clover']
num_list = [0]*13

for i in range(1,14):
    num_list[i-1] = i

num_list[0] = 'A'
num_list[10] = 'J'
num_list[11] = 'Q'
num_list[12] = 'K'
card_list = [[0]*2 for i in range(52)]
cnt = 0

for i in shape_list: # 'spade','diamond','heart','clover'
    for j in range(13):
        card_list[cnt] = {'shape' : i, 'num' : num_list[j]}
        cnt += 1
# print(card_list)

random.shuffle(card_list)

# print(card_list)

# 모양 : spade, 번호 : 1
arr_num = 0
while True:
    print('[ 카드게임 ]')
    print('-'*30)
    print('1. 카드 1장 뽑기')
    print('2. 카드 5장 뽑기')
    print('0. 종료')
    # card_list[0]['shape']
    c_num = int(input('번호를 선택하세요 : '))
    if c_num == 1:
        print('모양 : {}, 번호 : {}'.format(card_list[arr_num]['shape'], card_list[arr_num]['num'])) # 0 6
        arr_num += 1
    elif c_num == 2:
        for i in range(5):
            print('모양 : {}, 번호 : {}'.format(card_list[arr_num]['shape'], card_list[arr_num]['num'])) # 1,2,3,4,5 7,8,9,10,11,12
            arr_num += 1
    elif c_num == 0:
        print('종료합니다.')
        break