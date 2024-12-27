import random
import time
a=0
while a<100:
    time.sleep(0.01)
    a+=1
    
    s=f"[[False,False],[{random.randint(-10,10)},{random.randint(-10,10)}],0]"
    open("./serverD/command","w").write(s)

open("./serverD/command","w").write("[[False,False],[0,0],0]")