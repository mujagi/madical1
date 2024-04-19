# str.txt 파일의 내용을 모두 출력하시오.

# 파일열기
f = open("str.txt","r",encoding="utf8")
# 파일 읽기
while True :
    content = f.readline()
    if content.strip() == "" : break # 빈공백 엔터키삭제
    print(content,end="")
# 파일 닫기
f.close()
# str.txt 파일 내용을 읽어와서
# str1.txt에 그 내용을 추가해 보세요
f = open("str.txt","r",encoding="utf8")
ff = open("str1.txt","a",encoding="utf8")
while True :
    content = f.readline() # 파일 내용을읽어오기
    if content.strip() == "" : break
    ff.write(content) # 내용을 추가하기

f.close()
ff.close

f=open("str1.txt","r",encoding="utf8")
while True :
    content = f.readline()
    if content.strip() == "" : break
    print(content,end="")
f.close
    


    
    