from tkinter import *
import tkinter
prefix_list_allowed=['192.168.2.3','192.168.2.4','192.168.2.5']
def Writetomenu():
    root= Tk()
    text=Text(root)
    for y in prefix_list_allowed:
        text.insert(INSERT,y+"\n")
        text.tag_config(y, background="black", foreground="green")
        print(y)

    text.pack()
    root.mainloop()






k= input('start writing to window? y/n')
if k=='y':
    root = tkinter.Tk()
    root.geometry('250x250')
    B=tkinter.Button(root,activeforeground='blue',activebackground='cyan',padx='25',pady='25',text='Show Configuration list',command=Writetomenu)
    B.pack()
    root.mainloop()

else:
    Exit()
