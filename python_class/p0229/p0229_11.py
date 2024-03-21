fruits = ['딸기','사과','자몽','포도','수박','자몽']

# 만약에 자몽을 삭제를 하고싶다
# 리스트명.remove('요소명')
# print(fruits)
# fruits.remove('자몽') # 앞 자몽부터 삭제
# print(fruits)
del(fruits[5]) # 그 위치에 있는 자몽 삭제
print(fruits)

for i,f in enumerate(fruits) : 
    print('{}는 {}번째에 있습니다.'.format(f,i))