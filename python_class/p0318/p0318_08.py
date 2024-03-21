class Card : # 4rodmlqustn :kind,number,width, height
    kind = ""
    number = ""
    width = 0 # 클래스변수
    height = 0 # 클래스변수
    def __init__(self,kind,number) :
        self.kind = kind
        self. number = number
        Card.width = 100
        Card.height = 200
        
        
        
# 클래스 5개를 생성해서 kind="shape",number=1,2,3,4,5
# 클래스를 출력하시오
# kind = ["SPADE","DIAMOND","HEART","CLOVER"]
# number = ["1","2","3","4","5"]
card_list = []
card_list.append(Card("SPADE","1"))

print("리스트 개수 :",len(card_list))
for i in range(13) :
    card_list.append(Card("SPADE",i+1))
    print("리스트 출력 :",card_list[0].kind,card_list[i].number)
    


# # 52장 카드 생성        
# number = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
# card_list = []
# for i in range(4) :
#     for j in range(13) :
#         c = Card(kind[i],number[j]) #객체선언
#         card_list.append(Card(kind[i],number[j])) #리스트추가

# for i in range(52) :
#     c = card_list[i] # c=Card 객체
#     print("카드 출력 : ",c.kind,c.number)


            





