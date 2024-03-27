## 파일을 읽어와서 출력하시오.

# 파일열기
# medical 폴더안 member.csv
# medical>h0327>aaa 폴더안 h0327/aaa/member2.csv
with open("c:/workspace/madical1/madical1/h0322/h0327/aaa/member2.csv","r",encoding="utf-8") as f:
    while True :
        txt = f.readline()
        if txt == "" : break
        mem = txt.split(",")
        print(mem[0],mem[1])
    
f.close