from import_ import *
		
root = tk.Tk()
root.title('培勝老師,你好棒我好愛你')
root.geometry('550x450')
en = tk.StringVar()
la = tk.Label(root,text='使用者:',font = 50)
la.grid()
en = tk.Entry(root,text='',bg="gray",borderwidth = 2 , textvariable = en,width = 60)
en.grid()
btn = tk.Button(root,bd = 4, text='傳送訊息', command=lambda: btn_col(1, en, lb1, btn),height=2,width=8) 
#btn = tk.Button(root,bd = 4, text='傳送訊息', command=btn_col,height=2,width=8)
btn.grid()
lb = tk.Label(root,text='機器人:',font = 50)
lb.grid()
#lb1 = scrolledtext.ScrolledText(root,width=70,height=13)#滾動Lebal
#lb1.grid()

lb1 = tk.Label(root,height=50,width = 60,bg="gray",fg="black",font = 25, anchor = 'n', wraplength=550)
lb1.grid(padx=5)
root.mainloop()
