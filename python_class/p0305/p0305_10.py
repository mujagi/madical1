# 학번 1000, 이름 홍길동, 학과 컴퓨터공학
student = {"학번":1000,"이름":"홍길동","학과":"컴퓨터공학"}

for key in student :
    print("{} : {}".format(key,student[key]))

# 연락처 010-1111-1111
student["연락처"] = "010-1111-1111"
print(student)

# 수정
student["이름"] = "유관순"
print(student)

# 학과 = 화학과
student["학과"] = "화학과"
print(student)
print(student["이름"]) # key의 value 값을 출력
print(student.get["이름"])

#print(student["성별"]) # key값이 없을때 None, 에러가 안남

if"이름" in student:
    print('이름 키값이 있습니다')
else :
    print("이름 키값이 없습니다")

if "성별" in student :
    print("성별 키값이 있습니다")
    print(student["성별"]) # 에러
else : 
    print(student.keys())
# student.keys() 딕셔너리의 모든 key를 출력    
print(type(student.keys()))
print(student.keys())
print(list(student.keys())) # 형 변환을 해야 list 타입으로변환이됨
print("-"*50)
# student.values() 딕셔너리의 모든 value를 출력
print(student.values())
print(list(student.values()))
for i in student.values() :
    print(i)

# items() 튜플 형태 데이터를 리턴
print(student.items())

if '이름' in student :
    print("키 값이 있습니다.")
else :
    print("키 값이 없습니다.")