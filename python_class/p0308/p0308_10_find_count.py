ss = "파이썬 공부는 즐겁습니다. 공부가 모두 재미있지는 않습니다."
print(ss.count("공부"))
print(ss.count("자바")) # 없으면 0
print(ss.find("공부")) # 존재하는문자열의 위치값이 출력
print(ss.find("자바")) # 없을땐 -1로 표현
print(ss.find("공부",7)) # 7번째 위치부터 검색시작
print(ss.rfind("공부"))  #역순으로 찾음 
print("-"*20)
print(ss.index("공부")) #파인드랑 비슷함
print(ss.index("자바")) #파인드랑 다르게 없으면 에러

print(ss.startswith("파이썬")) # 첫 시작이 파이썬으로 시작하냐 맞으면 True
print(ss.startswith("자바")) # 틀리면 False

print(ss.endswith("않습니다")) # 마지막이 않습니다로 끝나냐 맞으면 True
print(ss.endswith("재미")) # 틀리면 False