import time
import random

for i in range(1,100+1) :
    if i%10 == 0 :
        num = random.randint(1,5)
        print(num,"초 대기")
        time.sleep(random.randint(1,5))
    print(i)