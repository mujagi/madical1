class Tv :
    channel = 0
    color = "black"
    size = 65
    volume = 0
    
    # def __init__(self,channel,color,size,volume) :
    #     self.channel = channel
    #     self.color = color
    #     self.size = size
    #     self.volume = volume
       
        
    
    def up_volume(self,volume) :
        self.volume+= volume
    def down_volume(self,volume) :
        self.volume-= volume
    
    def up_channel(self,channel) :
        self.channel+=channel
    def down_channel(self,channel) :
        self.channel-=channel



# 철수=화이트,채널 10,2증가 
c1 = Tv()
c1.channel = 10
c1.up_channel(2)
c1.color = "화이트"
c1.size = Tv.size
c1.volume = Tv.volume
print(f"철수 TV : {c1.channel},{c1.color},{c1.size},{c1.volume}")

# 영희=핑크,채널 7 5증가
c2 = Tv()
c2.channel = 7
c2.up_channel(5)
c2.color = "핑크"
c2.size = Tv.size
c2.volume = Tv.volume
print(f"영희 TV : {c2.channel},{c2.color},{c2.size},{c2.volume}")
# 반장 =실버,채널 1 3증가
c3 = Tv()
c3.channel = 1
c3.up_channel(3)
c3.color = "실버"
c3.size = Tv.size
c3.volume = Tv.volume
print(f"방장 TV : {c3.channel},{c3.color},{c3.size},{c3.volume}")




    