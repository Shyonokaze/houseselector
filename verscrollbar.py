# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 16:19:29 2017

@author: pyh
"""
def color():
    Beijing_counter=0
    for choice in Beijing.keys():
        if Beijing[choice][0]:
            Beijing_lb.itemconfig(Beijing_counter,fg='black',selectforeground='white')
        else:
            Beijing_lb.itemconfig(Beijing_counter,fg='red',selectforeground='Indigo')
        Beijing_counter +=1

def deleter(event):
    Beijing[Beijing_lb.get(Beijing_lb.curselection())][0]=(Beijing[Beijing_lb.get(Beijing_lb.curselection())][0]-1)**2
    color()
    Beijing_best.config(text='最佳房源：%s'%findbest())
    if Beijing[Beijing_lb.get(Beijing_lb.curselection())][0]:
        mem_lb.insert(tk.END,'恢复房源%s'% Beijing_lb.get(Beijing_lb.curselection()))
    else:
        mem_lb.insert(tk.END,'删除房源%s'%Beijing_lb.get(Beijing_lb.curselection()))
    mem_lb.yview(tk.END)

def findbest():
    bestchoice='无'
    for i in range(len(Beijing_order)):
        if Beijing_order[i] in Beijing.keys():
            if Beijing[Beijing_order[i]][0]:
                bestchoice=Beijing_order[i]
                break
    return bestchoice

def save():
    check_print=tk.messagebox.askokcancel(title='确定', message='确定要保存文件么？')
    if check_print:
        fid3=open('data_new.txt','wt')        
        for choice in Beijing.keys():
            print(choice,file=fid3,end=' ')
            if Beijing[choice][0]:
                print('True',file=fid3,end=' ')
            else:
                print('False',file=fid3,end=' ')
            if Beijing[choice][1]:
                print('new',file=fid3)
            else:
                print('',file=fid3)
        fid3.close()
        
def reset():
    import os
    import shutil
    check_reset=tk.messagebox.askokcancel(title='注意！', message='您将失去所有记录，确定要重置文件么？')
    if check_reset:
        try:
            os.remove('data_new.txt')
        except:
            pass
        shutil.copy('data.txt','data_new.txt')
        for choice in Beijing.keys():
            Beijing[choice][0]=1
        color()

        Beijing_best.config(text='最佳房源：%s'%findbest())
        mem_lb.delete(0,tk.END)
        
        
        
        
                
def printnew():
    check_print=tk.messagebox.askokcancel(title='确定', message='确定要打印已被选的房源并保存么？')
    if check_print:
        fid3=open('data_new.txt','wt')
        for choice in Beijing.keys():
            print(choice,file=fid3,end=' ')
            if Beijing[choice][0]:
                print('True',file=fid3,end=' ')
            else:
                print('False',file=fid3,end=' ')
            if Beijing[choice][1]:
                print('new',file=fid3)
            else:
                print('',file=fid3)
        fid3.close()

        fid4=open('被选的房源.txt','wt')
        for choice in Beijing.keys():
            if not Beijing[choice][0]:
                print(choice,file=fid4)    
        fid4.close()
        
            
import tkinter as tk
from tkinter import messagebox
fid = open('data_new.txt','rt')
line = fid.readline()
Beijing = {}
while line:
    tline=line.split()
    if tline[4]=='False':
        Beijing[tline[0]+' '+tline[1]+' '+tline[2]+' '+tline[3]]=[0,0]
    else:
        Beijing[tline[0]+' '+tline[1]+' '+tline[2]+' '+tline[3]]=[1,0]
    
    try:    
        if tline[5]:
            Beijing[tline[0]+' '+tline[1]+' '+tline[2]+' '+tline[3]][1]=1
    except:
        pass
    line = fid.readline()        
fid.close()

fid2=open('data_old.txt','rt')
line = fid2.readline()
Beijing_order = []

while line:
    tline=line.split()
    mai=tline[0]+' '+tline[1]+' '+tline[2]+' '+tline[3]
    Beijing_order.append(mai)  
    line = fid2.readline()
fid2.close()


top = tk.Tk()
top.title("House Selector")
Beijing_lb = tk.Listbox(top,font=('微软雅黑',15),height = 20)
Beijing_sl = tk.Scrollbar(top,command=Beijing_lb.yview)
Beijing_best = tk.Label(top,text='最佳房源：%s'%findbest(),font=('微软雅黑',15))
Beijing_best.grid(row = 0,column = 0,columnspan=2)
Beijing_lb.config(yscrollcommand = Beijing_sl.set)
Beijing_lb.grid(row = 1,column = 0,sticky='NSEW')
Beijing_sl.grid(row = 1,column = 1,sticky='NSW')

mem_lb = tk.Listbox(top,font=('微软雅黑',10),height = 4)
mem_lb.grid(row = 2,column = 0,sticky='EW')

for choice in Beijing.keys():
    Beijing_lb.insert(tk.END,choice)
color()

Beijing_lb.bind('<Return>',deleter)
Beijing_lb.bind('<Double-Button-1>',deleter)

tk.Button(top, text = "打印已选",font=("华文彩云", 15),command = printnew).grid(row = 1,column = 999,sticky='S')

tk.Button(top, text = "保存",font=("华文彩云", 15),command = save).grid(row = 2,column = 999)
tk.Button(top, text = "重置",font=("华文彩云", 15),command = reset).grid(row = 0,column = 999)
        
    
top.mainloop()
