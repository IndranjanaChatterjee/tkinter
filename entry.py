import tkinter
if __name__=='__main__':
    window=tkinter.Tk()
    window.title("For Entry")
    window.geometry('500x500')
    def submit():
        print("Submitted")
    label=tkinter.Label(window,text="Enter some text")
    label.pack()
    text=tkinter.Entry(window)
    text.pack()
    button=tkinter.Button(window,text="submit",command=submit)
    button.pack()
    window.mainloop()