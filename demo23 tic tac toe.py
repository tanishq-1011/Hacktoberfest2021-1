from tkinter import*
from time import sleep

root = Tk()
root.geometry("400x800")
#root.resizable(0,0)



def find_winner():

    ####rows
    if b1["text"] == b2["text"] ==b3["text"]:
        if b1["text"]=="0":
            print("Winner is Player1")
            l = Label(root, text = "Winner is Player1", font=("Arial", 19))
            l.grid(row=3,column=1)
            
        elif b1["text"]=="X":
            print("Winner is Player2")
            l = Label(root, text = "Winner is Player2", font=("Arial", 19))
            l.grid(row=3,column=1)
            
    if b4["text"] == b5["text"] ==b6["text"]:
        if b4["text"]=="0":
            print("Winner is Player1")
            l = Label(root, text  ="Winner is Player1", font=("Arial", 19))
            l.grid(row=3,column=1)
        elif b4["text"]=="X":
            print("Winner is Player2")
            l = Label(root, text ="Winner is Player2", font=("Arial", 19))
            l.grid(row=3,column=1)

    if b7["text"] == b8["text"] ==b9["text"]:
        if b7["text"]=="0":
            print("Winner is Player1")
            l = Label(root, text ="Winner is Player1", font=("Arial", 19))
            l.grid(row=3,column=1)
        elif b7["text"]=="X":
            print("Winner is Player2")
            l = Label(root, text ="Winner is Player2", font=("Arial", 19))
            l.grid(row=3,column=1)

    ####columns

    if b1["text"] == b4["text"] ==b7["text"]:
        if b4["text"]=="0":
            print("Winner is Player1")
            l = Label(root, text ="Winner is Player1", font=("Arial", 19))
            l.grid(row=3,column=1)
        elif b4["text"]=="X":
            print("Winner is Player2")
            l = Label(root, text ="Winner is Player2", font=("Arial", 19))
            l.grid(row=3,column=1)

    if b2["text"] == b5["text"] ==b8["text"]:
        if b2["text"]=="0":
            print("Winner is Player1")
            l = Label(root, text ="Winner is Player1", font=("Arial", 19))
            l.grid(row=3,column=1)
        elif b2["text"]=="X":
            print("Winner is Player2")
            l = Label(root, text ="Winner is Player2", font=("Arial", 19))
            l.grid(row=3,column=1)

    if b3["text"] == b6["text"] ==b9["text"]:
        if b3["text"]=="0":
            print("Winner is Player1")
            l = Label(root, text= "Winner is Player1", font=("Arial", 19))
            l.grid(row=3,column=1)
        elif b3["text"]=="X":
            print("Winner is Player2")
            l = Label(root, text ="Winner is Player2", font=("Arial", 19))
            l.grid(row=3,column=1)


    ###diagnols
    
    if b1["text"] == b5["text"] ==b9["text"]:
        if b1["text"]=="0":
            print("Winner is Player1")
            l = Label(root, text ="Winner is Player1", font=("Arial", 19))
            l.grid(row=3,column=1)
        elif b1["text"]=="X":
            print("Winner is Player2")
            l = Label(root, text ="Winner is Player2", font=("Arial", 19))
            l.grid(row=3,column=1)

    if b3["text"] == b5["text"] ==b7["text"]:
        if b3["text"]=="0":
            print("Winner is Player1")
            l = Label(root, text ="Winner is Player1", font=("Arial", 19))
            l.grid(row=3,column=1)
        elif b3["text"]=="X":
            print("Winner is Player2")
            l = Label(root, text ="Winner is Player2", font=("Arial", 19))
            l.grid(row=3,column=1)



x=1


def show(b):
    
    if b["text"]=="":
        global x
        x+=1
        if x%2==0:
            b["text"]= "0"
        else:
            b["text"]= "X"

        find_winner()
    
    
######
b1= Button(root,text="", width=5, height= 3, font=("Arial",30), command=lambda: show(b1))
b1.grid(row=0,column=0)

b2= Button(root,text="",width=5, height= 3, font=("Arial",30), command=lambda: show(b2))
b2.grid(row=0,column=1)

b3= Button(root,text="",width=5, height= 3, font=("Arial",30), command=lambda: show(b3))
b3.grid(row=0,column=2)

#######
b4= Button(root,text="", width=5, height= 3, font=("Arial",30), command=lambda: show(b4))
b4.grid(row=1,column=0)

b5= Button(root,text="",width=5, height= 3, font=("Arial",30), command=lambda: show(b5))
b5.grid(row=1,column=1)

b6= Button(root,text="",width=5, height= 3, font=("Arial",30), command=lambda: show(b6))
b6.grid(row=1,column=2)


#####
b7= Button(root,text="", width=5, height= 3, font=("Arial",30), command=lambda: show(b7))
b7.grid(row=2,column=0)

b8= Button(root,text="",width=5, height= 3, font=("Arial",30), command=lambda: show(b8))
b8.grid(row=2,column=1)

b9= Button(root,text="",width=5, height= 3, font=("Arial",30), command=lambda: show(b9))
b9.grid(row=2,column=2)


root.mainloop()

