from tkinter import *
def click(value):
    ex = entryField.get()  # 789 ex[0:len(ex)-1]

    if value=='C':
        ex = ex[0:len(ex)-1]  # 78
        entryField.delete(0, END)
        entryField.insert(0, ex)
        return

    elif value == 'AC':
        entryField.delete(0, END)
        return

    elif value == "/":  # 7/2=3.5
        entryField.insert(END, '/')
        return
    elif value == '=':
        answer = eval(ex)
    else:
        entryField.insert(END, value)
        return


    entryField.delete(0, END)
    entryField.insert(0, answer)


root=Tk()
root.title('Calculator')
root.config(bg='black')
root.geometry('300x320+80+80')

entryField=Entry(root,font=('arial',20,'bold'),bg='black',fg='white',bd=10,width=20)
entryField.grid(row=0,column=0,columnspan=4)

button_text_list=["C","(",")","AC",
                 "7","8","9","/",
                 "4","5","6","*",
                 "1","2","3","-",
                 "0",".","=","+"]
rowvalue=1
columnvalue=0
for m in button_text_list:

    button=Button(root,width=4,height=1,bd=2,text=m,bg='black',fg='white',
              font=('arial',18,'bold'),command=lambda button=m: click(button))
    button.grid(row=rowvalue,column=columnvalue)
    columnvalue+=1
    if columnvalue>3:
        rowvalue+=1
        columnvalue=0
root.mainloop()