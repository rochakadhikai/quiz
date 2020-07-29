import random
import os
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('QUIZ')
root.geometry('1200x750')
f_opt = [("Music", "m"), ("Movies", "mo"), ("Science", "s"), ("Literature", "l"), ("Sports", "sp"), ("History", "h"),
         ("Geography", "g"), ("All", "a")]
t = [("30 sec", 30), ("1 min", 60), ("1 min 30 sec", 90), ("2 min", 120), ("3 min", 180)]
n_o_q = [8, 12, 14, 16]
roundsel = StringVar()
answer = StringVar()
answer.set('null')
time = IntVar()
noq = IntVar()
noq.set(6)
time.set(0)
roundsel.set("null")
i = j = k = 3
c = 0
mainlist = []
minilist = []
points = 0
sp_list = []
ans_list = []

headline = Label(root, text='Quiz-Mania', font=("Candara", 30), fg='blue')
headline.grid(row=0, column=0, padx=20, pady=20, columnspan=4)

nm = Label(root, text="Name: ", font=('Candara', 15), anchor='e')
nm.grid(row=1, column=0, padx=10, pady=40)
namebox = Entry(root, width=50, borderwidth=5)
namebox.grid(row=1, column=1, padx=10, pady=40)
r = Label(root, text="Select your round: ", font=("Candara", 15), fg='red')
r.grid(row=2, column=0, padx=10, pady=20)
tm = Label(root, text="Select timer: ", font=("Candara", 15), fg='green')
tm.grid(row=2, column=1, padx=30, pady=20)
qs = Label(root, text="Select no. of questions per round: ", font=("Candara", 15))
qs.grid(row=2, column=2, padx=30, pady=20)

for round, code in f_opt:
    a = Radiobutton(root, text=round, font=("corbel", 10), variable=roundsel, value=code, anchor=W)
    a.grid(row=i, column=0, padx=20)
    i = i + 1
    mainlist.append(a)

for t1, t2 in t:
    b = Radiobutton(root, text=t1, font=("corbel", 10), variable=time, value=t2, anchor=W)
    b.grid(row=j, column=1, padx=20)
    j += 1
    mainlist.append(b)

for q in n_o_q:
    d = Radiobutton(root, text=q, font=("corbel", 10), variable=noq, value=q, anchor=W)
    d.grid(row=k, column=2, padx=20)
    k += 1
    mainlist.append(d)

sub = Button(root, width=20, text="Submit", borderwidth=5,
             command=lambda: clicked(roundsel.get(), int(time.get()), noq.get()))
sub.grid(row=11, column=2)


def timer():
    global h
    if h >= 0:
        t2.configure(text=h, font=("Candara", 15))
        h = h - 1
        t2.after(1000, timer)
    else:
        messagebox.showinfo("Timeout", "Score :" + str(points))
        return


def q_print(que, ans):
    s1 = Label(root, text="Round: Sports", font=("Candara", 20), fg='blue')
    s1.pack(side=TOP, anchor=NW, padx=30, pady=50)
    minilist.append(s1)
    s2 = Label(root, text=que, font=("Candara", 20))
    s2.pack(padx=55, pady=10)
    minilist.append(s2)
    t3 = Label(root, text="Score: " + str(points), font=("Candara", 15), fg='green')
    t3.pack(side=TOP, anchor=NW)
    minilist.append(t3)
    checkboxes(ans)


def minidestroy():
    global minilist
    for i in minilist:
        i.destroy()
    minilist = []


def checkboxes(ans_list):
    m = []
    org_ans = ''
    spam = {}
    o = 1
    l = ans_list.split(' ')
    for j in l:
        j = str.rstrip(j)
        if j not in m and j != '':
            m.append(j)
            spam.setdefault(j, j)
        else:
            org_ans = j
            print(org_ans)
    for l, m in spam.items():
        a = Radiobutton(root, text=l, font=("Corbel", 15), variable=answer, value=m)
        a.pack()
        minilist.append(a)

    bt = Button(root, text="Next", font=("Candara", 12), fg='white', bg='black',
                command=lambda: check_ans(answer.get(), org_ans))
    bt.pack()
    minilist.append(bt)


def destroy():
    for i in mainlist:
        i.destroy()
    sub.destroy()
    headline.destroy()
    nm.destroy()
    namebox.destroy()
    r.destroy()
    tm.destroy()
    qs.destroy()


def check_ans(ans, org):
    global points, c
    if org == ans:
        points += 1
    c += 1
    minidestroy()
    q_print(sp_list[c], ans_list[c])


def que_print(que_op, ans_op):
    while len(sp_list) < len(que_op):
        r = random.randint(0, 4)
        r1 = que_op[r]
        a1 = ans_op[r]
        if r1 not in sp_list:
            sp_list.append(r1)
            ans_list.append(a1)
        else:
            continue
    q_print(sp_list[c], ans_list[c])


def set_everything():
    h1 = Label(root, text='Quiz-Mania', font=("Candara", 30), fg='orange')
    h1.pack(side=TOP)
    global h, t2, points
    h = int(time.get())
    t2 = Label(root, text=h, font=("Candara", 15), fg='red')
    t2.pack(side=RIGHT, anchor=NE)


def clicked(r, t, n):
    global time
    name = namebox.get()
    if r == 'null' or t == 0 or n == 6 or name == '':
        b = messagebox.showinfo("Error", "Field missing")
        if b == 'ok':
            return
    else:
        destroy()
        set_everything()
        timer()
        if r == 'sp':
            que_op = open('E:\\turtle\\quizquestions\\sports.txt').readlines()
            ans_op = open('E:\\turtle\\quizquestions\\sportsans.txt').readlines()
            que_print(que_op, ans_op)
        root.mainloop()


que_op = open('E:\\turtle\\quizquestions\\sports.txt').readlines()
ans_op = open('E:\\turtle\\quizquestions\\sportsans.txt').readlines()
print(que_op)
print(ans_op)
root.mainloop()
