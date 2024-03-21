import requests
# 웹에 접근해서 html 소스를 가져옴.
# res =requests.get("https://www.google.com/")
# res =requests.get("https://www.daum.net/")
res =requests.get("https://www.melon.com/index.htm")
# 200 : 정상, 403,404 : 페이지 없음,500:프로그램 에러 
print(res)
print("코드 :",res.status_code)
if res.status_code == requests.codes.ok : # requests.codes.ok = 200코드냐
    print("정상페이지 호출입니다.")
else :
    print("에러코드 발생")
    
res.raise_for_status() # 코드가 200이 아니면 오류처리에서 자동 멈춤

print("-"*60)
# request를 통해 html소스를 출력
print(res.text)