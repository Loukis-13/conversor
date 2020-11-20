from tkinter import*

def bt_click():
    n=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '-', '_')
    a = int(e1.get())
    b = int(e2.get())
    y = (e3.get())
    z = str()
    w = int()
    k = str()
    
    #others bases to decimal base
    if b==10:
        for i in range(len(y)):
            if y[-(i + 1)] != "0":
                for j in n:
                    if j == y[-(i + 1)]:
                        break
                    k = k + j
                w = w + (len(k) * (a ** i))
                k=""
        l4["text"] = w
    
    #decimal base to others bases
    elif a==10:
        x = int(y)
        while x > 0:
            z=(n[(x % b)] + z)
            x=(x // b)
        l4["text"] = z
    
    #others bases to others bases
    else:
        for i in range(len(y)):
            if y[-(i + 1)] != "0":
                for j in n:
                    if j == y[-(i + 1)]:
                        break
                    k = k + j
                w = w + (len(k) * (a ** i))
                k=""
    
        while w > 0:
            z=(str(w % b) + z)
            w=(w // b)
        l4["text"] = z

janela = Tk()
janela.title("Conversor")
janela.geometry("280x240")

v0=Label(janela);v0.pack()
frame = Frame(janela);frame.pack()

l1 = Label(frame, text="From wich base you want to convert:")
l1.grid(row=0,column=1)
l11 = Label(frame, text="Min.2 ", fg="grey"); l11.grid(row=1, column=0)
l12 = Label(frame, text="Max.64", fg="grey"); l12.grid(row=1, column=2)
e1 = Entry(frame, width=28, borderwidth=2)
e1.grid(row=1,column=1)

l2 = Label(frame, text="To wich base you want to convert:")
l2.grid(row=2,column=1)
l13 = Label(frame, text="Min.2 ", fg="grey"); l13.grid(row=3, column=0)
l14 = Label(frame, text="Max.64", fg="grey"); l14.grid(row=3, column=2)
e2 = Entry(frame, width=28, borderwidth=2)
e2.grid(row=3,column=1)

v1=Label(frame); v1.grid(row=4,column=1)

l3 = Label(frame, text="Type the number:")
l3.grid(row=5,column=1)
e3 = Entry(frame, width=28, borderwidth=2)
e3.grid(row=6,column=1)

l4 = Label(frame, text="Result")
l4.grid(row=7,column=1)

bt = Button(janela, text="convert", command=bt_click)
bt.pack()

janela.mainloop()
