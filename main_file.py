#主程式
from import_ import *
		
root = tk.Tk()
root.title('培勝老師,你好棒我好愛你')
root.geometry('650x450')
en = tk.StringVar()
la = tk.Label(root,text='使用者:',font = 50)
la.grid()
en = tk.Entry(root,text='',bg="gray",borderwidth = 2 , textvariable = en,width = 40)
en.grid()
btn = tk.Button(root,bd = 4, text='傳送訊息', command=lambda: btn_col(1, en, lb1, btn),height=2,width=8) 
btn.grid()
lb = tk.Label(root,text='機器人:',font = 50)
lb.grid()
lb1 = scrolledtext.ScrolledText(root,width=45,height=15, font=('UD Digi Kyokasho NP-B',15))
lb1.grid()
root.mainloop()
