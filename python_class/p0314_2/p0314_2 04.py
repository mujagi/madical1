# 파일 읽어오기

# 1. 파일 열기
# read() : 모든 문자열을 가져옴
# readline() : 한줄씩 가져옴
# readlines() : 1줄씩 리스트 타입에 입력해서 모두 가져옴 
# 3. 파일 닫기

# 파일 확인
import os
if os.path.exists("str.txt") :  # 파일 존재 확인
    
    with open("str.txt","r",encoding="utf8")as f : #변수명을 뒤에
        txt_list=f.readlines()
        for txt in txt_list :
            print(txt,end="")
        print()


        

# f.close() 생략가능
    







# # readlines
# f = open("str.txt","r",encoding="utf8")
# # 1줄씩 리스트 타입으로 저장
# txt_list = f.readlines()
# print(txt_list)
# print(txt_list[0])
# f.close() # 파일 종료를 반드시 해야함


# readline 으로 읽어오기 readline = 1줄을 str타입으로 가져옴
# f= open("str.txt","r",encoding="utf-8")
# while True :
#     txt = f.readline()
#     if txt == "" : break
    
#     print(txt,end="")

# print("모든 파일을 읽어 왔습니다.")