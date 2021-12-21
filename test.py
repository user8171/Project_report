from tkinter import Tk, Button

def goodbye_world(var):
    print (var)
    button['command'] = lambda: hello_world(2)

def hello_world(var):
    print (var)
    button['command'] = lambda: goodbye_world(1)

root = Tk()
button = Button(root, text="Hello World!", command=lambda: goodbye_world(1))
button.pack()

root.mainloop()