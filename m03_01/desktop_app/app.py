from tkinter import Tk, Label, Button, Entry


def handler():
    text = txt.get()
    txt.delete(0, 'end')
    lbl.configure(text=text)

wnd = Tk()

wnd.title('My App')
wnd.geometry('800x600')
wnd.resizable(False, False)


lbl = Label(wnd, text='Python Web #7', font=('Arial', 21), fg='#168D4E')
lbl.place(x=40, y=30)


btn_close = Button(wnd, text='Close', font=('Courier', 16), fg='#E9102E', command=wnd.destroy)
btn_close.place(x=700, y=30)

txt = Entry(wnd, width=30, font=('Courier', 16))
txt.place(x=40, y=200)
btn_txt = Button(wnd, text='Edit title', font=('Courier', 16), fg='#E9102E', command=handler)
btn_txt.place(x=40, y=250)

wnd.mainloop()
