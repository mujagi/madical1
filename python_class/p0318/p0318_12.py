# Car 클래스를 선언해서
# carCount 클래스 변수
# carNo에는 carCount 클래스 변수를 사용해서 숫자를 증가시켜 보세요
# carNo,color="white", door=5, tire = 4, speed = 0
# up_speed 함수를 호출하면 10씩 증가 될 수 있도록
# down_speed 함수를 호출하면 -10씩 감소되게
class Car :
    carCount = 0
    carNo = 0
    
    def __init__(self,color="white",door=5,tire=4,speed=0) :
        self.color = color
        self.door = door
        self.tire = tire
        self.speed = speed
        Car.carCount += 1
        self.carNo = Car.carCount
        

    def up_speed(self) :
        self.speed +=10
    def down_speed(self) :
        self.speed -=10
# c1 = 1,white,5,4,0 -> speed 30이 되도록
c1 = Car("white",5,4,0)
for i in range(3) :
    
    c1.up_speed()
print(c1.carNo,c1.color,c1.door,c1.tire,c1.speed)
# c2 = 2,red,5,4,0 -> speed 100
c2 = Car("red",5,4,0)
for i in range(10) :
    c2.up_speed()
print(c2.carNo,c2.color,c2.door,c2.tire,c2.speed)
# c3 = 3,silver,5,4,0 - > speed 70
c3 = Car("silver",5,4,0)
for i in range(7) :
    c3.up_speed()
print(c3.carNo,c3.color,c3.door,c3.tire,c3.speed)

# car_list 추가하고
# car_list 것을 모두 출력하시오
        
    



    
