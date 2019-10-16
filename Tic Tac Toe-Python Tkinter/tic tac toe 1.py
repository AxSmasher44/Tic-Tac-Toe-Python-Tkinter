from tkinter import *
import random
import tkinter.messagebox

#Functions


def play(displaybox):
    if lb1.get(0, END) == "X":
        print("abc")



    displaybox.insert(END,"X")
    lists = ["", lb1, lb2, lb3, lb4, lb5, lb6, lb7, lb8, lb9]
    d = str(displaybox)
    if (lb1.get(ACTIVE) and lb2.get(ACTIVE) and lb3.get(ACTIVE) and lb4.get(ACTIVE) and
            lb5.get(ACTIVE) and lb6.get(ACTIVE) and lb7.get(ACTIVE) and lb8.get(ACTIVE) and lb9.get(ACTIVE)):
        return
    else:
        while True:

            z = random.randint(1, 9)
            y = str(z)
            r = str(("lb" + y))
            c = lists[z]
            if c.get(ACTIVE):
                pass
            elif c.get(0, END) != str:
                if r == d:
                    pass
                elif r != d:
                    c.insert(END, "O")
                    break
            """if (str(lb1.get(0, END) == "X" and str(lb5.get(0, END)) == "X" and str(lb9.get(0, END)) == "X" or
                    str(lb2.get(0, END)) == "X" and str(lb5.get(0, END)) == "X" and str(lb8.get(0, END)) == "X" or
                    str(lb3.get(0, END)) == "X" and str(lb5.get(0, END)) == "X" and str(lb7.get(0, END)) == "X" or
                    str(lb1.get(0, END)) == "X" and str(lb4.get(0, END)) == "X" and str(lb7.get(0, END)) == "X" or
                    str(lb3.get(0, END)) == "X" and str(lb6.get(0, END)) == "X" and str(lb9.get(0, END)) == "X" or
                    str(lb1.get(0, END)) == "X" and str(lb2.get(0, END)) == "X" and str(lb3.get(0, END)) == "X" or
                    str(lb4.get(0, END)) == "X" and str(lb5.get(0, END)) == "X" and str(lb6.get(0, END)) == "X" or
                    str(lb7.get(0, END)) == "X" and str(lb8.get(0, END)) == "X" and str(lb9.get(0, END)) == "X"):
                lbl1.configure(text = "You won")
                break
            elif (lb1.get(0, END) == "O" and lb5.get(0, END) == "O" and lb9.get(0, END) == "O" or
                  lb2.get(0, END) == "O" and lb5.get(0, END) == "O" and lb8.get(0, END) == "O" or
                  lb3.get(0, END) == "O" and lb5.get(0, END) == "O" and lb7.get(0, END) == "O" or
                  lb1.get(0, END) == "O" and lb4.get(0, END) == "X" and lb7.get(0, END) == "O" or
                  lb3.get(0, END) == "O" and lb6.get(0, END) == "O" and lb9.get(0, END) == "O" or
                  lb1.get(0, END) == "O" and lb2.get(0, END) == "O" and lb3.get(0, END) == "O" or
                  lb4.get(0, END) == "O" and lb5.get(0, END) == "O" and lb6.get(0, END) == "O" or
                  lb7.get(0, END) == "O" and lb8.get(0, END) == "O" and lb9.get(0, END) == "O"):
                tkinter.messagebox.showinfo("CPU WINS")
                break"""



#GUI
w = Tk()
w.geometry("600x600")
w.title("Tix Tax Tox")
lbl1 = Label(w, text = "Tix Tax Tox", font = ("CountryBlueprint", 30), fg = "#634108")

#Listboxes
boxes = StringVar()
lb1 = Listbox(w, height = "9", width="29", font = ("Times New Roman",80))
lb2 = Listbox(w, height = "9", width="29", font = ("Times New Roman",80))
lb3 = Listbox(w, height = "9", width="29", font = ("Times New Roman",80))
lb4 = Listbox(w, height = "9", width="29", font = ("Times New Roman",80))
lb5 = Listbox(w, height = "9", width="29", font = ("Times New Roman",80))
lb6 = Listbox(w, height = "9", width="29", font = ("Times New Roman",80))
lb7 = Listbox(w, height = "9", width="29", font = ("Times New Roman",80))
lb8 = Listbox(w, height = "9", width="29", font = ("Times New Roman",80))
lb9 = Listbox(w, height = "9", width="29", font = ("Times New Roman",80))

lists = [lb1, lb2, lb3, lb4, lb5, lb6, lb7, lb8, lb9]

#Buttons
btn1 = Button(w,text= "Place", font = ("Times New Roman", 15), command=lambda: play(lb1))
btn2 = Button(w,text= "Place", font = ("Times New Roman", 15), command=lambda: play(lb2))
btn3 = Button(w,text= "Place", font = ("Times New Roman", 15), command=lambda: play(lb3))
btn4 = Button(w,text= "Place", font = ("Times New Roman", 15), command=lambda: play(lb4))
btn5 = Button(w,text= "Place", font = ("Times New Roman", 15), command=lambda: play(lb5))
btn6 = Button(w,text= "Place", font = ("Times New Roman", 15), command=lambda: play(lb6))
btn7 = Button(w,text= "Place", font = ("Times New Roman", 15), command=lambda: play(lb7))
btn8 = Button(w,text= "Place", font = ("Times New Roman", 15), command=lambda: play(lb8))
btn9 = Button(w,text= "Place", font = ("Times New Roman", 15), command=lambda: play(lb9))



#Placements
lbl1.place(x=200, y=0)

lb1.place(x=10, y=60)
lb2.place(x=210, y=60)
lb3.place(x=410, y=60)
lb4.place(x=10, y=230)
lb5.place(x=210, y=230)
lb6.place(x=410, y=230)
lb7.place(x=10, y=400)
lb8.place(x=210, y=400)
lb9.place(x=410, y=400)

btn1.place(x=70, y=160)
btn2.place(x=270, y=160)
btn3.place(x=470, y=160)
btn4.place(x=70, y=330)
btn5.place(x=270, y=330)
btn6.place(x=470, y=330)
btn7.place(x=70, y=500)
btn8.place(x=270, y=500)
btn9.place(x=470, y=500)

lb1.delete(0,END)
w.mainloop()

























