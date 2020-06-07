import tkinter as T
from tkinter import *
from tkinter.constants import *
import threading as _
from time import sleep
import os

#tk.geometry('854x480')
hi=0
coders=['Redroadsl']
if not os.path.isfile(r"./NJCFG.RD"):
    open(r"./NJCFG.RD",mode='w').close()
##Functions
def About():
    '''About this app'''
    global coders
    w=Tk()
    w.attributes("-alpha",0.85)
    w.title('秃头师们('+str(len(coders))+')')
    w.geometry('500x300')
    Label(w,text='NojavaTools是一个工具合集，为爱折腾的人设计...',font=('Arial')).pack(expand=0,fill=X)
    box=Listbox(w,width=499,height=299,bd=3)
    for mem in range(len(coders)):
        box.insert(mem-1,coders[mem-1])
    box.pack()
    
def QUIT():
    '''Quit event'''
    exit()
name=''

def hi():
    global tk,hi
    hi+=1

def changeName():
    global entry
    global var
    name=entry.get()
    var.set('Hello, '+name)
    with open(r"./NJCFG.RD",mode='w+') as file:
        file.write(name)
def displayName():
    with open(r"./NJCFG.RD",mode='r') as file:
        global var
        name=file.read()
        if not name=='':
            var.set('Hello,'+name)
#tk.geometry('854x'+str(hi))
##_.Thread(target=hi,args=()).start()
Ver='V1.0'
tk=Tk()
tk.resizable(True,True)
tk.title('NojavaTools_'+Ver)
tk.attributes("-alpha",1.0)
var=StringVar()
frame=Frame(tk, relief=RIDGE, borderwidth=5)
frame.pack(fill=BOTH,expand=1)
Label(frame,font=('Arial',30),textvariable=var).pack(fill=BOTH, expand=0)
var.set('Welcome To NojavaTools')
displayName()
Label(frame, text="Version:"+Ver).pack(fill=BOTH, expand=0)
Label(frame, text="Name:").pack(expand=0)
entry=Entry(frame, show=None, font=('Arial', 14))
entry.pack(expand=0)
Button(frame,text='[OK]',font=('Arial',15),command=changeName).pack()

Button(tk,text="Exit",font=('Arial',15),command=tk.destroy,bd=3,width=100).pack(side=BOTTOM)
Button(tk,text="秃头师们",font=('Arial',13),command=About,bd=3,width=100).pack(expand=0)
tk.geometry('854x480')
tk.mainloop()

#Listbox(root).insert(下标,项目).pack()
