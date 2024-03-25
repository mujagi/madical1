import requests

res = requests.get("https://www.google.com/")
res.raise_for_status() # 에러코드이면 자동 멈춤
print(res.text)
print("총 문자 길이 : ",len(res.text))

with open ("gogle.html","w",encoding="utf8") as f :
    f.write(res.text)