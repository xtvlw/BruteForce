#_[N_F]_
import tkinter as tk
import time

root = tk.Tk()
final = 'password'
pos = 0
timeF = 'time'
def Click():
    global final, pos, timeF
    st = time.time()
    try:
        password = int(box.get())
        while password != pos:
            pos += 1
        final = pos
        fi = time.time()
        di = fi - st
        timeF = str('was need {:.5f} Seconds'.format(di))
    except:
        final = 'only numbers!'
    labelTime['text'] = timeF
    label['text'] = final

box = tk.Entry(root, font='calabri 12', width=50)
box.place(x=15, y=20)

button = tk.Button(root, width=50,
                   font='calabri 12', text='GO!',
                   relief='solid', command=Click)
button.place(x=15, y=100)

label = tk.Label(root, width=50,
                   font='calabri 12', text=final,
                   relief='solid', background='white')
label.place(x=15, y=150)

labelTime = tk.Label(root, width=50,
                   font='calabri 12', text=timeF,
                   relief='solid', background='white')
labelTime.place(x=15, y=200)


root.title("Brute Force")
root.geometry("490x300")
root.mainloop()
