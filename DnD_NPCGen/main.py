import tkinter
import getdata,writefile,pullnpc
from tkinter import Label, Tk, Canvas, Button, ttk, messagebox
import os

#CREATE WINDOW FOR PROGRAM
root = Tk() #creates window object
root.title("DnD Npc Generator") #sets window title
root.configure(width=800, height=400) #set dimensions of window

canvas = Canvas(root,width=500,height=500,bg='darkgrey')#create a canvas to put text on
canvas.create_text(250,50,text="Dungeon and Dragons NPC Generator",font=('Helvetica 19 bold'))#Text placed on the opened window
canvas.pack()

#generate data and open file
def getandlook():
    getdata.get_data(10)
    writefile.write_file()
    tkinter.messagebox.showinfo("Complete!","NPCs Generated!")
    pullnpc.usedbin.clear()

text = tkinter.Text(root,height=20,width=45)#create text box for npc data
text.place(x=120,y=90)
text.config(state='disabled')#disables ability to manually write in text box

#create a output of npc details on the window when 'pick' button is pressed
def npcprint():
    #label = tkinter.Label(root, text=pullnpc.pull_npc())
    text.config(state='normal')#changes state of text box to be written into
    text.delete('1.0', 'end')#clears the frist character to the last character of text within the box (where '1.0' is the first character and 'end' is the last character)
    text.insert('insert', pullnpc.pull_npc())#insert npc data to the textbox
    text.config(state='disabled')#close the textbox for edition once finished

#function to be able to clear the textbox
def clearall():
    text.config(state='normal')
    text.delete('1.0', 'end')
    text.config(state='disabled')

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
cleartext.place(x=20, y=170)

root.mainloop()
os.remove('npc.txt')#removes previous loaded file from last generate