from import_ import *

def btn_col():
	if en.get() != '':
		#取得使用者輸入的文字
		#en.get()

		talking_function(en.get(), lb1)

root = tk.Tk()
root.title('talking robot') #拜託不要叫line bot(沒有用到line api) 
root.geometry('700x700')
en = tk.StringVar()
la = tk.Label(root,text='使用者:',font = 50)
la.pack()
en = tk.Entry(root,text='',bg="white",borderwidth = 2 , textvariable = en,width = 60)
en.pack(padx=10)
btn = tk.Button(root,bd = 4, text='傳送訊息', command=btn_col,height=2,width=8)
btn.pack()
lb = tk.Label(root,text='機器人:',font = 50)
lb.pack()
lb1 = tk.Label(root,height=50,width = 60,bg="white",fg="black",font = 25, anchor = 'n')
lb1.pack(padx=5)
root.mainloop()