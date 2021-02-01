import datetime
y=datetime.datetime(2020,5,6,4,5,6)
print(y)
import time
print(time.ctime(time.time()))
for i in range(0,3):
    print(i)
    time.sleep(2)
print()
z=time.localtime(time.time())
print(z)
print(type(z))
p=time.asctime(z)
print(p)
print()
import calendar
print(calendar.month(2020,3))
