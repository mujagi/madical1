class Car :
    car_name = ""
    color = ""
    door = 0
    length = 0
    width= 0
    speed = 0
    
    def up_speed(self,s) : # 클래스 내부에서 변수 지정시 앞에 꼭 self를 입력해줘야함
        self.speed += s
# 철수 차        
c1 = Car()
c1.car_name = "드뉴아반떼"
c1.color = "white"
c1.door = 5 
c1.length = 2000
c1.width = 1000
c1.up_speed(60) # 현재 speed에서 60을 더해줌
#c1.up_speed(40) # 현재 속도는 얼마? 100
#c1.speed = 50 # 현재 spped는 얼마? 50
# # 영희의 차를 1대 생산해서, 색상은 green, 나머지는 동일, speed = 100 설정해서 출력하시오.
c2 = Car()
c2.car_name = "드뉴아반떼"
c2.color = "green"
c2.door = 5 
c2.length = 2000
c2.width = 1000
c2.up_speed(100)
# # 방장- 디올뉴그랜저, 화이트펄, 길이:2500, 폭 : 1400, speed =150
c3 = Car()
c3.car_name = "디올뉴그랜저"
c3.color = "화이트펄"
c3.door = 5 
c3.length = 2500
c3.width = 1400
c3.up_speed(150)

print("철수 성능:",c1.car_name,c1.color,c1.door,c1.length,c1.width,c1.speed)
print("영희 성능:",c2.car_name,c2.color,c2.door,c2.length,c2.width,c2.speed)
print("방장 성능:",c3.car_name,c3.color,c3.door,c3.length,c3.width,c3.speed)
