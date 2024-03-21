# print("a는 %s입니다"%"입력값")
# a="입력값"
# print("a는 %s입니다"%a)

#input은 문자열로 입력받는다
#숫자로 된 숫자를 올바르게 받기 위해선 int사용으로 강제 변환필요
#입력 
n1 = input("첫번째 숫자를 입력하세요 >>")
n2 = input("두번째 숫자를 입력하세요 >>")
#print("두 수의합 :",int(n1)+int(n2))
#문자를 숫자(실수)로 강제변환할때는 float 사용
print("두 수의 합 (float형):", float(n1)+float(n2))