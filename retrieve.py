import tkinter
if __name__=='__main__':
    window=tkinter.Tk()
    def gettext():
        print(textentry.get())
    window.title("retrieving text")
    window.geometry('500x500')
    label=tkinter.Label(window,text="Retrieving text from entry",bg="green",fg="black")
    label.pack()
    textentry=tkinter.Entry(window,bg="yellow",fg="red",width="50")
    textentry.pack()
    button=tkinter.Button(window,text="submit",bg="yellow",fg="red",command=gettext)
    button.pack()
    window.mainloop()