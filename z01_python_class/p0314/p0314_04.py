# 파일 1개 저장

# file open
file =open("memo.txt","w",encoding="utf-8")
try:
    # file write
    file.write("안녕하세요1.\n")
    file.write("안녕하세요2.\n")
    print(1/0)
    file.write("안녕하세요3.\n")
    file.write("안녕하세요4.\n")
except Exception as e : # Exception = 설명문 as "e" = 앞에 있는 Exception을 e로 부를께
    print("저장시 에러가 났습니다.")
    print(e)
finally : # 예외 발생해도 발생안해도 무조건 실행
    # file close
    file.close() 