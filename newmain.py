def findbest(dic):
    return True

def lastcheck():
    choose1.config(text=select1.get())
    choose2.config(text=select2.get())
    choose3.config(text=select3.get())
    choose4.config(text=select4.get())

def layercheck():
    select4.set(value='')
    for j in range(1,100):
        try:
            top.grid_slaves(7,j)[0].grid_forget()
        except:
            pass
        
    k=1    
    for house in Beijing[select1.get()][select2.get()][select3.get()].keys():
        if Beijing[select1.get()][select2.get()][select3.get()][house]:
            tk.Radiobutton(top, text = house, variable = select4, value = house,command =lastcheck, font=("微软雅黑",size)).grid(row = 7,column = k)
        else:
            tk.Radiobutton(top, text = house, variable = select4, value = house,command =lastcheck,fg = 'red', font=("微软雅黑",size)).grid(row = 7,column = k)
        k +=1
    choose1.config(text=select1.get())
    choose2.config(text=select2.get())
    choose3.config(text=select3.get())
    choose4.config(text='')
    
def unitcheck():
    select3.set(value='')
    select4.set(value='')
    for i in range(6,8):
        for j in range(1,100):
            try:
                top.grid_slaves(i,j)[0].grid_forget()
            except:
                pass
    k=1    
    for layer in Beijing[select1.get()][select2.get()].keys():
        tk.Radiobutton(top, text = layer, variable = select3, value = layer,command =layercheck, font=("微软雅黑",size)).grid(row = 6,column = k)
        k +=1
    choose1.config(text=select1.get())
    choose2.config(text=select2.get())
    choose3.config(text='')
    choose4.config(text='')
    
def buildingcheck():
    select2.set(value='')
    select3.set(value='')
    select4.set(value='')
    for i in range(5,8):
        for j in range(1,100):
            try:
                top.grid_slaves(i,j)[0].grid_forget()
            except:
                pass
    k=1    
    for unit in Beijing[select1.get()].keys():
        tk.Radiobutton(top, text = unit, variable = select2, value = unit,command = unitcheck, font=("微软雅黑",size)).grid(row = 5,column = k)
        k +=1
    choose1.config(text=select1.get())
    choose2.config(text='')
    choose3.config(text='')
    choose4.config(text='')
    
def citycheck():
    select1.set(value='')
    select2.set(value='')
    select3.set(value='')
    select4.set(value='')
    for i in range(4,8):
        for j in range(1,100):
            try:
                top.grid_slaves(i,j)[0].grid_forget()
            except:
                pass
    k=1    
    for district in Beijing.keys():
        tk.Radiobutton(top, text = district, variable = select1, value = district,command = buildingcheck, font=("微软雅黑",size)).grid(row = 4,column = k)
        k +=1
    choose1.config(text='')
    choose2.config(text='')
    choose3.config(text='')
    choose4.config(text='')
        
        
def deleter():
    if select1.get() in Beijing.keys():
        if select2.get() in Beijing[select1.get()].keys():
            if select3.get() in Beijing[select1.get()][select2.get()].keys():
                if select4.get() in Beijing[select1.get()][select2.get()][select3.get()].keys():
                    Beijing[select1.get()][select2.get()][select3.get()][select4.get()]=False
                    
                    for j in range(1,100):
                        try:
                            top.grid_slaves(7,j)[0].grid_forget()
                        except:
                            pass
        
                    k=1    
                    for house in Beijing[select1.get()][select2.get()][select3.get()].keys():
                        if Beijing[select1.get()][select2.get()][select3.get()][house]:
                            tk.Radiobutton(top, text = house, variable = select4, value = house,command =lastcheck, font=("微软雅黑",size)).grid(row = 7,column = k)
                        else:
                            tk.Radiobutton(top, text = house, variable = select4, value = house,command =lastcheck,fg = 'red', font=("微软雅黑",size)).grid(row =7 ,column = k)
                        k +=1
                    best = findbest(Beijing_old) 
                    besthouse.config(text = best)
       

        
def recover():
    if select1.get() in Beijing.keys():
        if select2.get() in Beijing[select1.get()].keys():
            if select3.get() in Beijing[select1.get()][select2.get()].keys():
                if select4.get() in Beijing[select1.get()][select2.get()][select3.get()].keys():
                    Beijing[select1.get()][select2.get()][select3.get()][select4.get()]=True
                    
                    for j in range(1,100):
                        try:
                            top.grid_slaves(7,j)[0].grid_forget()
                        except:
                            pass
        
                    k=1    
                    for house in Beijing[select1.get()][select2.get()][select3.get()].keys():
                        if Beijing[select1.get()][select2.get()][select3.get()][house]:
                            tk.Radiobutton(top, text = house, variable = select4, value = house,command =lastcheck, font=("微软雅黑",size)).grid(row = 7,column = k)
                        else:
                            tk.Radiobutton(top, text = house, variable = select4, value = house,command =lastcheck,fg = 'red', font=("微软雅黑",size)).grid(row =7 ,column = k)
                        k +=1
                    best = findbest(Beijing_old) 
                    besthouse.config(text = best)
                
def expand_real():
    if write1.get():
        if write2.get():
            if write3.get():
                if write4.get():
                        buildings=write1.get()+'号楼'
                        layers=write2.get()+'层'
                        units=write3.get()+'单元'
                        rooms=write4.get()+'侧'
                        
                        if buildings not in Beijing.keys():                        
                            Beijing[buildings]={}
                        if layers not in Beijing[buildings].keys():
                            Beijing[buildings][layers]={}
                        if units not in Beijing[buildings][layers].keys():
                            Beijing[buildings][layers][units]={}
                        Beijing[buildings][layers][units][rooms]=False
                    
                        if buildings==select1.get():
                            if layers==select2.get():
                                if units==select3.get():
                                    layercheck()
                                else:
                                    unitcheck()
                            else:
                                buildingcheck()
                        else:                        
                            citycheck()
                                        
