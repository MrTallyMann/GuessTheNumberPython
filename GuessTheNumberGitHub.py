from ttkthemes import ThemedTk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
#window = ThemedTk(theme="equilux")
#window.config(themebg="equilux")
import random

window = Tk()
window.geometry("500x300")

tries = 0

upArrow = PhotoImage(file="uparrow.png")
downArrow = PhotoImage(file="downarrow.png")
correct = PhotoImage(file="correct.png")
dice = PhotoImage(file="die.png")

number = 0

var = StringVar()

def exit():
    window.destroy()

def playerGuess(event):
    global number
    global upArrow
    global downArrow
    global correct
    global diceLbl
    global var
    global tries
    global triesLbl
    global answerEntry

    if int(answerEntry.get()) == number:
        diceLbl.configure(image=correct)
        tries = tries + 1
        triesLbl.configure(text="Tries: " + str(tries))
        randomizeBtn.configure(state=ACTIVE)
        tries = 0
    elif int(answerEntry.get()) > number:
        diceLbl.configure(image= downArrow)
        tries = tries+1
        triesLbl.configure(text="Tries: "+str(tries))
        randomizeBtn.configure(state=ACTIVE)
    elif int(answerEntry.get()) < number:
        diceLbl.configure(image=upArrow)
        tries = tries + 1
        triesLbl.configure(text="Tries: " + str(tries))
        randomizeBtn.configure(state=ACTIVE)

    answerEntry.delete(0, 'end')



def Difficulty():
    global number
    global upArrow
    global downArrow
    global correct
    global dicelbl
    if rb.get() == "First":
        number = random.randint(0, 50)
        randomizeBtn.configure(state= DISABLED)
    elif rb.get() == "Second":
        number = random.randint(0, 100)
        randomizeBtn.configure(state= DISABLED)
    elif rb.get() == "Third":
        number = random.randint(0, 200)
        randomizeBtn.configure(state= DISABLED)

rb = StringVar()

titleLbl = Label(text="Guess the Number", font=("Arial",15))
titleLbl.grid(column=1, row=0)

rad1 = Radiobutton(window, text="Easy(0-50)", value="First", variable=rb, font=("Arial",10))
rad1.grid(column=0, row=1)

rad2 = Radiobutton(window, text="Normal(0-100)", value="Second", variable=rb, font=("Arial",10))
rad2.grid(column=1, row=1)

rad3 = Radiobutton(window, text="Hard(0-200)", value="Third", variable=rb, font=("Arial",10))
rad3.grid(column=2, row=1)

tutorialLbl1 = Label(text="In this game you will try to find a secret number", font=("Arial",10))
tutorialLbl1.grid(column=1, row=2)

tutorialLbl2 = Label(text="that is randomly chosen every round.", font=("Arial",10))
tutorialLbl2.grid(column=1, row=3)

tutorialLbl3 = Label(text="Try to guess it with the least possible tries!", font=("Arial",10))
tutorialLbl3.grid(column=1, row=4)

exitBtn = Button(text="Exit", font=("Arial",15), command= exit)
exitBtn.grid(column=2, row=5)

randomizeBtn = Button(text="Randomize", font=("Arial",15), command= Difficulty)
randomizeBtn.grid(column=2, row=6)

answerEntry = Entry(window, font=("Arial",15))
answerEntry.grid(column=1, row=5)

triesLbl = Label(text="Tries: ", font=("Arial",15))
triesLbl.grid(column=1, row=6)

diceLbl = Label(image=dice)
diceLbl.grid(column=0, row=6)

window.bind("<Return>", playerGuess)
window.mainloop()
