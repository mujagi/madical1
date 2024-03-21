# 숫자 5개를 입력받아 5개를 출력하시오 .
# 1. 숫자 2개 입력
# 2. 숫자 2개 출력
nums = []
for i in range(0,5) :
    nums.append(int(input("숫자를 입력하세요.")))
# 5개의 합을 구하시오
sum = 0
for num in nums :
    sum += num
print("합계 : ",sum)

    

