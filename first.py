import tkinter

def hello():
    print("Learning tkinter")
if __name__== '__main__':
    window=tkinter.Tk()
    window.title("Tkinter")
    window.geometry("500x500")
    label=tkinter.Label(window,text="Hello")
    label.pack()
    button=tkinter.Button(window,text="click",command=hello)
    button.pack()
    
window.mainloop()