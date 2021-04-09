from tkinter import *
from random import *
from tkinter.font import *

root=Tk()
root.title('Guessing Number by System')

def start():
    correct="n"
    a,b=1,100
    counter=1
    while correct!="y":
        my_guess=(a+b)//2
        label_result1=Label(root,text="My guess is ")
        label_result1.grid(row=2,column=0,sticky=S+W)
        label_result2=Label(root,text=my_guess)
        label_result2.grid(row=2,column=1)
        label_result3=Label(root,text="Is your number matchs my guess?(y/n)")
        label_result3.grid(row=3,column=0)
        entry=Entry(root)
        entry.grid(row=3,column=1)
        #button_next=Button(root,text="Next",command=Next)
        #button_next.grid(row=3,column=2,columnspan=3)
        #correct=entry.get()
        #if correct=="n":
            #label_result3=Label(root,text="Is your number is small or large than my guess(s/l):")
            #entry.delete(0,END)
            #acc=entry.get()
            #if acc=="s":
            #    b=my_guess
            #elif acc=="l":
            #    a=my_guess
            #counter+=1
    #print("I got it! After " + str(counter) + " trails")

def Next():
    pass

label_start=Label(root,text="You Guess a Number and i will find that number!\nAre you ready??\nLEt's get started...\nNow it's time for You to Guess a number between 1 and 100\nAfter you Guess the Number Press the below 'Start' button",font=Font(size=11))
label_start.grid(row=0,column=0)

button_start=Button(root,text="Start",padx=35,pady=3,borderwidth=5,font=Font(size=15),command=start)
button_start.grid(row=1,column=0,columnspan=2)

root.mainloop()