import keyboard
import time
import tkinter
from tkinter import messagebox
#root = tkinter.Tk()
#root.withdraw()
r=(int(input("How many required: ")))
i=0
j=1
k=open('C:\\Users\\RIANE\\Desktop\\Random\\wc.txt','a')
while(1):
    if keyboard.is_pressed('.'):
        i+=j
        print(i)
        k.seek(0)
        k.truncate()
        k.write(str(i))
        time.sleep(1)
    if keyboard.is_pressed('-'):
        k.close()
        quit()
    if(i==r):
        k.close()
        messagebox.showinfo("All done ", "Total done: %d"%i)
        quit()
