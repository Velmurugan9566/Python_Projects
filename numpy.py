import numpy as np
li=np.random.randint(low=12,high=40,size=20)
print(li)
import datetime
import time
while True:
    d=datetime.datetime.now()
    print(d)
    time.sleep(1)
    
ty=datetime.date.today()

print(ty.year)
print(ty.day)
print(ty.month)
#print(dir(datetime))
