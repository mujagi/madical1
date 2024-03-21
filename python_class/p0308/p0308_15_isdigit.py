print("1234".isdigit()) # 숫자인지  확인
print("abc".isalpha()) #문자인지 확인
print("a1bc".isalpha()) # 1이 들어있으니 불가능
print("abc".islower()) #소문자인지 확인
print("ABC".upper()) # 대문자인지 확인
print(" ".isupper()) # 아예 빈공백인지 확인
print(" ㅣ".isupper()) # 글자가 하나라도 있기때문에 False
