import tkinter
import getdata,writefile,pullnpc
from tkinter import Label, Tk, Canvas, Button, Widget, ttk, messagebox, Entry
import os

#CREATE WINDOW FOR PROGRAM
root = Tk() #creates window object
root.title("DnD Npc Generator") #sets window title
root.configure(width=800, height=400) #set dimensions of window

canvas = Canvas(root,width=600,height=500,bg='darkgrey')#create a canvas to put text on
canvas.create_text(250,50,text="Dungeon and Dragons NPC Generator",font=('Helvetica 19 bold'))#Text placed on the opened window
canvas.pack()

#textbox for user to pull specific number of npcs
tb = tkinter.Entry(root, width=5, text='10')
tb.insert(0,'10')
tb.pack()
tb.place(x=80,y=90)

text = tkinter.Text(root,height=20,width=55, wrap=tkinter.WORD)#create text box for npc data
text.place(x=120,y=90)
text.config(state='disabled')#disables ability to manually write in text box

#generate data and open file
def getandlook():
    total = int(tb.get()) #casts the entry box input into an integer
    if total % 10 != 0:
        text.config(state='normal')
        text.delete('1.0', 'end')
        text.insert('insert', 'ERROR: program only generates in increments of 10')
        text.config(state='disabled')
    else:
        getdata.get_data(total)
        writefile.write_file()
        tkinter.messagebox.showinfo("Complete!","NPCs Generated!")
    pullnpc.usedbin.clear()

#create a output of npc details on the window when 'pick' button is pressed
def npcprint():
    text.config(state='normal')#changes state of text box to be written into
    text.delete('1.0', 'end')#clears the frist character to the last character of text within the box (where '1.0' is the first character and 'end' is the last character)
    text.insert('insert', pullnpc.pull_npc())#insert npc data to the textbox
    text.config(state='disabled')#close the textbox for edition once finished

#function to be able to clear the textbox
def clearall():
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.config(state='disabled')

# #function to pull multiple npcs
e = tkinter.Entry(root, width=5)#create entry box for numbers
e.pack()
e.place(x=60, y=155)

#Function to control the 'pick many' option of taking multiple entries out of the data
def pickmany():
    val = int(e.get()) #casts the entry box input into an integer
    if val < 9 and val > 0:
        while val != 0: #loop to print out multiple npcs for number inputed
            text.config(state='normal')#changes state of text box to be written into
            text.insert('insert', pullnpc.pull_npc())
            text.insert('insert', '\n')
            val = val - 1
        text.config(state='disabled')
    else:
        text.insert('insert', 'ERROR: Incorrect input entered (digits 1-9)')

#funtion to show pickmany function
def showmany():
    text.config(state='normal')#changes state of text box to be written into
    text.delete('1.0', 'end')
    text.insert('insert', pickmany())#insert npc data to the textbox
    text.config(state='disabled')#close the textbox for edition once finished

#create button to pick many
pickmore = Button(root, text="Pick :", command=showmany, highlightbackground='lightgray')
pickmore.place(x=20, y=150)

#creates a button to generate the text file of npcs
generate = Button(root, text="generate!", command= getandlook ,highlightbackground='lightgray')
generate.place(x=20,y=90)

#Button to pull random NPC from list of downloaded NPCs
pick = Button(root, text="Pick One", command=npcprint, highlightbackground='lightgray')
pick.place(x=20, y=120)

#Button to close the window
close = Button(root,text="Close", command=root.destroy, highlightbackground='lightgray')
close.place(x=20,y=390)

#Button to clear generated text from window
cleartext = Button(root, text='Clear', command=clearall, highlightbackground='lightgray')
cleartext.place(x=20, y=200)

root.mainloop()
os.remove('npc.txt')#removes previous loaded file from last generate