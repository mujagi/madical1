f=open("medical_2.csv","r",encoding="utf8")
cnt = 0
sum = 0
while True :
    content = f.readline()
    if cnt == 0 :
        cnt+=1
        continue
    if content == "" : break
    a_list = content.split(",")
    a_list[4] = int(a_list[4])
    sum+=a_list[4]
print(sum)

