# medical_1.csv

# 파일열기
f=open("medical_1.csv","r",encoding="utf8")
# 파일읽기
cnt = 0 
sum =0
while True :
    content = f.readline()
    if cnt == 0 :
        cnt += 1
        continue
    if content == "" : break
    print(content,end="")
    c_list = content.split(",")
    c_list[1] = int(c_list[1])
    sum+=c_list[1]
print("기초수급대상자 전체수 : ",sum)
    


    
            
# 파일닫기
f.close()
