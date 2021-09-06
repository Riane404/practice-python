import time
import os
time.sleep(0)
# Runs on startup
i=time.ctime(time.time())
print(i)

f = open('C:\\Users\\RIANE\\Desktop\\Python practice\\file.txt', 'a')
f.write(i)
f.write('\n')
f.close()