def cut_real():
    if select1.get() in Beijing.keys():
        if select2.get() in Beijing[select1.get()].keys():
            if select3.get() in Beijing[select1.get()][select2.get()].keys():
                if select4.get() in Beijing[select1.get()][select2.get()][select3.get()].keys():
                    
                    Beijing[select1.get()][select2.get()][select3.get()][select4.get()]=False
                    del Beijing[select1.get()][select2.get()][select3.get()][select4.get()]
                    
                    
                    if not Beijing[select1.get()][select2.get()][select3.get()]:
                        del Beijing[select1.get()][select2.get()][select3.get()]
                        unitcheck()
                        if not Beijing[select1.get()][select2.get()]:
                            del Beijing[select1.get()][select2.get()]
                            buildingcheck()
                            if not Beijing[select1.get()]:
                                del Beijing[select1.get()]
                                citycheck()
                    else:
                        layercheck()
                                



import tkinter as tk 

fid = open('data_new.txt','rt')
line = fid.readline()
Beijing = {}
while line:
    tline=line.split()
    if tline[0] not in Beijing.keys():
        Beijing[tline[0]]={}
    if tline[1] not in Beijing[tline[0]].keys():
        Beijing[tline[0]][tline[1]]={}
    if tline[2] not in Beijing[tline[0]][tline[1]].keys():
         Beijing[tline[0]][tline[1]][tline[2]]={}
    Beijing[tline[0]][tline[1]][tline[2]][tline[3]]=True

    line = fid.readline()

Beijing_old = Beijing.copy()

top = tk.Tk()
size=12
top.title("House Selector")

best = findbest(Beijing_old) 
tk.Label(top, text = '最佳房源',font=("微软雅黑",size)).grid(row = 0,column = 201)
tk.Label(top, text = '-',font=("微软雅黑",size)).grid(row = 0,column = 203)
tk.Label(top, text = '-',font=("微软雅黑",size)).grid(row = 0,column = 205)
tk.Label(top, text = '-',font=("微软雅黑",size)).grid(row = 0,column = 207)
besthouse = tk.Label(top, text = best,font=("微软雅黑",size))
besthouse.grid(row = 0,column = 990)


site = ["楼号","层数","单元","方向"]
for ss in range(4):
    tk.Label(top, text = site[ss], font=("微软雅黑",size)).grid(row = ss+4,column = 0)

select1 = tk.StringVar()
select2 = tk.StringVar()
select3 = tk.StringVar()
select4 = tk.StringVar()

cl = 1
for district in Beijing.keys():
    tk.Radiobutton(top, text = district, variable = select1, value = district, command = buildingcheck, font=("微软雅黑",size)).grid(row = 4,column = cl)
    cl +=1

tk.Button(top, text = "标记删除", command = deleter,font=("微软雅黑",size)).grid(row = 999,column = 200)
tk.Label(top, text = '选择：',font=("微软雅黑", 15)).grid(row = 998,column = 201)
choose1 = tk.Label(top, text = '',font=("微软雅黑",size))
choose2 = tk.Label(top, text = '',font=("微软雅黑",size))
choose3 = tk.Label(top, text = '',font=("微软雅黑",size))
choose4 = tk.Label(top, text = '',font=("微软雅黑",size))
choose1.grid(row = 998,column = 202)
tk.Label(top, text = '-',font=("微软雅黑",size)).grid(row = 998,column = 203)
choose2.grid(row = 998,column = 204)
tk.Label(top, text = '-',font=("微软雅黑",size)).grid(row = 998,column = 205)
choose3.grid(row = 998,column = 206)
tk.Label(top, text = '-',font=("微软雅黑",size)).grid(row = 998,column = 207)
choose4.grid(row = 998,column = 208)
tk.Button(top, text = "标记恢复", command = recover,font=("微软雅黑",size)).grid(row = 999,column = 998)


write1=tk.StringVar()
write2=tk.StringVar()
write3=tk.StringVar()
write4=tk.StringVar()
tk.Entry(top,textvariable = write1,font=("微软雅黑",size),width=3).grid(row = 1000,column = 202)
tk.Label(top, text = '号楼',font=("微软雅黑", size)).grid(row = 1000,column = 203)
tk.Entry(top,textvariable = write2,font=("微软雅黑", size),width=3).grid(row = 1000,column = 204)
tk.Label(top, text = '层楼',font=("微软雅黑", size)).grid(row = 1000,column = 205)
tk.Entry(top,textvariable = write3,font=("微软雅黑", size),width=4).grid(row = 1000,column = 206)
tk.Label(top, text = '单元',font=("微软雅黑", size)).grid(row = 1000,column = 207)
tk.Entry(top,textvariable = write4,font=("微软雅黑", size),width=3).grid(row = 1000,column = 208)
tk.Label(top, text = '侧',font=("微软雅黑", size)).grid(row = 1000,column = 209)
tk.Button(top, text = "扩展房源",font=("微软雅黑", size),command = expand_real).grid(row = 1000,column = 201)
tk.Button(top, text = "删除房源",font=("微软雅黑", size),command = cut_real).grid(row = 999,column = 999)

top.mainloop()
