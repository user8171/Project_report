from import_ import *

def btn_col(status_code):
	if en.get() != '':
		if status_code == 1:
			status = talking_function(en.get(), lb1, btn, status_code)
		elif status_code == 2:
			weather(input_, label_element, en.get(), btn, status_code)
	if status == '1':
		button_element.configure(command=lambda: btn_col(2))
		
root = tk.Tk()
root.title('培勝老師,你好棒我好愛你')
root.geometry('550x450')
en = tk.StringVar()
la = tk.Label(root,text='使用者:',font = 50)
la.grid()
en = tk.Entry(root,text='',bg="white",borderwidth = 2 , textvariable = en,width = 60)
en.grid()
btn = tk.Button(root,bd = 4, text='傳送訊息', command=lambda: btn_col(1),height=2,width=8) 
#btn = tk.Button(root,bd = 4, text='傳送訊息', command=btn_col,height=2,width=8)
btn.grid()
lb = tk.Label(root,text='機器人:',font = 50)
lb.grid()
lb1 = scrolledtext.ScrolledText(root,width=70,height=13)#滾動Lebal
lb1.grid()
#lb1 = tk.Label(root,height=50,width = 60,bg="white",fg="black",font = 25, anchor = 'n')
#lb1.grid(padx=5)
root.mainloop()