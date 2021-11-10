import tkinter as tk
import random
import threading
import time

def dow(a,b):
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    '''
    a = random.randrange(0,width)
    b = random.randrange(0,height)
    '''
    window.title("生日快乐")
    window.geometry("150x120" + "+" + str(a) + "+" + str(b))
    tk.Label(window,
        text = "生日快乐",
        bg = "Purple",
        font = ('楷体',19),
        fg = '#fcce03',
        width = 13,
        height = 5).pack()
    window.overrideredirect(1)
    window.mainloop()

threads = []
threads2 = []
threads3 = []
threads4 = []
threads5 = []
threads6 = []
threads7 = []
for i in range(8):
    t = threading.Thread(target=dow,args = (220,125*i+30))
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()

for j in range(8):
    t2 = threading.Thread(target=dow,args = (520,125*j+30))
    threads2.append(t2)
    time.sleep(0.1)
    threads2[j].start()

for k in range(8):
    t3 = threading.Thread(target=dow,args = (820,125*k+30))
    threads3.append(t3)
    time.sleep(0.1)
    threads3[k].start()

for x in range(8):
    t4 = threading.Thread(target=dow,args = (1120,125*x+30))
    threads4.append(t4)
    time.sleep(0.1)
    threads4[x].start()

for y in range(3):
    t5 = threading.Thread(target=dow,args = (1270+y*150,905))
    threads5.append(t5)
    time.sleep(0.1)
    threads5[y].start()

for n in range(7):
    t6 = threading.Thread(target=dow,args = (1570,780-125*n))
    threads6.append(t6)
    time.sleep(0.1)
    threads6[n].start()

for m in range(2):
    t7 = threading.Thread(target=dow,args = (1420-m*150,30))
    threads7.append(t7)
    time.sleep(0.1)
    threads7[m].start()