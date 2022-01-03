#主程式
from import_ import *
		
root = tk.Tk()
root.title('聊天機器人')
root.geometry('610x430')
en = tk.StringVar()
la = tk.Label(root,text='使用者:',font = 50)
la.grid(column = 0,row = 0, sticky=tk.W)
en = tk.Entry(root,text='',bg="gray",borderwidth = 2 , textvariable = en,width = 40,font=('UD Digi Kyokasho NP-B',13))
en.grid(column = 0,row = 0, sticky=tk.W, padx=60)
btn = tk.Button(root,bd = 4, text='傳送訊息', command=lambda: btn_col(1, en, lb1, btn),height=1,width=8) 
btn.grid(column = 0,row = 0, sticky=tk.E)
lb = tk.Label(root,text='機器人:',font = 50)
lb.grid(column = 0,row = 3, sticky=tk.W)
lb1 = scrolledtext.ScrolledText(root,width=45,height=15, font=('UD Digi Kyokasho NP-B',15))
lb1.grid(column = 0,row = 4)
root.mainloop()
