def findbest(dic):
    return dic['东城区']['a']['g']['h']['j']

def layercheck():
    
    for j in range(1,100):
        try:
            top.grid_slaves(8,j)[0].grid_forget()
        except:
            pass
        
    k=1    
    for house in Beijing[select1.get()][select2.get()][select3.get()][select4.get()].keys():
        if Beijing[select1.get()][select2.get()][select3.get()][select4.get()][house]:
            tk.Radiobutton(top, text = house, variable = select5, value = house,command =layercheck).grid(row = 8,column = k)
        else:
            tk.Radiobutton(top, text = house, variable = select5, value = house,command =layercheck,fg = 'red').grid(row = 8,column = k)
        k +=1
        
def unitcheck():
    
    for i in range(7,9):
        for j in range(1,100):
            try:
                top.grid_slaves(i,j)[0].grid_forget()
            except:
                pass
    k=1    
    for layer in Beijing[select1.get()][select2.get()][select3.get()].keys():
        tk.Radiobutton(top, text = layer, variable = select4, value = layer,command =layercheck).grid(row = 7,column = k)
        k +=1
        
def buildingcheck():
    
    for i in range(6,9):
        for j in range(1,100):
            try:
                top.grid_slaves(i,j)[0].grid_forget()
            except:
                pass
    k=1    
    for unit in Beijing[select1.get()][select2.get()].keys():
        tk.Radiobutton(top, text = unit, variable = select3, value = unit,command = unitcheck).grid(row = 6,column = k)
        k +=1
        
def districtcheck():
    for i in range(5,9):
        for j in range(1,100):
            try:
                top.grid_slaves(i,j)[0].grid_forget()
            except:
                pass
    
    k=1    
    for building in Beijing[select1.get()].keys():
        tk.Radiobutton(top, text = building, variable = select2, value = building,command = buildingcheck).grid(row = 5,column = k)
        k +=1
        
def deleter():
    if select2.get() in Beijing[select1.get()].keys():
        if select3.get() in Beijing[select1.get()][select2.get()].keys():
            if select4.get() in Beijing[select1.get()][select2.get()][select3.get()].keys():
                if select5.get() in Beijing[select1.get()][select2.get()][select3.get()][select4.get()].keys():
                    Beijing[select1.get()][select2.get()][select3.get()][select4.get()][select5.get()]=False
        
                    for j in range(1,100):
                        try:
                            top.grid_slaves(8,j)[0].grid_forget()
                        except:
                            pass
        
                    k=1    
                    for house in Beijing[select1.get()][select2.get()][select3.get()][select4.get()].keys():
                        if Beijing[select1.get()][select2.get()][select3.get()][select4.get()][house]:
                            tk.Radiobutton(top, text = house, variable = select5, value = house,command =layercheck).grid(row = 8,column = k)
                        else:
                            tk.Radiobutton(top, text = house, variable = select5, value = house,command =layercheck,fg = 'red').grid(row = 8,column = k)
                        k +=1
                    best = findbest(Beijing) 
                    besthouse.config(text = best)
       

        
def recover():
    if select2.get() in Beijing[select1.get()].keys():
        if select3.get() in Beijing[select1.get()][select2.get()].keys():
            if select4.get() in Beijing[select1.get()][select2.get()][select3.get()].keys():
                if select5.get() in Beijing[select1.get()][select2.get()][select3.get()][select4.get()].keys():
                    Beijing[select1.get()][select2.get()][select3.get()][select4.get()][select5.get()]=True
        
                    for j in range(1,100):
                        try:
                            top.grid_slaves(8,j)[0].grid_forget()
                        except:
                            pass
        
                    k=1    
                    for house in Beijing[select1.get()][select2.get()][select3.get()][select4.get()].keys():
                        if Beijing[select1.get()][select2.get()][select3.get()][select4.get()][house]:
                            tk.Radiobutton(top, text = house, variable = select5, value = house,command =layercheck).grid(row = 8,column = k)
                        else:
                            tk.Radiobutton(top, text = house, variable = select5, value = house,command =layercheck,fg = 'red').grid(row = 8,column = k)
                        k +=1
                    best = findbest(Beijing) 
                    besthouse.config(text = best)

import tkinter as tk 

Beijing={'东城区':{'a':{'g':{'h':{'j':True,'k':True}}},'b':{'l':{'m':{'o':True,'p':True}}}},'西城区':{'c':{'q':{'r':{'t':True,'u':True}}}}}
top = tk.Tk()
top.title("House Selector")

tk.Label(top, text = '最佳房源：',height = 3,font=("Arial", 15)).grid(row = 0,column = 999)
best = findbest(Beijing) 
besthouse = tk.Label(top, text = best,height = 3,font=("Arial", 15))
besthouse.grid(row = 0,column = 1000)


site = ["城区","楼号","单元","层数","户号"]
for ss in range(5):
    tk.Label(top, text = site[ss], font=("Arial", 12)).grid(row = ss+4,column = 0)

select1 = tk.StringVar()
select2 = tk.StringVar()
select3 = tk.StringVar()
select4 = tk.StringVar()
select5 = tk.StringVar()  

cl = 1
for district in Beijing.keys():
    tk.Radiobutton(top, text = district, variable = select1, value = district, command = districtcheck).grid(row = 4,column = cl)
    cl +=1

tk.Button(top, text = "标记删除", command = deleter).grid(row = 0,column = 997)
tk.Button(top, text = "标记恢复", command = recover).grid(row = 0,column = 998)

top.mainloop()
