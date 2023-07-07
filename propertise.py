import tkinter
def show():
    print("button clicked")
if __name__=='__main__':
    window=tkinter.Tk()
    window.title("Propertise")
    window.geometry('600x400')
    label=tkinter.Label(window,text="More Features",bg="yellow",fg="red")
    label.pack()
    textentry=tkinter.Entry(window,bg="blue",fg="white",width="50")
    textentry.pack()
    button=tkinter.Button(window,text="Submit",bg="yellow",fg="red",activebackground="pink",activeforeground="blue",command=show)
    button.pack()
    window.mainloop()
