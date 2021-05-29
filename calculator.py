from tkinter import *
expression=""
def press(num):
    global expression

    expression=expression+ str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression

        total=str(eval(expression))
        equation.set(total)
    except:
        equation.set("ERROR")
        expression=""
        

def clear():
    global expression
    expression=""
    equation.set("Enter your Expression")
if __name__=='__main__':
    x=Tk()
    x.resizable(0,0)
    x.configure(bg='black')
    x.geometry("320x340")

    equation=StringVar()

    exp=Entry(x,textvariable=equation, font="25")

    exp.grid(columnspan=4, ipadx=70, pady=10)
    equation.set("Enter your Expression")

    but1=Button(x, text='1', fg='white', bg='red',command=lambda:press(1), height=2, width=7).grid(row=2, column=0, pady=2)
    but2=Button(x, text='2', fg='black', bg='pink',command=lambda:press(2), height=2, width=7).grid(row=2, column=1, pady=2)
    but3=Button(x, text='3', fg='white', bg='red',command=lambda:press(3), height=2, width=7).grid(row=2, column=2, pady=2)
    but4=Button(x, text='4', fg='black', bg='pink',command=lambda:press(4), height=2, width=7).grid(row=3, column=0, pady=2)
    but5=Button(x, text='5', fg='white', bg='red',command=lambda:press(5), height=2, width=7).grid(row=3, column=1, pady=2)
    but6=Button(x, text='6', fg='black', bg='pink',command=lambda:press(6), height=2, width=7).grid(row=3, column=2, pady=2)
    but7=Button(x, text='7', fg='white', bg='red',command=lambda:press(7), height=2, width=7).grid(row=4, column=0, pady=2)
    but8=Button(x, text='8', fg='black', bg='pink',command=lambda:press(8), height=2, width=7).grid(row=4, column=1, pady=2)
    but9=Button(x, text='9', fg='white', bg='red',command=lambda:press(9), height=2, width=7).grid(row=4, column=2, pady=2)
    but0=Button(x, text='0', fg='white', bg='red',command=lambda:press(0), height=2, width=7).grid(row=5, column=1, pady=2)
    plus=Button(x, text='+', fg='white', bg='red',command=lambda:press('+'), height=2, width=7).grid(row=3, column=3, pady=2)
    minus=Button(x, text='-', fg='black', bg='pink',command=lambda:press('-'), height=2, width=7).grid(row=4, column=3, pady=2)
    product=Button(x, text='*', fg='white', bg='red',command=lambda:press('*'), height=2, width=7).grid(row=5, column=3, pady=2)
    
    div=Button(x, text='/', fg='black', bg='pink',command=lambda:press('/'), height=2, width=7).grid(row=2, column=3, pady=2)
    clear=Button(x, text='AC', fg='black', bg='pink',command=clear, height=2, width=7).grid(row=5, column=0, pady=2)
    dot=Button(x, text='.', fg='black', bg='pink',command=lambda:press('.'), height=2, width=7).grid(row=5, column=2, pady=2)
    EQUAL=Button(x, text='=', fg='maroon', bg='orange',command=equalpress, height=2, width=7).grid(row=7, columnspan=8, sticky='nsew',padx=2, pady=10)
    int=Button(x, text="Int", fg="gold", bg="red", command=lambda:press('//'),height=2, width=7).grid(row=6, column=0, pady=2)
    rem=Button(x, text="Remainder", fg="black", bg="pink", command=lambda:press('%'),height=2, width=7).grid(row=6, column=1, pady=2)
    pow=Button(x, text="Power", fg="gold", bg="red", command=lambda:press('**'),height=2, width=7).grid(row=6, column=2, pady=2)
    int=Button(x, text="Sq.", fg="gold", bg="red", command=lambda: press('**2'), height=2, width=7).grid(row=6, column=3, pady=2)

    
    x.mainloop()


